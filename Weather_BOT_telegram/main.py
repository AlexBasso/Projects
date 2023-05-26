import asyncio
import logging

from loader import bot_main


if __name__ == '__main__':
    print('Bot started working!')
    logging.basicConfig(level=logging.INFO)
    asyncio.run(bot_main())
