import sys, os
base_path = os.path.dirname(os.path.dirname(
                            os.path.abspath(__file__)))
sys.path.append(base_path)
import curses
from curses import wrapper
from vlc_player import VLCPlayer


class RadioUi:

    def __init__(self):
        self.player = VLCPlayer()
        self.radio_list = []
        self.init_radio_url_list()
        self.current_row_idx = 0
        self.pause_flag = False

    def init_radio_url_list(self):
        with open('./radio_list', 'r') as radio_list_file:
            for line in radio_list_file.readlines():
                self.radio_list.append(line.strip())

    def draw_radio_list(self, std_scr):
        std_scr.addstr(0, 0, '>>Radio List')
        for index, e in enumerate(self.radio_list):
            radio_name = e.split('_')[1]
            if self.current_row_idx == index:
                std_scr.attron(curses.color_pair(1))
                std_scr.addstr(index + 1, 0, radio_name)
                std_scr.attroff(curses.color_pair(1))
            else:
                std_scr.addstr(index + 1, 0, radio_name)

    def play_radio(self, current_row_idx):
        radio_full_url = self.radio_list[current_row_idx]
        radio_url = radio_full_url.split('_')[2]
        self.player.play(radio_url)

    def init_screen(self, std_scr):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        self.draw_radio_list(std_scr)
        std_scr.refresh()

        self.on_key_press(std_scr)

    def pause_or_resume(self):
        if self.pause_flag:
            self.player.resume()
            self.pause_flag = False
        else:
            self.player.pause()
            self.pause_flag = True

    def on_key_press(self, std_scr):
        while True:
            key = std_scr.getch()
            std_scr.clear()

            if key == 106 and self.current_row_idx < len(self.radio_list) - 1:
                self.current_row_idx += 1
            elif key == 107 and self.current_row_idx > 0:
                self.current_row_idx -= 1
            elif key == 108:
                self.play_radio(self.current_row_idx)
            elif key == 115:
                self.player.stop()
            elif key == 32:
                self.pause_or_resume()
            elif key == 113:
                exit(1)
            else:
                std_scr.addstr(f'key_name:{key}')
            self.draw_radio_list(std_scr)
            std_scr.refresh()

    def run(self):
        wrapper(self.init_screen)

