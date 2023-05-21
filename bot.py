import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config 
from create_dp import dp
from handlers import user_handlers, other_handlers


async def main(dp: Dispatcher) -> None:
    config: Config = load_config()
    bot: Bot = Bot(token=config.tgbot.token)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main(dp))
