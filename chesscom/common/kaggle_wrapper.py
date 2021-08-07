from kaggle.api.kaggle_api_extended import KaggleApi


class KaggleWrapper:
    def __init__(self):
        self.la = 'ls'


api = KaggleApi()
api.authenticate()
