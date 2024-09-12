from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup as Markup
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
import json


with open('DGYar.json', 'r', encoding='utf-8') as file:
    bot_data = json.load(file)

bot = Client('aksify',api_id=863373,api_hash='c9f8495ddd20615835d3fd073233a3f6')

def markup_creator(buttons):
    rows = []

    for data, text in buttons.items(): 
        rows.append([InlineKeyboardButton (text, callback_data=data)])

    markup = InlineKeyboardMarkup(rows)
    return markup

@bot.on_message(filters.command('test') & filters.private)
async def up(client, message):
    await message.reply('im upppp')

@bot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    chat_id = message.chat.id
    msg = bot_data['welcome_new_user']['msg']
    btn = bot_data['welcome_new_user']['btn']
    markup = markup_creator(btn)

    await client.send_message(chat_id, msg, reply_markup = markup)

@bot.on_message(filters.command('menu') & filters.private)
async def menu(client, message):
    chat_id = message.chat.id
    msg = bot_data['authenticated']['msg']
    btn = bot_data['authenticated']['btn']
    markup = markup_creator(btn)

    await client.send_message(chat_id, msg, reply_markup = markup)


@bot.on_callback_query()
async def callbacks(client, callback_query):
    message = callback_query.message
    data = callback_query.data
    chat_id = callback_query.from_user.id

    await message.delete()

    if(data == 'connect_to_digikala'):
        msg = bot_data['authenticate_to_digikala']['msg']
        fields = bot_data['authenticate_to_digikala']['fields']

        #TODO:generate the Auth Link

        if fields:
            msg = msg.format(auth_link="Auth Link")
    
        await message.reply(msg)



bot.run()