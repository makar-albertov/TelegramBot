import asyncio
from aiogram import Bot
from config_data.config import load_config, Config
from create_dp import dp


async def main() -> None:
    config: Config = load_config()

    bot: Bot = Bot(token=config.tgbot.token)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
