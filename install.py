import os
import shutil
token= input("введи токен телеграм бота: ")
os.system("git clone https://github.com/Ulbwaa/YandexImagesParser")
os.system("cd YandexImagesParser")
os.system("pip install -r requirements.txt")
os.system("cd ..")

shutil.copy('YandexImagesParser/ImageParser.py', 'ImageParser.py')
shutil.rmtree('YandexImagesParser')

os.system("pip install -r requirements.txt")

my_file = open('.env', 'w')
 
text_for_file = f"TOKEN = '{token}'"
my_file.write(text_for_file)
 
my_file.close()


my_file = open('settings.py', 'w')
 
text_for_file = "from dotenv import load_dotenv"
my_file.write(text_for_file)
my_file.write("load_dotenv()")
 
my_file.close()


