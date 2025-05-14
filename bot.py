# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #
import pytz, time
from config import DS
from aiohttp import web
from pyrogram import Client
from translation import TXT
from datetime import date, datetime
from DSCAPTION.web_support import web_server
from DSCAPTION.buttons import temp

# ===================== [ Running Client ] ===================== #

class DS_AutoCaptionBot(Client):
    def __init__(self):
        super().__init__(
            "DS-AutoCaptionBot",
            api_id=DS.API_ID,
            api_hash=DS.API_HASH,
            bot_token=DS.BOT_TOKEN,
            workers=200,
            plugins={"root": "DSCAPTION"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        temp.U_NAME = me.username
        temp.B_LINK = me.mention
        self.uptime = DS.BOT_UPTIME
        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S %p")
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, DS.PORT).start()
        await self.send_message(chat_id=DS.LOG_CHANNEL, text=TXT.RESTART_TXT.format(temp.B_LINK, today, time))
        for id in DS.ADMIN:
            try:
                await self.send_message(id, f"**__{me.first_name} Started.....✨️__**")
            except:
                pass
        
    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped 🙄")

if __name__ == "__main__":
    DS_AutoCaptionBot().run()
