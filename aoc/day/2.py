# https://adventofcode.com/2022/day/2

import enum

from aoc.input import get_input


class RPS(enum.Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


throw_worth = {
    RPS.ROCK: 1,
    RPS.PAPER: 2,
    RPS.SCISSORS: 3,
}


def score_strategy_guide(input: list[str]) -> int:
    thems = {
        "A": RPS.ROCK,
        "B": RPS.PAPER,
        "C": RPS.SCISSORS,
    }
    yous = {
        "X": RPS.ROCK,
        "Y": RPS.PAPER,
        "Z": RPS.SCISSORS,
    }
    total_score = 0
    for line in input:
        them, you = line.split()
        total_score += throw_worth[yous[you]]
        if thems[them] == yous[you]:
            # draw
            total_score += 3
        elif thems[them] == RPS.ROCK and yous[you] == RPS.PAPER \
            or thems[them] == RPS.PAPER and yous[you] == RPS.SCISSORS \
            or thems[them] == RPS.SCISSORS and yous[you] == RPS.ROCK:
            # you win
            total_score += 6
        else:
            # you lose
            pass
    return total_score


def score_ldw_guide(input: list[str]) -> int:
    thems = {
        "A": RPS.ROCK,
        "B": RPS.PAPER,
        "C": RPS.SCISSORS,
    }
    yous = {
        "X": RPS.ROCK,
        "Y": RPS.PAPER,
        "Z": RPS.SCISSORS,
    }
    total_score = 0
    for line in input:
        them, outcome = line.split()
        if outcome == "X":
            # lose
            if thems[them] == RPS.ROCK:
                your_throw = RPS.SCISSORS
            elif thems[them] == RPS.PAPER:
                your_throw = RPS.ROCK
            elif thems[them] == RPS.SCISSORS:
                your_throw = RPS.PAPER
        elif outcome == "Y":
            # draw
            your_throw = thems[them]
        elif outcome == "Z":
            # win
            if thems[them] == RPS.ROCK:
                your_throw = RPS.PAPER
            elif thems[them] == RPS.PAPER:
                your_throw = RPS.SCISSORS
            elif thems[them] == RPS.SCISSORS:
                your_throw = RPS.ROCK
        total_score += throw_worth[your_throw]
        if thems[them] == your_throw:
            # draw
            total_score += 3
        elif thems[them] == RPS.ROCK and your_throw == RPS.PAPER \
            or thems[them] == RPS.PAPER and your_throw == RPS.SCISSORS \
            or thems[them] == RPS.SCISSORS and your_throw == RPS.ROCK:
            # you win
            total_score += 6
        else:
            # you lose
            pass
    return total_score


if __name__ == "__main__":
    input_ = get_input(day=2)
    print(score_strategy_guide(input_.splitlines()))
    print(score_ldw_guide(input_.splitlines()))