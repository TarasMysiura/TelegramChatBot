from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = "5863212826:AAHfHUxMQlImc98FwRkjwa4aRefArGCmjbY"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
     await update.message.reply_text("Вітаю у моєму боті")


def run():
    aplication = ApplicationBuilder().token(BOT_TOKEN).build()
    
    aplication.add_handler(CommandHandler("start", start))
    aplication.add_handler(CommandHandler("help", start))

    aplication.run_polling()


if __name__ == "__main__":
    run()
