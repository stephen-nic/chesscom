import json
import os

import requests

from omegaconf import DictConfig, OmegaConf
import hydra

import logging

log = logging.getLogger(__name__)


@hydra.main(config_path="conf", config_name="config")
def run_my_app(cfg: DictConfig) -> None:
    """
    Starter point for the app

    :return: None
    """
    player_list = get_titled_players('GM')
    get_player_stats(player_list)


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
    with open('../data/tweet_json.txt', 'w') as outfile:
        for username in player_list:
            url = f'https://api.chess.com/pub/player/{username}/stats'
            log.info(f"Getting stats for player {username} players using {url}")

            response = requests.get(url)
            log.info(f"Response from server: {response}")

            response = response.json()
            json.dump(response, outfile)
            outfile.write('\n')


if __name__ == '__main__':
    run_my_app()
