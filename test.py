import requests

def download_plugin(plugin_name, plugin_url):
    #raw_url = plugin_url.replace("github.com", "raw.githubusercontent.com")
    response = requests.get(plugin_url)
    if response.status_code == 200:
        with open(plugin_name, "wb") as file:
            file.write(response.content)
        return True
    return False


download_plugin("vercel.json", "https://raw.githubusercontent.com/ishikki-akabane/TeleHook/main/vercel.json")