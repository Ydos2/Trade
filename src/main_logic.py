import math
import statistics
import sys

from .candlestick_japanese import candlestick


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
    period = 10

    _format = {}
    BTC_money = 0
    ETH_money = 0
    USDT_money = 0
    BTC_ETH_list = [[]]
    USDT_ETH_list = [[]]
    USDT_BTC_list = [[]]

    buy = [0, 0, 0]

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
        candle_list = ["pair", "date", "high",
                       "low", "open", "close", "volume"]
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

    def last_relative_evolution(self, tab):
        val = ((tab[len(tab) - 2][5] - tab[len(tab) - 2 - self.period][5]) /
                tab[len(tab) - 2 - self.period][5]) * 100
        return val

    def actual_relative_evolution(self, tab):
        val = ((tab[len(tab) - 1][5] - tab[len(tab) - 1 - self.period][5]) /
                tab[len(tab) - 1 - self.period][5]) * 100
        return val

    def is_occur(self, tab):
        if (len(tab) < self.period + 3):
            return 0
        if (tab[len(tab) - 1 - self.period][5] == 0 or tab[len(tab) - 2 - self.period][5] == 0):
            return 0
        x = self.actual_relative_evolution(tab)
        y = self.last_relative_evolution(tab)
        if ((x  >= 0 and y < 0) or (x < 0 and y >= 0)):
            return 1
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
                #if (self.is_occur(self.BTC_ETH_list)):
                #    print("BTC switch occurs !", file=sys.stderr)
            if (info[self._format["pair"]] == "USDT_ETH"):
                self.USDT_ETH_list.append([
                    float(info[self._format["date"]]),
                    float(info[self._format["high"]]),
                    float(info[self._format["low"]]),
                    float(info[self._format["open"]]),
                    float(info[self._format["close"]]),
                    float(info[self._format["volume"]])
                ])
                #if (self.is_occur(self.USDT_ETH_list)):
                #    print("ETH switch occurs !", file=sys.stderr)
            if (info[self._format["pair"]] == "USDT_BTC"):
                self.USDT_BTC_list.append([
                    float(info[self._format["date"]]),
                    float(info[self._format["high"]]),
                    float(info[self._format["low"]]),
                    float(info[self._format["open"]]),
                    float(info[self._format["close"]]),
                    float(info[self._format["volume"]])
                ])
                #if (self.is_occur(self.USDT_BTC_list)):
                #    print("USDT switch occurs !", file=sys.stderr)
    def set_money(self, string) -> int:
        arr = string.split(",")
        if (len(arr) != 3):
            print("Wrong value : " + string, file=sys.stderr)
            return 84
        for i in arr:
            info = i.split(":")
            if (len(info) != 2):
                return 84
            # print(info[0], float(info[1]), file=sys.stderr)
            if (info[0] == "BTC"):
                self.BTC_money = float(info[1])
            elif (info[0] == "ETH"):
                self.ETH_money = float(info[1])
            elif (info[0] == "USDT"):
                self.USDT_money = float(info[1])
            else:
                print(f"Money error at {i} itérator", file=sys.stderr)
                return 84
        return 0

    def go_buy(self, name_money: str, money_actu: int, hasBought: bool, type_money: int) -> bool:
        if (money_actu >= self.buy[type_money] and self.buy[type_money] > 0.001):
            if (hasBought):
                print(";", end='')
            print("buy " + name_money + " " + str(self.buy[type_money]), end='')
            print("should buy !", file=sys.stderr)
            self.buy[type_money] = 0
            return (True)
        elif (self.buy[type_money] < 0):
            if (hasBought):
                print(";", end='')
            print("sell " + name_money + " " + str(self.buy[type_money]), end='')
            print("should sell !", file=sys.stderr)
            self.buy[type_money] = 0
            return (True)
        return (False)

    def set_action(self, milliseconds):
        isBuy = False
        if (self.go_buy("USDT_ETH", self.USDT_money, False, 0) == True):
            isBuy = True
        if (self.go_buy("BTC_ETH", self.BTC_money, isBuy, 1) == True):
            isBuy = True
        if (self.go_buy("USDT_BTC", self.USDT_money, isBuy, 2) == True):
            isBuy = True
        if (isBuy):
            print("")
            print("Buy today !", file=sys.stderr)
        else:
            print("pass")
            print("Pass to another day !", file=sys.stderr)

    def set_buy(self, action: list):
        if (action[0] > 6):
            self.buy[0] = 0.5
        elif (action[0] < 0):
            self.buy[0] = -0.5
        else:
            self.buy[0] = 0

        if (action[1] > 6):
            self.buy[1] = 0.5
        elif (action[1] < 0):
            self.buy[1] = -0.5
        else:
            self.buy[1] = 0

        if (action[2] > 6):
            self.buy[2] = 0.5
        elif (action[2] < 0):
            self.buy[2] = -0.5
        else:
            self.buy[2] = 0

    def main_loop(self) -> int:
        candlestick_class = candlestick()
        index = 0
        while (1):
            try:
                input_list = input()
            except:
                return 84
            training_list = input_list.split(" ")
            print("Command : " + input_list, file=sys.stderr)
            if (training_list[0] == "update" and training_list[1] == "game" and training_list[2] == "next_candles"):
                self.append_candles(training_list[3])
                if index > 4:
                    action = candlestick_class.candlestick_japanese(self.BTC_ETH_list, self.USDT_ETH_list, self.USDT_BTC_list)
                    self.set_buy(action)
            elif (training_list[0] == "update" and training_list[1] == "game" and training_list[2] == "stacks"):
                if (self.set_money(training_list[3]) == 84):
                    print("Error in sey money !", file=sys.stderr)
                    return 84
            elif (training_list[0] == "action" and training_list[1] == "order"):
                self.set_action(float(training_list[2]))
            else:
                print("Unknow cmd : " + input_list, file=sys.stderr)
            index += 1
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
