from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, this is your Telegram bot!")

def main():
    TOKEN = "7590187559:AAG3LzMwLj-koPQ_t6Z3IhxpgT0ud0bRMwM"
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
