from telegram import KeyboardButton, ReplyKeyboardMarkup

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

    def showCloseATMs(this, update, context, atmDataList):
        if len(atmDataList) == 0:
            this.notifyNoATMsNearby(update, context)
        else:
            messages = []
            for atm in atmDataList:
                messages.append('Nombre del banco: ' + atm[0] + '\nDireccion: ' + atm[1])
            
            context.bot.send_message(
                chat_id = update.effective_chat.id,
                text = '\n\n'.join(messages))

    def notifyNoATMsNearby(this, update, context):
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "No existen cajeros automaticos de la red seleccionada a menos de 500 metros de su ubicacion")

    def sendImage(this, update, context, path):
        context.bot.send_photo(
            chat_id = update.effective_chat.id,
            photo = open(path, 'rb')
        )