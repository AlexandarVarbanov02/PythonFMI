INVALID_FORMAT_MSG = "Невалиден формат"
INVALID_LETTERS_MSG = "Невалидни букви"
INVALID_CODE_MSG = "Невалиден регионален код"

ALLOWED_LETTERS = set("АВЕКМНОРСТУХ")

REGION_CODES = {
    "Е": "Благоевград",
    "А": "Бургас",
    "В": "Варна",
    "ВТ": "Велико Търново",
    "ВН": "Видин",
    "ВР": "Враца",
    "ЕВ": "Габрово",
    "ТХ": "Добрич",
    "К": "Кърджали",
    "КН": "Кюстендил",
    "ОВ": "Ловеч",
    "М": "Монтана",
    "РА": "Пазарджик",
    "РК": "Перник",
    "ЕН": "Плевен",
    "РВ": "Пловдив",
    "РР": "Разград",
    "Р": "Русе",
    "СС": "Силистра",
    "СН": "Сливен",
    "СМ": "Смолян",
    "СО": "София (област)",
    "С": "София (столица)",
    "СА": "София (столица)",
    "СВ": "София (столица)",
    "СТ": "Стара Загора",
    "Т": "Търговище",
    "Х": "Хасково",
    "Н": "Шумен",
    "У": "Ямбол",
}


def is_valid(license_plate: str):
    # Allowed formats "XX0000XX" or "X0000XX"
    # using slicing split into 3 substrings and check their validity?

    license_plate = license_plate.upper()
    tail, numbers, region = license_plate[-2:], license_plate[-6:-2], license_plate[0:-6]

    if not tail.isalpha() or not region.isalpha() or not numbers.isdigit():
        return False, INVALID_FORMAT_MSG

    if not set(tail).issubset(ALLOWED_LETTERS) or not set(region).issubset(ALLOWED_LETTERS):
        return False, INVALID_LETTERS_MSG

    if region in REGION_CODES.keys():
        return True, REGION_CODES[region]
    else:
        return False, INVALID_CODE_MSG


assert is_valid("СА1234АВ") == (True, "София (столица)")
assert is_valid("С1234АВ") == (True, "София (столица)")
assert is_valid("ТХ0000ТХ") == (True, "Добрич")
assert is_valid("ТХ000ТХ") == (False, INVALID_FORMAT_MSG)
assert is_valid("ТХ0000Т") == (False, INVALID_FORMAT_MSG)
assert is_valid("ТХ0000ТХХ") == (False, INVALID_FORMAT_MSG)
assert is_valid("У8888СТ") == (True, "Ямбол")
assert is_valid("Y8888CT") == (False, INVALID_LETTERS_MSG)
assert is_valid("ПЛ7777АА") == (False, INVALID_LETTERS_MSG)
assert is_valid("РВ7777БВ") == (False, INVALID_LETTERS_MSG)
assert is_valid("ВВ6666КН") == (False, INVALID_CODE_MSG)
