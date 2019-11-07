import sys, os
base_path = os.path.dirname(os.path.dirname(
                            os.path.abspath(__file__)))
sys.path.append(base_path)
import vlc


class VLCPlayer:

    def __init__(self):
        vlc_instance = vlc.Instance()
        self._player = vlc_instance.media_player_new()

    @property
    def player(self):
        return self._player

    def play(self, url: str):
        self.stop()
        self.player.set_mrl(url)
        self.player.play()

    def stop(self):
        self.player.stop()

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.set_pause(0)
