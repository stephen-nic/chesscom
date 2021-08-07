from omegaconf import DictConfig, OmegaConf
import hydra

from chesscom.common.titled_players import (
    get_titled_players,
    get_player_stats,
    load_player_stats)

import logging

log = logging.getLogger(__name__)


@hydra.main(config_path="conf", config_name="config")
def run_my_app(cfg: DictConfig) -> None:
    """
    Starter point for the app

    :return: None
    """
    # Chess API
    player_list = get_titled_players('GM')
    get_player_stats(player_list)
    load_player_stats()

    # Kaggle


if __name__ == '__main__':
    run_my_app()
