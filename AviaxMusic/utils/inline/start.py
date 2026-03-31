import config
from AviaxMusic import app


def start_panel(_):
    buttons = [
        [
            {
                "text": _["S_B_1"],
                "url": f"https://t.me/{app.username}?startgroup=true",
            },
            {
                "text": _["S_B_2"],
                "url": config.SUPPORT_GROUP,
            },
        ],
    ]
    return {"inline_keyboard": buttons}


def private_panel(_):
    buttons = [
        [
            {
                "text": _["S_B_3"],
                "url": f"https://t.me/{app.username}?startgroup=true",
            }
        ],
        [
            {
                "text": _["S_B_4"],
                "callback_data": "settings_back_helper",
            }
        ],
        [
            {
                "text": "𝖠𝖯𝖨 𝖢𝗈𝗇𝗌𝗈𝗅𝖾",
                "callback_data": "api_console",
                "style": "danger",   # ✅ WORKING
            }
        ],
        [
            {
                "text": _["S_B_5"],
                "url": f"tg://user?id={config.OWNER_ID}",  # FIXED
            },
            {
                "text": _["S_B_2"],
                "url": config.SUPPORT_GROUP,
            },
        ],
        [
            {
                "text": _["S_B_6"],
                "url": config.SUPPORT_CHANNEL,
            },
            {
                "text": _["S_B_7"],
                "url": config.UPSTREAM_REPO,
            },
        ],
    ]
    return {"inline_keyboard": buttons}
