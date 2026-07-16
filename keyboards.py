from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

DONATES = {
    "Bull": 10,
    "Tiger": 20,
    "Rabbit": 30,
    "Cobra": 35,
    "Bunny": 40,
    "Hydra": 45,
    "Dracula": 50,
    "God": 75,
    "Pegas": 99,
    "Helper": 99,
}

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛡 Привилегия на сервере",
                callback_data="donate"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔓 Разбан на сервере",
                callback_data="unban"
            )
        ]
    ]
)


def donate_keyboard():
    keyboard = []

    for name, price in DONATES.items():
        keyboard.append(
            [
                InlineKeyboardButton(
                    text=f"{name} - ⭐{price}",
                    callback_data=f"buy_{name}"
                )
            ]
        )

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
