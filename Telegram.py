import telegram.ext

Token = "6466483620:AAEKWIsizoVuayz7rprof04uT0LdbaNdv7w"

updater = telegram.ext.updater('6466483620:AAEKWIsizoVuayz7rprof04uT0LdbaNdv7w', useContext = True)
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