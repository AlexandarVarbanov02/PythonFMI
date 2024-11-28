import os.path


class InvalidLineError(ValueError):
    def __init__(self, line_content: str, expected_format: str=None) -> None:
        msg = f"Invalid line format: {line_content}\nExpected format: {expected_format}."
        super().__init__(msg)


class InvalidItemError(ValueError):
    def __init__(self, item_name: str) -> None:
        msg = f"Invalid item name: {item_name}."
        super().__init__(msg)


class InvalidQuantityError(ValueError):
    def __init__(self, quantity: int, item_name: str) -> None:
        msg = f"Item {item_name} has an invalid quantity of {quantity}."
        super().__init__(msg)


class InvalidPriceError(ValueError):
    def __init__(self, price: float, item_name: str) -> None:
        msg = f"Item {item_name} has an invalid price of {price}."
        super().__init__(msg)


class ListFileError(IOError):
    def __init__(self, path: str) -> None:
        msg = f"Failed to open shopping list file at '{path}'."
        super().__init__(msg)


def validate_path(path: str) -> list[str]:
    if not os.path.exists(path):
        raise ListFileError(path)

    try:
        with open(path, 'r', encoding="utf-8") as file:
            return file.readlines()
    except Exception:
        raise ListFileError(path)


def parse_line(line: str) -> list[str]:
    if line[0] != '-':
        raise InvalidLineError(line, "-'name of item':'quantity':'price'")

    parts = line[1:].split(':')
    if len(parts) != 3:
        raise InvalidLineError(line, "-'name of item':'quantity':'price'")

    return parts


def validate_list(path: str) -> int:
    shopping_list = validate_path(path)
    total_amount = 0
    for line in shopping_list:
        name, quantity, price = parse_line(line)

        if len(name) == 0 or name.isdigit():
            raise InvalidItemError(name)

        if quantity.isdecimal():
            quantity = int(quantity)
        else:
            raise InvalidQuantityError(quantity, name)

        try:
            price = float(price)
            if price < 0:
                raise InvalidPriceError(price, name)
        except ValueError:
            raise InvalidPriceError(price, name)

        total_amount += price * quantity

    return total_amount


assert abs(validate_list(os.path.join("task_1", "list1.txt")) - 11.25) < 0.001

assert int(validate_list(os.path.join("task_1", "list2.txt"))) == 0, "Empty files should return 0"

try:
    validate_list(os.path.join("task_1", "list3.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("task_1", "list4.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("task_1", "list5.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidItemError:
    pass

try:
    validate_list(os.path.join("task_1", "list6.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("task_1", "list7.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("task_1", "list8.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("task_1", "list9.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("task_1", "list10.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("task_1", "list11.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

print("✅ All OK! +1 point")
