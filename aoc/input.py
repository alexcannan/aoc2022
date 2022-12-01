# inputs are like https://adventofcode.com/2022/day/1/input

import os

import requests


class MissingSessionCookie(Exception):
    pass


session_cookie = os.environ.get("AOC_SESSION_COOKIE")
if not session_cookie:
    raise MissingSessionCookie("AOC_SESSION_COOKIE not set")


def get_input(day: int) -> str:
    return requests.get(f"https://adventofcode.com/2022/day/{day}/input", cookies={"session": session_cookie}).text