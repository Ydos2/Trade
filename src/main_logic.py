import math
import sys


class Trade:
    _input = ""
    settings = {}

    timebank = 0
    time_per_move = 0
    player_names = ""
    your_bot = ""
    candle_interval = 0
    candles_total = 0
    candles_given = 0
    initial_stack = 0
    candle_format = ""
    transaction_fee_percent = 0

    _format = {}
    BTC_stack = 0
    ETH_stack = 0
    USDT_stack = 0
    BTC_ETH_array = [{}]
    USDT_ETH_array = [{}]
    USDT_BTC_array = [{}]

    def get_input(self):
        try:
            self._input = input()
        except:
            exit(0)

    def get_settings(self) -> int:
        for _ in range(0, 10):
            self.get_input()
            arr = self._input.split(" ")
            if (arr[0] != "settings" or len(arr) < 3):
                print("Bad setting : " + self._input, file=sys.stderr)
                return 84
            self.settings[arr[1]] = arr[2]
        return 0

    def set_format(self) -> int:
        good_val = 0
        candle_arr = ["pair", "date", "high", "low", "open", "close", "volume"]
        self.candle_format = self.candle_format.split(",")
        if (len(self.candle_format) != 7):
            print("Error with candle_format : ",
                  self.candle_format, file=sys.stderr)
            return 84
        for i in self.candle_format:
            for j in candle_arr:
                if i == j:
                    self._format[j] = good_val
                    good_val = good_val + 1
                    candle_arr.remove(j)
        if (good_val != 7):
            print("Error with candle_format : ",
                  self.candle_format, file=sys.stderr)
            return 84

    def set_settings(self) -> int:
        try:
            self.timebank = int(self.settings["timebank"])
            self.time_per_move = int(self.settings["time_per_move"])
            self.player_names = self.settings["player_names"]
            self.your_bot = self.settings["your_bot"]
            self.candle_interval = int(self.settings["candle_interval"])
            self.candles_total = int(self.settings["candles_total"])
            self.candles_given = int(self.settings["candles_given"])
            self.initial_stack = int(self.settings["initial_stack"])
            self.candle_format = self.settings["candle_format"]
            self.transaction_fee_percent = float(
                self.settings["transaction_fee_percent"])
        except:
            print("Settings error", file=sys.stderr)
            return 84
        self.set_format()

    def get_info(self, arr, info):
        return arr[self._format[info]]

    def append_candles(self, string):
        arr = string.split(";")
        for i in arr:
            info = i.split(",")
            if (self.get_info(info, "pair") == "BTC_ETH"):
                self.BTC_ETH_array[-1]["date"] = float(
                    self.get_info(info, "date"))
                self.BTC_ETH_array[-1]["high"] = float(
                    self.get_info(info, "high"))
                self.BTC_ETH_array[-1]["low"] = float(
                    self.get_info(info, "low"))
                self.BTC_ETH_array[-1]["open"] = float(
                    self.get_info(info, "open"))
                self.BTC_ETH_array[-1]["close"] = float(
                    self.get_info(info, "close"))
                self.BTC_ETH_array[-1]["volume"] = float(
                    self.get_info(info, "volume"))
                self.BTC_ETH_array.append({})
            if (self.get_info(info, "pair") == "USDT_ETH"):
                self.USDT_ETH_array[-1]["date"] = float(
                    self.get_info(info, "date"))
                self.USDT_ETH_array[-1]["high"] = float(
                    self.get_info(info, "high"))
                self.USDT_ETH_array[-1]["low"] = float(
                    self.get_info(info, "low"))
                self.USDT_ETH_array[-1]["open"] = float(
                    self.get_info(info, "open"))
                self.USDT_ETH_array[-1]["close"] = float(
                    self.get_info(info, "close"))
                self.USDT_ETH_array[-1]["volume"] = float(
                    self.get_info(info, "volume"))
                self.USDT_ETH_array.append({})
            if (self.get_info(info, "pair") == "USDT_BTC"):
                self.USDT_BTC_array[-1]["date"] = float(
                    self.get_info(info, "date"))
                self.USDT_BTC_array[-1]["high"] = float(
                    self.get_info(info, "high"))
                self.USDT_BTC_array[-1]["low"] = float(
                    self.get_info(info, "low"))
                self.USDT_BTC_array[-1]["open"] = float(
                    self.get_info(info, "open"))
                self.USDT_BTC_array[-1]["close"] = float(
                    self.get_info(info, "close"))
                self.USDT_BTC_array[-1]["volume"] = float(
                    self.get_info(info, "volume"))
                self.USDT_BTC_array.append({})

    def set_stack(self, string) -> int:
        arr = string.split(",")
        if (len(arr) != 3):
            print("Wrong value : " + string, file=sys.stderr)
            return 84
        for i in arr:
            info = i.split(":")
            if (len(info) != 2):
                return 84
            elif (info[0] == "BTC"):
                self.BTC_stack = float(info[1])
            elif (info[0] == "ETH"):
                self.ETH_stack = float(info[1])
            elif (info[0] == "USDT"):
                self.USDT_stack = float(info[1])
            else:
                print("Unknow val : " + i, file=sys.stderr)
                return 84

    def order(self, milliseconds):
        print("pass")

    def main_loop(self) -> int:
        while (1):
            self.get_input()
            arr = self._input.split(" ")
            if (arr[0] == "update" and arr[1] == "game" and arr[2] == "next_candles"):
                self.append_candles(arr[3])
            elif (arr[0] == "update" and arr[1] == "game" and arr[2] == "stacks"):
                if (self.set_stack(arr[3]) == 84):
                    print("Error in update !", file=sys.stderr)
                    return 84
            elif (arr[0] == "action" and arr[1] == "order"):
                self.order(float(arr[2]))
            else:
                print("Unknow cmd : " + self._input, file=sys.stderr)

    def start(self) -> int:
        if (self.get_settings() == 84):
            print("Error in get settings", file=sys.stderr)
            return 84
        if (self.set_settings() == 84):
            print("Error in set settings", file=sys.stderr)
            return 84
        if (self.main_loop() == 84):
            print("Error in loop", file=sys.stderr)
            return 84
        return 0
