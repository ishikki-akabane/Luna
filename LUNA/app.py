from fastapi import FastAPI, Request
from LUNA import TeleHook, BOT_TOKEN
import requests

app = FastAPI()


#################################################################

async def setup_plugins():
    response = requests.get("https://testing.vercel.app")

def download_plugin(plugin_name, plugin_url):
    response = requests.get(plugin_url)
    if response.status_code == 200:
        with open(f"LUNA/plugins/{plugin_name}", "wb") as file:
            file.write(response.content)
        return True
    return False


download_plugin("vercel.json", "https://raw.githubusercontent.com/ishikki-akabane/TeleHook/main/vercel.json")


@app.get("/")
async def home_endpoint():
    return {"message": "Telegram Bot is running."}

@app.post("/webhook")
async def webhook_endpoint(request: Request):
    try:
        update = await request.json()
        await TeleHook.process_update(update)
    except Exception as e:
        print(e)
        return {"error": str(e)}
    return {"status": "ok"}

@app.get("/run")
async def run_endpoint():
    try:
        result = TeleHook.setup_webhook()
        return {"webhook_setup_result": result}
    except Exception as e:
        return {"error": str(e)}


TeleHook.load_plugins()
