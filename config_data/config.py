from dataclasses import dataclass
from environs import Env
import os


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tgbot: TgBot


def load_config() -> Config:
    env: Env = Env()
    env.read_env()
    return Config(tgbot=TgBot(token=env.str('BOT_TOKEN'), 
                              admin_ids=list(map(int, env.list('ADMIN_IDS')))))
