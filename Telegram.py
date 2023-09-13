import telegram.ext
import os
from dotenv import load_dotenv

# Load Telegram token from environment variables
load_dotenv()
telegram_token = os.getenv("TELEGRAM_TOKEN")

updater = telegram.ext.Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

# Commands and their responces
def start(update, context):
    update.message.reply_text('Hello welcome to Svelte help.')

def help(update, context):
    update.message.reply_text(
        '''
        /start -> Welcome to Svelte help!
        /help -> See all list of commands
        /beginner -> Get free resources for beginners
        /uilib -> UI libraries for svelte
        /channels -> Useful Youtube channels related on svelte
        /deploy -> Deploy your project
        '''
    )

def beginner(update, context):
    update.message.reply_text('Svelte is a javascript framework.')

def uilib(update, context):
    update.message.reply_text('There are several UI Libraries for svelte. Most of these libries use tailwindcss so you should be fimilar with it.')

def channels(update, context):
    update.message.reply_text('These are some useful channels- ')

def deploy(update, context):
    update.message.reply_text('There are various methods to deploy your projects. These are the useful ones- ')

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('beginner', beginner))
dispatcher.add_handler(telegram.ext.CommandHandler('uilib', uilib))
dispatcher.add_handler(telegram.ext.CommandHandler('channels', channels))
dispatcher.add_handler(telegram.ext.CommandHandler('deploy', deploy))

updater.start_polling()
updater.idle()