import math
import sys


class Trade:
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
    BTC_money = 0
    ETH_money = 0
    USDT_money = 0
    BTC_ETH_list = [[]]
    USDT_ETH_list = [[]]
    USDT_BTC_list = [[]]

    def get_settings(self) -> int:
        for _ in range(0, 10):
            try:
                input_list = input()
            except:
                return 84
            training_list = input_list.split(" ")
            if (training_list[0] != "settings" or len(training_list) < 3):
                print("Bad setting : " + input_list, file=sys.stderr)
                return 84
            self.settings[training_list[1]] = training_list[2]
        return 0

    def set_format(self) -> int:
        good_val = 0
        candle_list = ["pair", "date", "high", "low", "open", "close", "volume"]
        self.candle_format = self.candle_format.split(",")
        if (len(self.candle_format) != 7):
            print("Error with candle_format : ",
                  self.candle_format, file=sys.stderr)
            return 84
        for i in self.candle_format:
            for j in candle_list:
                if i == j:
                    self._format[j] = good_val
                    good_val = good_val + 1
                    candle_list.remove(j)
        if (good_val != 7):
            print(f"Error with candle {self.candle_format}", file=sys.stderr)
            return 84
        return 0

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
        return 0

    def append_candles(self, string):
        arr = string.split(";")
        for i in arr:
            info = i.split(",")
            if (info[self._format["pair"]] == "BTC_ETH"):
                self.BTC_ETH_list.append([
                    float(info[self._format["date"]]),
                    float(info[self._format["high"]]),
                    float(info[self._format["low"]]),
                    float(info[self._format["open"]]),
                    float(info[self._format["close"]]),
                    float(info[self._format["volume"]])
                ])
            if (info[self._format["pair"]] == "USDT_ETH"):
                self.USDT_ETH_list.append([
                    float(info[self._format["date"]]),
                    float(info[self._format["high"]]),
                    float(info[self._format["low"]]),
                    float(info[self._format["open"]]),
                    float(info[self._format["close"]]),
                    float(info[self._format["volume"]])
                ])
            if (info[self._format["pair"]] == "USDT_BTC"):
                self.USDT_BTC_list.append([
                    float(info[self._format["date"]]),
                    float(info[self._format["high"]]),
                    float(info[self._format["low"]]),
                    float(info[self._format["open"]]),
                    float(info[self._format["close"]]),
                    float(info[self._format["volume"]])
                ])

    def set_money(self, string) -> int:
        arr = string.split(",")
        if (len(arr) != 3):
            print("Wrong value : " + string, file=sys.stderr)
            return 84
        for i in arr:
            info = i.split(":")
            if (len(info) != 2):
                return 84
            print(info[0], float(info[1]), file=sys.stderr)
            if (info[0] == "BTC"):
                self.BTC_stack = float(info[1])
            elif (info[0] == "ETH"):
                self.ETH_stack = float(info[1])
            elif (info[0] == "USDT"):
                self.USDT_stack = float(info[1])
            else:
                print(f"Money error at {i} itérator", file=sys.stderr)
                return 84
        return 0

    def order(self, milliseconds):
        print("pass")

    def main_loop(self) -> int:
        while (1):
            try:
                input_list = input()
            except:
                return 84
            training_list = input_list.split(" ")
            if (training_list[0] == "update" and training_list[1] == "game" and training_list[2] == "next_candles"):
                self.append_candles(training_list[3])
            elif (training_list[0] == "update" and training_list[1] == "game" and training_list[2] == "stacks"):
                if (self.set_money(training_list[3]) == 84):
                    print("Error in sey money !", file=sys.stderr)
                    return 84
            elif (training_list[0] == "action" and training_list[1] == "order"):
                self.order(float(training_list[2]))
            else:
                print("Unknow cmd : " + input_list, file=sys.stderr)
        return 0

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
