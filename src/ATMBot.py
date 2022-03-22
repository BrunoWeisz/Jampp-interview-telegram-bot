from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, JobQueue
from telegram import Update
import datetime
import pytz

from src.CSVReader import CSVReader
from src.ATMBotNotifier import ATMBotNotifier
from src.LoggingConfiguration import LoggingConfiguration
from src.SearchEngine import SearchEngine
from src.ExtractionAgent import ExtractionAgent
from src.CSVWriter import CSVWriter
from src.ExtractionRestorer import ExtractionRestorer

class ATMBot:
    def __init__(this):

        this.initializeConstants()
        this.initializeBasicBotComponents()
        LoggingConfiguration().startLogging()
        this.initializeHandlers()

        this.initializeSearchEngines()
        this.initializeExtractionAgents()

        this.setDailyRestauration()    

    #Initialization

    def initializeConstants(this):
        this.routeToLink = 'files/cajeros-automaticos-link.csv'
        this.routeToBanelco = 'files/cajeros-automaticos-banelco.csv'
        this.API_KEY = '5111062134:AAHLgQS7JDDvZY5I__shCnRG5i5oDCAsRXA'

    def initializeBasicBotComponents(this):
        this.updater = Updater(token = this.API_KEY, use_context = True)
        this.dispatcher = this.updater.dispatcher
        this.queue = this.updater.job_queue
        this.notifier = ATMBotNotifier()

    def initializeHandlers(this):
    
        this.dispatcher.add_handler(CommandHandler('start', this.start))
        this.dispatcher.add_handler(CommandHandler('link', this.link))
        this.dispatcher.add_handler(CommandHandler('banelco', this.banelco))
        this.dispatcher.add_handler(MessageHandler(Filters.location, this.handleLocationReceive))

        this.updater.start_polling()

    def initializeSearchEngines(this):
        this.linkSearch = SearchEngine(this, CSVReader(this.routeToLink))
        this.banelcoSearch = SearchEngine(this, CSVReader(this.routeToBanelco))
        this.currentSearch = None

    def initializeExtractionAgents(this):
        this.extractionAgentLink = ExtractionAgent(CSVWriter(this.routeToLink))
        this.extractionAgentBanelco = ExtractionAgent(CSVWriter(this.routeToBanelco))
        this.currentExtractionAgent = None

    
    
# Bot handlers
        
    def handleLocationReceive(this, update, context):
        location = update.message.location 
        lat = location.latitude
        long = location.longitude

        inRangeATMIndexes, atmData = this.currentSearch.validATMs(long, lat)
        this.currentExtractionAgent.extractFromBanks(inRangeATMIndexes, atmData)

        this.notifier.showCloseATMs(update, context, inRangeATMIndexes, atmData, [lat, long])
    
    def start(this, update: Update, context: CallbackContext):
        this.notifier.welcomeMessage(update, context)

    def link(this, update: Update, context: CallbackContext):
        this.linkSearch.deploySearch(update, context)
        this.currentExtractionAgent = this.extractionAgentLink

    def banelco(this, update: Update, context: CallbackContext):
        this.banelcoSearch.deploySearch(update, context)
        this.currentExtractionAgent = this.extractionAgentBanelco

# Bot state management

    def setCurrentSearchEngine(this, aSearchEngine):
        this.currentSearch = aSearchEngine

# Messages to user

    def deploySearchForValidSearch(this, update, context, aSearchEngine):
        this.notifier.requestLocation(update, context)

# Persistence 

    def setDailyRestauration(this):
        this.extractionRestorer = ExtractionRestorer()
        timeOfRestauration = datetime.time(19,1,15)
        timezone = pytz.timezone('Etc/GMT-3')
        timeOfRestauration = timezone.localize(timeOfRestauration)
        this.queue.run_daily(callback = this.restoreExtractions, 
                             time = timeOfRestauration, 
                             days = (0,1,2,3,4))


    def restoreExtractions(this, context):
        this.extractionRestorer.restoreExtractions(this.routeToLink)
        this.extractionRestorer.restoreExtractions(this.routeToBanelco)



    