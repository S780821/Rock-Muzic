from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def choose_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵 Play Music",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🎥 Play Video",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
      [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/ROCKERZ_UPDATES"
                ),
                InlineKeyboardButton(
                    text=" ɢʀᴏᴜᴘ", url=f"https://t.me/ROCKERZ_SUPPORT"
             ),
          ],
        [
            InlineKeyboardButton(
                text="🗑 Close Search",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def livestream_markup(quality, videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎥  Start Live",
                callback_data=f"LiveStream {quality}|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 Close",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def stream_quality_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="📽 360P",
                callback_data=f"VideoStream 360|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 720P",
                callback_data=f"VideoStream 720|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 480P",
                callback_data=f"VideoStream 480|{videoid}|{duration}|{user_id}",
            ),
        ],
      [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/ROCKERZ_UPDATES"
                ),
                InlineKeyboardButton(
                    text=" ɢʀᴏᴜᴘ", url=f"https://t.me/ROCKERZ_SUPPORT"
             ),
         ],
       [
            InlineKeyboardButton(
                text="🗑 Close Search",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
