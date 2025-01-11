from fastapi import FastAPI, Request
from LUNA import TeleHook, BOT_ID, ECHO
import requests

app = FastAPI()


#################################################################

def download_plugin(plugin_url):
    response = requests.get(plugin_url)
    if response.status_code == 200:
        plugin_id = plugin_url.split("main/")[1]
        with open(f"LUNA/plugins/{plugin_id}", "wb") as file:
            file.write(response.content)
        return True
    return False


plugin_list = ECHO.setup_plugins(BOT_ID)
for plugin_url in plugin_list:
    download_plugin(plugin_url)



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
