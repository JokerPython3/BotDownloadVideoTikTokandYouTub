from telebot.types import InlineKeyboardMarkup as mk
from telebot.types import InlineKeyboardButton as btn

import telebot
from Downloader.download import Downloads
import os
Java = telebot.TeleBot(input("enter token :"))
print("Bot is running send /start to bot")
@Java.message_handler(commands=["start"])
def start(message):
    b1 = btn(text="Channel",url="https://t.me/python3_Tool")
    m1 = mk(row_width=1).add(b1)
    Java.reply_to(message,text="<strong> send url or link video in youtub or tiktoks to downloads </strong>",parse_mode="html",reply_markup=m1)
@Java.message_handler(func=lambda message:True)
def down(message):
    link = message.text
    info=Downloads(link).ksj()
    size = info["filesize"]
    name = info["title"];path=info["s"]
    b1 = btn(text="Channel",url="https://t.me/python3_Tool")
    m1 = mk(row_width=1).add(b1)
    with open(path,"rb") as video:
        Java.send_video(message.chat.id,video=video,caption="<strong>name : {} |size : {} | ~ @python3_Tool ~ </strong>".format(name,size),parse_mode="html",reply_markup=m1)
    os.remove(path)
Java.polling(True)
#Ilove Java