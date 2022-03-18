from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update


from CSVReader import CSVReader
from ATMBotNotifier import ATMBotNotifier
from LoggingConfiguration import LoggingConfiguration
from SearchEngine import ValidSearchEngine, NullSearchEngine
from PointMapGenerator import PointMapGenerator

class ATMBot:
    def __init__(this):
        routeToLink = './cajeros-automaticos-link.csv'
        routeToBanelco = './cajeros-automaticos-banelco.csv'
        this.API_KEY = '5111062134:AAHLgQS7JDDvZY5I__shCnRG5i5oDCAsRXA'

        this.updater = Updater(token = this.API_KEY, use_context = True)
        this.dispatcher = this.updater.dispatcher
        this.notifier = ATMBotNotifier()

        LoggingConfiguration().startLogging()
        this.initHandlers()

        this.linkSearch = ValidSearchEngine(this, CSVReader(routeToLink))
        this.banelcoSearch = ValidSearchEngine(this, CSVReader(routeToBanelco))
        this.nullSearch = NullSearchEngine(this)
        this.currentSearch = this.nullSearch


    def initHandlers(this):
        start_handler = CommandHandler('start', this.start) 
        this.dispatcher.add_handler(start_handler)
        this.updater.start_polling()

        link_handler = CommandHandler('link', this.link)
        this.dispatcher.add_handler(link_handler)

        banelco_handler = CommandHandler('banelco', this.banelco)
        this.dispatcher.add_handler(banelco_handler)

        location_handler = MessageHandler(Filters.location, this.handleLocationReceive)
        this.dispatcher.add_handler(location_handler)

# Bot handlers
        
    def handleLocationReceive(this, update, context):
        location = update.message.location 
        lat = location.latitude
        long = location.longitude

        #this.notifier.displayCoordinatesToUser(update, context, lat, long)
        atmInfo = this.currentSearch.validATMs(long, lat)
        this.notifier.showCloseATMs(update, context, atmInfo)
        pathToMap = PointMapGenerator().generateMap(
                                                    [lat,long],
                                                    map(
                                                        lambda data : [data[3],data[2]],
                                                        atmInfo
                                                    ))

        this.notifier.sendImage(update, context, pathToMap)
    
    def start(this, update: Update, context: CallbackContext):
        this.notifier.welcomeMessage(update, context)

    def link(this, update: Update, context: CallbackContext):
        this.linkSearch.deploySearch(update, context)

    def banelco(this, update: Update, context: CallbackContext):
        this.banelcoSearch.deploySearch(update, context)

# Bot state management

    def setCurrentSearchEngine(this, aSearchEngine):
        this.currentSearch = aSearchEngine

# Messages to user

    def deploySearchForValidSearch(this, update, context, aSearchEngine):
        this.notifier.requestLocation(update, context)

    def deploySearchForNullSearch(this, update, context):
        this.notifier.noSearchMessage(update, context)

    def deployValidATMsForNullSearch(this):
        this.notifier.noSearchMessage(update, context)




    