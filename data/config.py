from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN") # токен Telegram бота. Брать токен из @BotFather! После добавления токена, удалите комментарий