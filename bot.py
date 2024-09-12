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
async def start_text(client, message):
    await message.reply('im upppp')

@bot.on_message(filters.command('start') & filters.private)
async def start_text(client, message):
    chat_id = message.chat.id
    msg = bot_data['welcome_new_user']['msg']
    markup = markup_creator(bot_data['welcome_new_user']['btn'])

    await client.send_message(chat_id, reply_markup = markup, caption = msg)


@bot.on_callback_query()
async def callbacks(client, callback_query):
    message = callback_query.message
    data = callback_query.data
    chat_id = callback_query.from_user.id

    await message.delete()

    if(data == 'connect_to_digikala'):
        await callback_query.answer("", show_alert = False)
        await message.reply("✅درخواست شما در صف پردازش قرار گرفت، لطفا کمی شکیبا باشید.")



bot.run()