import json
import pandas as pd
import requests

import logging

log = logging.getLogger(__name__)


def get_titled_players(chess_title: str) -> list:
    """
    Returns a list of player names

    :param chess_title:
    :return: None
    """
    url = f'https://api.chess.com/pub/titled/{chess_title}'
    log.info(f"Getting names of {chess_title} players using {url}")

    response = requests.get(url)
    log.info(f"Response from server: {response}")

    response = response.json()

    player_list = []
    for player in response['players']:
        player_list.append(player)

    return player_list


def get_player_stats(player_list: list) -> None:
    """
    Iterates through a list of player names and returns game statistics

    :param player_list:
    :return:
    """
    with open('/data/player_stats.txt', 'w') as file:
        for username in player_list:
            url = f'https://api.chess.com/pub/player/{username}/stats'
            log.info(f"Getting stats for player {username} players using {url}")

            response = requests.get(url)
            log.info(f"Response from server: {response}")

            response = response.json()
            response['username'] = username

            json.dump(response, file)
            file.write('\n')


def load_player_stats():
    player_stats = []
    with open('/data/player_stats.txt') as f:
        for line in f:
            player_stats.append(json.loads(line))

    # create dataframe from json data
    player_stats = pd.json_normalize(player_stats)
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(player_stats)

    for col in df.columns:
        df.rename(columns={col: col.lower().replace(".", "_")}, inplace=True)

    df.to_csv("/home/stephen/chesscom/data/player_stats_cleaned.csv")
