from ImageParser import YandexImage
import requests
import settings
import os
from art import tprint
import os.path
import logging
import shutil
from aiogram import Bot, Dispatcher, executor, types
tprint("img",font="tarty1")
tprint("parser",font="tarty1")
tprint("bot",font="tarty1")

token = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)
sea = 'car'
parser = YandexImage()



bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.reply("Привет!\nЯ бот для получения изображений по поисковому запросу")
	
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply("Скрипт запущен\nОжидайте...")
    global sea
    sea = message.text
    forimg()
    media = types.MediaGroup()
    for i in range(1, 31):
    	if os.path.isfile(sea+'/'+str(i)+'.jpg') and int(os.path.getsize(sea+'/'+str(i)+'.jpg')) > 100000:
    		photo = types.InputFile(sea+'/'+str(i)+'.jpg')
    		await bot.send_photo(chat_id=message.chat.id, photo=photo)
    shutil.rmtree(sea)
    
    
	


 

def img_down(url='', name=''):
		try:
			response = requests.get(url=url) 
			with open(sea+'/'+name+'.jpg' ,  'wb') as file:
				file.write(response.content)
			return sea+'/'+name+'.jpg'
		except Exception as _ex:
			return 'Не получилось скачать'
			

def forimg():
    count = 1
    os.mkdir(sea)
    for item in parser.search(sea):
    	print(img_down(item.url, str(count)))
    	count += 1
        	
     	
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
