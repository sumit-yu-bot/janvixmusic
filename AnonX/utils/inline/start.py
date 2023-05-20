from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="● ᴀᴅᴅ ᴍᴇ ᴍᴏɪ ʙᴀʙʏ ●",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="● ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ●",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="● sᴇᴛᴛɪɴɢs ●", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴍᴏɪ ʙᴀʙʏ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="settings_back_helper"
            ),
      
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="ᴍʏ ᴏᴡɴᴇʀ", user_id=OWNER
            )
           ],
        [
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            ),
        ],
          [
            InlineKeyboardButton(
                text="ᴀʙᴏᴜᴛ", url=f"https://graph.org/%F0%9D%95%8C%F0%9D%95%84%F0%9D%95%80%F0%93%86%A9%F0%93%86%AA-05-19",
            ),
            InlineKeyboardButton(
               text="ꜱᴏᴜʀᴄᴇ", url=config.SUPPORT_CHANNEL
            ),
        ],
     ]
    return buttons
