

class config():
    def __init__(self):
        self.BOT_TOKEN = "7774715976:AAFvr3nnh7ljMeG4QBAR2oR29dUEr4T0W4Y"
        self.WEBHOOK_URL = "https://pup-solid-publicly.ngrok-free.app/webhook"
        self.DATABASE_URI = "mongodb+srv://ishikkii:accha123@luna.tcbij.mongodb.net/?retryWrites=true&w=majority&appName=luna"
        self.ECHOCORE_TOKEN = "12345-EchoCore-Blue-6789-353678578"

        self.OWNER_ID = 1234567890

        self.BOT_ID = int(self.BOT_TOKEN.split(":")[0])