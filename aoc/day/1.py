# https://adventofcode.com/2022/day/1

from aoc.input import get_input


def calories_of_top_elf(lines: list[str]) -> int:
    most_calories = 0
    item_cals = []
    for line in lines:
        if not line.strip():
            total_cals = sum(item_cals)
            if total_cals > most_calories:
                most_calories = total_cals
            del item_cals
            item_cals = []
            continue
        cals = int(line.strip())
        item_cals.append(cals)
    return most_calories


def calories_of_top_3_elves(lines: list[str]) -> int:
    most_calories = (0, 0, 0)
    n_top = 3
    item_cals = []
    for line in lines:
        if not line.strip():
            total_cals = sum(item_cals)
            for i in range(n_top):
                if total_cals > most_calories[i]:
                    most_calories = most_calories[:i] + (total_cals,) + most_calories[i:-1]
                    break
            del item_cals
            item_cals = []
            continue
        cals = int(line.strip())
        item_cals.append(cals)
    return sum(most_calories)


if __name__ == "__main__":
    input_ = get_input(day=1)
    print(calories_of_top_elf(input_.splitlines()))
    print(calories_of_top_3_elves(input_.splitlines()))