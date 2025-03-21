# Python модули
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import asyncio
import json


# Локальные модули
from logger import logger
from config import BOT_TOKEN, JSON_FILE


# Переменные
bot = Bot(token=BOT_TOKEN)
scheduler = AsyncIOScheduler()


# Загрузка каналов из файла
def load_channels():
	with open(JSON_FILE, 'r', encoding='utf-8') as f:
		return json.load(f)


# Отправка сообщения в канал
async def send_message(channel_id, message):
	try:
		await bot.send_message(
			chat_id=channel_id,
			text=message
		)

		logger.info(f'CHANNEL={channel_id}, MESSAGE="send"')
	except Exception as e:
		logger.error(f'CHANNEL={channel_id}, MESSAGE="{e}"')


# Установка задач для отправки сообщений
def schedule_tasks(channels):
	for channel_id, data in channels.items():
		hour = int(data['hour'])
		minute = int(data['minute'])

		scheduler.add_job(
			send_message,
			'cron',
			hour=hour,
			minute=minute,
			args=(channel_id, data['message'])
		)


# Главная функция
async def main():
	channels = load_channels()

	schedule_tasks(channels=channels)

	scheduler.start()

	logger.info('USER=BOT, MESSAGE="Started"')

	try:
		await asyncio.Event().wait()
	except:
		scheduler.shutdown()
		logger.info('USER=BOT, MESSAGE="Finished"')


# Запуск
if __name__ == '__main__':
	asyncio.run(main())
