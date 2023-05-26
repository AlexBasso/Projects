import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import SiteSettings
from handlers.default_handlers import start_handler, basic_functions_handler, help_handler, history, hello_world, hello

tg_settings = SiteSettings()


async def bot_main():
    """
    Async function that runs tg_api part of code. Creates "bot" aiogram Bot object, that gets token via env and set
    parse mode as HTML. Creates "dp" aiogram Dispatcher object, that uses MemoryStorage( Default FSM storage) - all
    data will be lost if bot is reset. Dispatcher object takes all tg_api handlers from aiogram Router object. Bot
    object will not be handling telegram user messages(events) that where made before main() was running and will not
    proceed forward until all pending updates will be dropped. Bot will start pooling for new updates and will
    resolve already registered messages.
    """

    bot = Bot(token=tg_settings.bot_api.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(start_handler.router, basic_functions_handler.router, history.router, help_handler.router,
                       hello_world.router, hello.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, polling_timeout=15, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    print('load is running!')
    asyncio.run(bot_main())
