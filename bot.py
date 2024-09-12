from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup as Markup
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
import json

bot = Client('aksify',api_id=863373,api_hash='c9f8495ddd20615835d3fd073233a3f6')

@bot.on_message(filters.command('test') & filters.private)
async def start_text(client, message):
    await message.reply('im upppp')


bot.run()
