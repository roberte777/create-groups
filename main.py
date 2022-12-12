"""main"""
from classroom import Class, Person


def main():
    """create groups and execute"""
    people = [
        Person("A", ["B", "C"]),
        Person("B", ["A", "C"]),
        Person("C", ["A", "B"]),
        Person("D", ["A", "B"]),
        Person("E", ["F", "G"]),
        Person("F", ["E", "G"]),
        Person("G", ["E", "F"]),
        Person("H", ["E", "F"]),
        Person("I", ["J", "K"]),
        Person("J", ["I", "K"]),
        Person("K", ["I", "J"]),
        Person("L", ["I", "J"]),
    ]
    grps = Class(people).create_groups(4)
    for grp in grps:
        print(grp)


if __name__ == "__main__":
    main()
