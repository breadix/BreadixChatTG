import asyncio

from aiogram import Bot, Dispatcher
import logging

from breadixchattg.pyrogram_tools.client import client
from breadixchattg.core.config import settings
from breadixchattg.handlers import main_router


bot = Bot(token=settings.tg_api_keys.bot_api_key)

dp = Dispatcher()

dp.include_router(main_router)

async def main():
    if settings.mode == 'debug':
        logging.basicConfig(level=logging.DEBUG)

        pyro_logger = logging.getLogger('pyrogram')
        pyro_logger.setLevel(logging.WARNING)

    await client.start()
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())