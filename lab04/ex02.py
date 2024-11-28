import os
from itertools import tee, chain


class Laika:
    def __init__(self, path: str, caesar_key: int) -> None:
        self.__ceaser_key = caesar_key
        self.__path = path

    @staticmethod
    def encode(string: str, n: int) -> list[str]:
        laika_string = string[::2] + string[1::2][::-1]
        return [laika_string[i:i+n] for i in range(0, len(laika_string), n)]

    @staticmethod
    def decode(laika_list: list[str]) -> str:
        laika_string = ''.join(laika_list)
        return ''.join(''.join(pair) for pair in zip(laika_string[::1], laika_string[::-1]))[:len(laika_string)]

    @staticmethod
    def ceaser_encode(string: str, ceaser_key: int) -> str:
        return ''.join([chr((ord(c) + ceaser_key)) for c in string])

    def save_to(self, file_name: str, data: str) -> None:
        with open(os.path.join(self.__path, file_name), 'w') as file:
            file.write(data)

    def encode_to_files(self, string: str, n: int) -> str:
        files = dict(map(lambda x: (self.ceaser_encode(x, self.__ceaser_key), x), self.encode(string, n)[::-1]))
        last_name = ""
        for name, data in files.items():
            self.save_to(name, last_name + '\n' + data if last_name != "" else '\n' + data)
            last_name = name
        return last_name

    def decode_from_files(self, file_name: str) -> str:
        current_file = os.path.join(self.__path, file_name)
        result = list()

        while True:
            if current_file == os.path.join(self.__path, ""):
                break
            if os.path.exists(current_file):
                with open(current_file, "r") as file:
                    data = file.readlines()
                    if len(data) == 1:
                        result.append(data[0].strip())
                        current_file = ""
                    elif len(data) > 2:
                        result.extend(data)
                    else:
                        result.append(data[1].strip())
                    current_file = os.path.join(self.__path, data[0].strip())
                    print(current_file)
            else:
                raise FileNotFoundError

        return self.decode(result)


# Tests

# Preconditions
import os

root_dir = "task_2"
os.makedirs(root_dir)

l = Laika(root_dir, 3)

# encode
assert l.encode("abcdefg", 2) == ["ac", "eg", "fd", "b"]
assert l.encode("abcdefg", 3) == ["ace", "gfd", "b"]
assert l.encode("abcdefg", 5) == ["acegf", "db"]
assert l.encode("abcdefghijkl", 1) == ["a", "c", "e", "g", "i", "k", "l", "j", "h", "f", "d", "b"]
assert l.encode("abcdefghijkl", 2) == ["ac", "eg", "ik", "lj", "hf", "db"]
assert l.encode("abcdefghijkl", 3) == ["ace", "gik", "ljh", "fdb"]
assert l.encode("abcdefghijkl", 4) == ["aceg", "iklj", "hfdb"]
assert l.encode("abcdefghijkl", 4) == ["aceg", "iklj", "hfdb"]
assert l.encode("abcdefghijkl", 12) == ["acegikljhfdb"]
assert l.encode("abcdefghijkl", 24) == ["acegikljhfdb"]


# decode
assert l.decode(["ac", "eg", "fd", "b"]) == "abcdefg"
assert l.decode(l.encode("abcdefg", 3)) == "abcdefg"
assert l.decode(l.encode("abcdefg", 5)) == "abcdefg"
assert l.decode(l.encode("abcdefghijkl", 1)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 2)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 3)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 4)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 4)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 12)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 24)) == "abcdefghijkl"


# encode_to_files
l1 = Laika(root_dir, 4)
assert l1.encode_to_files("abcdefghijkl", 3) == "egi"

assert sorted(os.listdir(root_dir)) == ["egi", "jhf", "kmo", "pnl"]

with open(os.path.join(root_dir, "egi")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "kmo"
assert content == "ace"

with open(os.path.join(root_dir, "jhf")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

print(next_file)
assert next_file == ""
assert content == "fdb"

with open(os.path.join(root_dir, "kmo")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "pnl"
assert content == "gik"

with open(os.path.join(root_dir, "pnl")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "jhf"
assert content == "ljh"


# decode_from_files
print(l1.decode_from_files("egi"))
assert l1.decode_from_files("egi") == "abcdefghijkl"

# Exception

try:
    l1.encode_to_files("abcdefghijkl", 3)
except FileExistsError:
    assert True
except Exception:
    assert False


try:
    l1.decode_from_files("non-existing-file")
except FileNotFoundError:
    assert True
except Exception:
    assert False

print("✅ All OK! +2 points")