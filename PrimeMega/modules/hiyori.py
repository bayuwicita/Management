import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message
from random import choice


SEPI = [
 "nggak sepi kok kan masih ada aku :v",
 "ngga sepi sayang, kan ada Tohru disini ..",
 "sepi kayak hati aku :v",
]
AYANG = [
 "iya ayang kenapa?",
 "kenapa ayang ?? manggil manggil ??",
 "kenapa ayang? kangen?",
]



@Client.on_message(filters.command(["sepi"], prefixes=""))
async def sepi(client, message):
        await message.reply(choice(SEPI))

    
@Client.on_message(filters.command(["ohayou", "ohayo", "ohayou minna", "pagi"], prefixes=""))
async def ohayou(client, message):
        await message.reply(
          f"Ohayou Gozaimasu {message.from_user.mention()}"
        )

    
@Client.on_message(filters.command(["konbanwa"], prefixes=""))
async def konbanwa(client, message):
        await message.reply(
          f"Konbanwa {message.from_user.mention()}"
        )

    
@Client.on_message(filters.command(["konnichiwa"], prefixes=""))
async def konnichiwa(client, message):
        await message.reply(
          f"Ohayou Gozaimasu {message.from_user.mention()}"
        )
  
@Client.on_message(filters.command(["ayang"], prefixes=""))
async def ayang(client, message):
        await message.reply(choice(AYANG))
