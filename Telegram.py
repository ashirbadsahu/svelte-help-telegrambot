import telegram.ext
import requests
from dotenv import Token

Token()

updater = telegram.ext.updater(Token, useContext = True)
dispatcher = updater.dispatcher

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
        /whatis -> Get information about a Svelte feature
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

def whatis(update, context):
    if len(context.args) == 0:
        update.message.reply_text('Please provide a feature name to search for.')
    else:
        feature_name = ' '.join(context.args)
        response = requests.get(f'https://svelte.dev/docs/{feature_name}')
        if response.status_code == 200:
            update.message.reply_text(response.url)
        else:
            update.message.reply_text(f'Could not find information about {feature_name} in Svelte docs.')