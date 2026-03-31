from pyrogram.types import InlineKeyboardButton

import config
from AviaxMusic import app


def btn(button, style=None):
    data = button.__dict__.copy()
    data = {k: v for k, v in data.items() if v is not None}

    if style:
        data["style"] = style

    return data


def start_panel(_):
    buttons = [
        [
            btn(InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true"
            )),
            btn(InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_GROUP
            )),
        ],
    ]
    return {"inline_keyboard": buttons}


def private_panel(_):
    buttons = [
        [
            btn(InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ))
        ],
        [
            btn(InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper"
            ))
        ],
        [
            btn(
                InlineKeyboardButton(
                    text="𝖠𝖯𝖨 𝖢𝗈𝗇𝗌𝗈𝗅𝖾",
                    callback_data="api_console"
                ),
                style="danger"   # 🔥 STYLE WORKING
            )
        ],
        [
            btn(InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"tg://user?id={config.OWNER_ID}"
            )),
            btn(InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_GROUP
            )),
        ],
        [
            btn(InlineKeyboardButton(
                text=_["S_B_6"],
                url=config.SUPPORT_CHANNEL
            )),
            btn(InlineKeyboardButton(
                text=_["S_B_7"],
                url=config.UPSTREAM_REPO
            )),
        ],
    ]
    return {"inline_keyboard": buttons}
