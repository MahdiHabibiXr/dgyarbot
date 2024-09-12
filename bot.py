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

@bot.on_message(filters.private)
async def messages(client, message):
    chat_id = message.chat.id
    command = message.text

    if(command == '/start'):
        msg = bot_data['welcome_new_user']['msg']
        btn = bot_data['welcome_new_user']['btn']
        markup = markup_creator(btn)

        await client.send_message(chat_id, msg, reply_markup = markup)

    elif(command == '/menu'):
        chat_id = message.chat.id
        msg = bot_data['authenticated']['msg']
        btn = bot_data['authenticated']['btn']
        markup = markup_creator(btn)

        await client.send_message(chat_id, msg, reply_markup = markup)

    elif(command.startswith('https://')):
        chat_id = message.chat.id
        msg = bot_data['sent_url']['msg']
        btn = bot_data['sent_url']['btn']
        fields = bot_data['authenticate_to_digikala']['fields']
        markup = markup_creator(btn)

        if fields:
                msg = msg.format(sheet_link = "SHEET LINK") #TODO: The sheet url should be used here

        await client.send_message(chat_id, msg, reply_markup = markup)


    else :
        #TODO: message should be sent to chatbot
        gpt_repsonse = 'CHATBOT RESPONSE'
        await message.reply(gpt_repsonse)

# @bot.on_message(filters.command('menu') & filters.private)
# async def menu(client, message):
#     chat_id = message.chat.id
#     msg = bot_data['authenticated']['msg']
#     btn = bot_data['authenticated']['btn']
#     markup = markup_creator(btn)

#     await client.send_message(chat_id, msg, reply_markup = markup)

# @bot.on_message(filters.regex('https://') & filters.private)
# async def url(client, message):
#     chat_id = message.chat.id
#     msg = bot_data['sent_url']['msg']
#     btn = bot_data['sent_url']['btn']
#     fields = bot_data['authenticate_to_digikala']['fields']
#     markup = markup_creator(btn)

#     if fields:
#             msg = msg.format(sheet_link = "SHEET LINK") #TODO: The sheet url should be used here

#     await client.send_message(chat_id, msg, reply_markup = markup)

@bot.on_message(filters.private & filters.photo)
async def image(client, message):
    img_id = message.photo.file_id
    chat_id = message.chat.id
    msg = bot_data['edit_image']['msg']
    btn = bot_data['edit_image']['btn']
    fields = bot_data['edit_image']['fields']
    markup = markup_creator(btn)

    if fields:
        msg = msg.format(sheet_link="SHEET LINK") #The sheet link should be placed here

    file = await client.download_media(img_id, file_name = f'photos/{chat_id}.jpg')

    #TODO: the image should be processed here
    processed = file

    await client.send_photo(chat_id, img_id, reply_markup = markup, caption = msg)

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

    elif(data == 'add_product'):
        msg = bot_data['add_product']['msg']
        
        await message.reply(msg)

    elif(data == 'confirm'):
        msg = bot_data['confirm']['msg']
        btn = bot_data['confirm']['btn']
        markup = markup_creator(btn)

        await client.send_message(chat_id, msg, reply_markup = markup)
    
    elif(data == 'return_to_menu'):
        msg = bot_data['return_to_menu']['msg']
        btn = bot_data['return_to_menu']['btn']
        markup = markup_creator(btn)

        await client.send_message(chat_id, msg, reply_markup = markup)

        
    elif(data == 'help'):
        msg = bot_data['help']['msg']
        btn = bot_data['help']['btn']
        markup = markup_creator(btn)

        await client.send_message(chat_id, msg, reply_markup = markup)

bot.run()