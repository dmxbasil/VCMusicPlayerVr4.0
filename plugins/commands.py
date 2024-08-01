from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nIam MusicPlayer 2.0 which plays music in Channels and Groups 24*7\n\nI can even Stream Youtube Live in Your Voicechat\n\nDeploy Your Own bot from source code below\n\nHit /help to know about available commands.</b>"
HELP = """
<b>Add the bot and User account in your Group with admin rights.
Start a VoiceChat
Use /play <song name> or use /play as a reply to an audio file or youtube link.
You can also use /dplay <song name> to play a song from Deezer.</b>
**Common Commands**:
**/play**  Reply to an audio file or YouTube link to play it or use /play <song name>.
**/dplay** Play music from Deezer, Use /dplay <song name>
**/player**  Show current playing song.
**/help** Show help for commands
**/playlist** Shows the playlist.
**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2
**/join**  Join voice chat.
**/leave**  Leave current voice chat
**/vc**  Check which VC is joined.
**/stop**  Stop playing.
**/radio** Start Radio.
**/stopradio** Stops Radio Stream.
**/replay**  Play from the beginning.
**/clean** Remove unused RAW PCM files.
**/pause** Pause playing.
**/resume** Resume playing.
**/mute**  Mute in VC.
**/unmute**  Unmute in VC.
**/restart** Restarts the Bot.
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/dmx_chating'),
        InlineKeyboardButton('🤖 Support Group', url='https://t.me/Yeageristbots'),
    ],
    [
        InlineKeyboardButton('👨🏼‍💻 Developer', url='https://t.me/Yeageristbotsdev'),
        InlineKeyboardButton('🧩 Source', url='https://github.com/Yeagerist-Music-Streamer-Bot-V3/VCMusicPlayerVr4.0'),
    ],
    [
        InlineKeyboardButton('👨🏼‍🦯 Help', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/Animemusicarchive6'),
            InlineKeyboardButton('🤖 Support Group', url='https://t.me/Yeageristbots'),
        ],
        [
            InlineKeyboardButton('👨🏼‍💻 Developer', url='https://t.me/Yeageristbotsdev'),
            InlineKeyboardButton('🧩 Source', url='https://github.com/Yeagerist-Music-Streamer-Bot-V3/VCMusicPlayerVr4.0'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
