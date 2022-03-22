from telegram import KeyboardButton, ReplyKeyboardMarkup
from src.PointMapGenerator import PointMapGenerator

class ATMBotNotifier:

    def welcomeMessage(this, update, context):
        welcomeText = 'Para usar este bot, debe introducir los comandos /link o /banelco'
        context.bot.send_message(chat_id= update.effective_chat.id, text= welcomeText)

    def requestLocation(this, update, context):
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = 'Comparta ubicacion para localizar los cajeros automaticos mas cercanos',
            reply_markup = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text= 'Presione para compartir su ubicacion actual.',request_location = True)]],
                                                one_time_keyboard= True,
                                                resize_keyboard = True)	
        )

    def displayCoordinatesToUser(this, update, context, lat, long):
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = 'Latitude: ' + str(lat) + '\nLongitude: ' + str(long) )

    def noSearchMessage(this, update, context):
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = 'Esta busqueda no es valida')

    def showCloseATMs(this, update, context, inRangeATMIndexes, atmData, userPosition):

        currentATMs = list(map(lambda index : atmData[index], inRangeATMIndexes))
        currentATMs = list(filter(lambda atm : this.hasExtractionsLeft(atm), currentATMs))
        messagesToSend = list(map(lambda atm : this.atmDisplayString(atm), currentATMs))

        if len(messagesToSend) == 0:
            this.notifyNoATMsNearby(update, context)
            return

        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = '\n\n'.join(messagesToSend))

        this.sendPositionalMap(userPosition, currentATMs, update, context)
   

#Private

    def hasExtractionsLeft(this, anATM):
        return float(anATM[len(anATM)-1]) >= 1

    def atmDisplayString(this, anATM):
        return 'Nombre del banco: ' + anATM[3] + '\nDireccion: ' + anATM[5] + '\nExtracciones restantes: ' + anATM[len(anATM)-1]

    def notifyNoATMsNearby(this, update, context):
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "No existen cajeros automaticos de la red seleccionada a menos de 500 metros de su ubicacion")

#Map sending

    def sendPositionalMap(this, userPosition, currentATMs, update, context):
        pathToMap = PointMapGenerator().generateMap(
                                                userPosition,
                                                map(
                                                    lambda data : [data[2],data[1]],
                                                    currentATMs
                                                ))

        this.sendImage(update, context, pathToMap)

    def sendImage(this, update, context, path):
        context.bot.send_photo(
            chat_id = update.effective_chat.id,
            photo = open(path, 'rb')
        )