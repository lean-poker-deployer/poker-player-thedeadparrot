import json
import urllib
import threading

import time

CONFIG_JSON_URL = 'https://dl.dropboxusercontent.com/u/819938/leanpoker/config.json'


class Config(object):
    version = 'config not loaded'
    refresh_interval = 5
    bet_on_high_card = 0
    bet_on_pair = 0
    bet_on_high_pair = 1000

    def __init__(self):
        self._start_thread()

    def load(self):
        r = urllib.urlopen(CONFIG_JSON_URL)
        config_json = json.load(r)

        for k, v in config_json.iteritems():
            self.__setattr__(k, v)

    def _start_thread(self):
        thread = threading.Thread(target=self._load)
        thread.start()

    def _load(self):
        while True:
            self.load()
            time.sleep(self.refresh_interval)
