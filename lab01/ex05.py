from typing import List


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    def __repr__(self) -> str:
        return f"Person('{self.__name}', {self.__age})"

    def __str__(self) -> str:
        return f"{self.__name} ({self.__age})"

    def __gt__(self, other) -> bool:
        return self.__age > other.age


class FamilyTree:
    def __init__(self, root: Person) -> None:
        self.__root = root
        self.__children = list()

    @property
    def root(self) -> Person:
        return self.__root

    @property
    def children(self) -> List['FamilyTree']:
        return self.__children

    def __str__(self) -> str:
        def children_indentation(tree: 'FamilyTree', level: int) -> str:
            result = f"{'    ' * level}> {tree.root}\n"

            for child in tree.children:
                result += children_indentation(child, level + 1)

            return result

        return children_indentation(self, 0)

    def count_descendants(self) -> int:
        result = 0
        if len(self.__children) != 0:
            for child in self.__children:
                result += 1
                result += child.count_descendants()

        return result

    def add_child_tree(self, child: 'FamilyTree') -> None:
        self.__children.append(child)


# tests

# Create dummies of class Person
john = Person("John", 50)
emily = Person("Emily", 30)
jake = Person("Jake", 18)
dan = Person("Dan", 3)
fiona = Person("Fiona", 7)

# Create family trees for each person
john_familiy_tree = FamilyTree(john)
emily_familiy_tree = FamilyTree(emily)
jake_familiy_tree = FamilyTree(jake)
dan_familiy_tree = FamilyTree(dan)
fiona_familiy_tree = FamilyTree(fiona)

# ---- Testing add_child_tree functionality ----

# Add children to John
john_familiy_tree.add_child_tree(jake_familiy_tree)
john_familiy_tree.add_child_tree(emily_familiy_tree)

# Add children to Emily
emily_familiy_tree.add_child_tree(dan_familiy_tree)
emily_familiy_tree.add_child_tree(fiona_familiy_tree)

assert john_familiy_tree.children[1] == emily_familiy_tree
assert john_familiy_tree.children[0] == jake_familiy_tree
assert emily_familiy_tree.children[0] == dan_familiy_tree
assert emily_familiy_tree.children[1] == fiona_familiy_tree

# ---- Testing __init__ functionality ----

assert john.name == "John"
assert john.age == 50


assert jake.name == "Jake"
assert jake.age == 18


assert john_familiy_tree.root == john
assert len(john_familiy_tree.children) == 2

assert jake_familiy_tree.root == jake
assert len(jake_familiy_tree.children) == 0

assert emily_familiy_tree.root == emily
assert dan_familiy_tree.root == dan
assert fiona_familiy_tree.root == fiona


# ---- Testing __str__functionality ----
expected_repr = "> John (50)\n    > Jake (18)\n    > Emily (30)\n        > Dan (3)\n        > Fiona (7)\n"
assert str(john_familiy_tree) == expected_repr

# # ---- Testing __gt__functionality ----
assert john > emily
assert john > jake
assert emily > jake
assert jake > dan

# # ---- Testing __gt__functionality ----
assert john_familiy_tree.count_descendants() == 4
assert jake_familiy_tree.count_descendants() == 0
assert emily_familiy_tree.count_descendants() == 2