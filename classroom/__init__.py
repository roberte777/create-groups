class Person:
    def __init__(self, name: str, do_not_pair_with: list):
        self.name = name
        self.do_not_pair_with = do_not_pair_with

    def __str__(self):
        return self.name


class Group:
    def __init__(self, people: list):
        self.people = people

    def __str__(self):
        return str(self.people)


class Class:
    def __init__(self, people: list):
        self.people = people

    def __str__(self):
        return str(self.people)

    def create_groups(self, group_size: int):
        # sort
        for person in self.people:
            for other_person in self.people:
                if person.name in other_person.do_not_pair_with:
                    person.do_not_pair_with.append(other_person)

        # sort people by number of do_not_pair_with
        self.people.sort(key=lambda person: len(person.do_not_pair_with), reverse=True)

        # color the vertices
        colors = {}
        colors_count = {}
        for person in self.people:
            # get an array of colors that are already used by the neighbors
            used_colors = []
            for neighbor in person.do_not_pair_with:
                if neighbor in colors:
                    used_colors.append(colors[neighbor])
            # find the first color that is not used by the neighbors that is less than num_groups
            color = 0
            while color in used_colors or colors_count.get(color, 0) >= group_size:
                color += 1
            colors[person.name] = color
            if color in colors_count:
                colors_count[color] += 1
            else:
                colors_count[color] = 1

        # create groups
        groups = []
        for color in range(max(colors.values()) + 1):
            group = []
            for person, curr_color in colors.items():
                if curr_color == color:
                    group.append(person)
            groups.append(Group(group))
        print(colors, colors_count)
        return groups
