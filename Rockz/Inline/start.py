from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Rockz import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Aᴜᴅɪᴏ Qᴜᴀʟɪᴛʏ.", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Aᴜᴅɪᴏ Vᴏʟᴜᴍᴇ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Aᴜᴛʜᴏʀɪᴢᴇᴅ Usᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Cʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ 🗂", callback_data="Salim"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME} Pᴏᴡᴇʀᴇᴅ Bʏ [「™ʟᴏɢ✓ᴏᴜᴛ❥︎✔︎」](t.me/Blaze_Support)**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ 🗂", callback_data="Salim"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Support", url=f"https://t.me/Blaze_Support"
                ),
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ 🗂", callback_data="Salim"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Updates 📨", url=f"https://t.me/The_Blaze_Network"
                ),
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ 🗂", callback_data="Salim"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Support", url=f"https://t.me/UNIQUE_SOCIETY"
                ),
                InlineKeyboardButton(
                    text="Updates 📨", url=f"https://t.me/THE_BLAZE_NETWORK"
                ),
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ 🗂", callback_data="Salim"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ Gʀᴏᴜᴘ ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **Tʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ 🗂", callback_data="Salim"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ Gʀᴏᴜᴘ ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Support", url=f"https://t.me/UNIQUE_SOCIETY"
                ),
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ 🗂", callback_data="Salim"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ Gʀᴏᴜᴘ ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="Updates 📨", url=f"https://t.me/Blaze_Support"
                ),
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘᴇʀ Cᴏᴍᴍᴀɴᴅs Mᴇɴᴜ 🗂", callback_data="Salim"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ Gʀᴏᴜᴘ ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Support", url=f"https://t.me/UNIQUE_SOCIETY"
                ),
                InlineKeyboardButton(
                    text="Updates 📨", url=f"https://t.me/BLAZE_support"
                ),
            ],
        ]
        return f"🎛  **ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 ᴀᴜᴅɪᴏ ϙᴜᴀʟɪᴛʏ", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 ᴀᴜᴅɪᴏ ᴠᴏʟ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 ᴅᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ ᴄʟᴏsᴇ", callback_data="close"),
            InlineKeyboardButton(text="🔙 ɢᴏ ʙᴀᴄᴋ", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 ʀᴇsᴇᴛ ᴀᴜᴅɪᴏ ᴠᴏʟᴜᴍᴇ 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 ʟᴏᴡ ᴠᴏʟ", callback_data="LV"),
            InlineKeyboardButton(text="🔉 ᴍᴇᴅɪᴜᴍ ᴠᴏʟ", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 ʜɪɢʜ ᴠᴏʟ", callback_data="HV"),
            InlineKeyboardButton(text="🔈 ᴀᴍᴘʟɪғɪᴇᴅ ᴠᴏʟ", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 ᴄᴜsᴛᴏᴍ ᴠᴏʟ 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 ɢᴏ ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼ᴄᴜsᴛᴏᴍ ᴠᴏʟᴜᴍᴇ🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 ᴇᴠᴇʀʏᴏɴᴇ", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 ᴀᴅᴍɪɴs", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛs", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 ɢᴏ ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ ᴜᴘᴛɪᴍᴇ", callback_data="UPT"),
            InlineKeyboardButton(text="💾 ʀᴀᴍ", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 ᴄᴘᴜ", callback_data="CPT"),
            InlineKeyboardButton(text="💽 ᴅɪsᴋ", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 ɢᴏ ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} sᴇᴛᴛɪɴɢs**", buttons
