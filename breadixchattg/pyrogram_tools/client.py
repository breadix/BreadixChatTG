from pyrogram import Client

from breadixchattg.core.config import settings

client = Client(
    name='BreadixChatTGApp',
    api_id=settings.tg_app.id,
    api_hash=settings.tg_app.hash,
    bot_token=settings.tg_api_keys.bot_api_key,
    no_updates=True
)
