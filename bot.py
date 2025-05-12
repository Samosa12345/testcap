# (c) @Bisal & (c) @Sanchit0102

# ===================== [ importing Requirements ] ===================== #

from config import DS
from aiohttp import web
from pyrogram import Client
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
        self.uptime = DS.BOT_UPTIME
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, DS.PORT).start()
        print(f"{me.first_name} Is Started !.....✨️")
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
