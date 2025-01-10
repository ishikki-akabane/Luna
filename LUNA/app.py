from flask import Flask, request
from LUNA import TeleHook, BOT_TOKEN


app = Flask(__name__)

@app.route("/haha")
def home_endpoint():
    return "Telegram Bot is running."

@app.route('/', methods=['POST'])
async def webhook_endpoint():
    try:
        update = request.get_json()
        await TeleHook.process_update(update)      
    except Exception as e:
        print(e)
    return 'ok'

@app.route("/run")
def run_endpoint():
    result = TeleHook.setup_webhook()
    return result

TeleHook.load_plugins()