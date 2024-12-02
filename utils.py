import requests


def get_puzzle_input(day, part=1):
    with open("session_token.txt", "r") as file:
        session_token = file.read().strip()
    url = f"https://adventofcode.com/2024/day/{day}/input"
    cookies = {"session": session_token}
    response = requests.get(url, cookies=cookies)
    if response.status_code != 200:
        raise Exception(
            "Failed to fetch input for day "
            f"{day}, part {part}: {response.status_code}"
        )
    return response.text.strip()
