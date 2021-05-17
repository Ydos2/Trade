import sys


class candlestick:
    BTC_ETH_list = [[]]
    USDT_ETH_list = [[]]
    USDT_BTC_list = [[]]

    actions_day = [[[]]]

    def le_marteau(self, val_list: list) -> int:
        val_high = val_list[1]
        val_low = val_list[2]
        val_open = val_list[3]
        val_close = val_list[4]
        if (val_high == val_open and val_low < val_close) or (val_high == val_close and val_low < val_open):
            print("Marteau", file=sys.stderr)
            return 1
        elif (val_low == val_open and val_high < val_close) or (val_low == val_close and val_high < val_open):
            print("Marteau", file=sys.stderr)
            return 1
        return 0

    def le_pendu(self, val_list: list) -> int:
        # Pareil que pour le marteau sauf que le pendu est localisé en haut d'une montée à l'inverse du marteau, qui se situe davantage en bas d'une descente
        return 0

    def le_doji(self, val_list: list) -> int:
        #val_high = val_list[1]
        #val_low = val_list[2]
        val_open = val_list[3]
        val_close = val_list[4]
        if (val_open == val_close):
            print("Doji", file=sys.stderr)
            return 1
        return 0

    def le_marubozu(self, val_list: list) -> int:
        val_high = val_list[1]
        val_low = val_list[2]
        val_open = val_list[3]
        val_close = val_list[4]
        if (val_high <= val_close and val_high >= val_open and val_low <= val_close and val_low >= val_open):
            print("Marubozu", file=sys.stderr)
            return 1
        return 0

    def le_morubozu(self, val_list: list) -> int:
        val_high = val_list[1]
        val_low = val_list[2]
        val_open = val_list[3]
        val_close = val_list[4]
        if (val_high >= val_close and val_high <= val_open and val_low >= val_close and val_low <= val_open):
            print("Morubozu", file=sys.stderr)
            return -1
        return 0

    def opening_yang_bozu(self, val_list: list) -> int:
        val_high = val_list[1]
        val_low = val_list[2]
        val_open = val_list[3]
        val_close = val_list[4]
        if (val_high <= val_close and val_high >= val_open and val_low < val_close and val_low < val_open):
            #print("Opening yang bozu", file=sys.stderr)
            return 1
        return 0

    def opening_yin_bozu(self, val_list: list) -> int:
        val_high = val_list[1]
        val_low = val_list[2]
        val_open = val_list[3]
        val_close = val_list[4]
        if (val_high >= val_close and val_high <= val_open and val_low > val_close and val_low > val_open):
            #print("Opening yin bozu", file=sys.stderr)
            return -1
        return 0

    def closing_yang_bozu(self, val_list: list) -> int:
        val_high = val_list[1]
        val_low = val_list[2]
        val_open = val_list[3]
        val_close = val_list[4]
        #print(f"ici {val_list}", file=sys.stderr)
        #print(f"high {val_list[1]}", file=sys.stderr)
        #print(f"low {val_list[2]}", file=sys.stderr)
        #print(f"open {val_list[3]}", file=sys.stderr)
        #print(f"close {val_list[4]}", file=sys.stderr)
        #print(f"", file=sys.stderr)
        # if (val_low >= val_close and val_low >= val_open and val_high < val_close and val_high < val_open and val_open < val_close):
        if (val_open < val_close):
            #print("Closing yang bozu", file=sys.stderr)
            return 1
        return 0

    def closing_yin_bozu(self, val_list: list) -> int:
        val_high = val_list[1]
        val_low = val_list[2]
        val_open = val_list[3]
        val_close = val_list[4]
        if (val_open > val_close):
            #print("Closing yin bozu", file=sys.stderr)
            return -1
        return 0

    # Les configurations double
    def avalement(self, val_list: list) -> int:
        return 0

    def harami(self, val_list: list) -> int:
        return 0

    def penetrante_baissiere(self, val_list: list) -> int:
        return 0

    def penetrante_haussiere(self, val_list: list) -> int:
        return 0

    def ligne_de_separation(self, val_list: list) -> int:
        return 0

    def ligne_de_pousse(self, val_list: list) -> int:
        return 0

    def les_etoiles(self, val_list: list) -> int:
        return 0

    def bebe_abandonne(self, val_list: list) -> int:
        return 0

    def les_trois_soldats_bleus(self, val_list: list) -> int:
        return 0

    def les_trois_corbeaux_rouges(self, val_list: list) -> int:
        return 0

    def can_trade(self, val_usdt: list, val_btc: list, val_eth: list):
        moyenne = 0
        i = 0
        for val in val_usdt:
            if i >= (len(val_usdt) - 7):
                if val > 0:
                    moyenne += 1
            i += 1
        self.actions_day.append(moyenne)
        
        moyenne = 0
        i = 0
        for val in val_btc:
            if i >= (len(val_btc) - 7):
                if val > 0:
                    moyenne += 1
            i += 1
        self.actions_day.append(moyenne)

        moyenne = 0
        i = 0
        for val in val_eth:
            if i >= (len(val_eth) - 7):
                if val > 0:
                    moyenne += 1
            i += 1
        self.actions_day.append(moyenne)

        return 0

    def candlestick_japanese(self, BTC_ETH_list: list, USDT_ETH_list: list, USDT_BTC_list: list) -> actions_day:
        self.BTC_ETH_list = BTC_ETH_list
        self.USDT_ETH_list = USDT_ETH_list
        self.USDT_BTC_list = USDT_BTC_list

        val_usdt = []
        val_btc = []
        val_eth = []

        index = 0

        for _ in USDT_BTC_list:
            indice_usdt = 0
            if index < 4:
                #print(f"ici {USDT_BTC_list}", file=sys.stderr)
                index += 1
                continue
            #print(f"la {USDT_BTC_list[index]}", file=sys.stderr)
            indice_usdt += self.le_marteau(USDT_BTC_list[index])
            indice_usdt += self.le_pendu(USDT_BTC_list[index])
            indice_usdt += self.le_doji(USDT_BTC_list[index])
            indice_usdt += self.le_marubozu(USDT_BTC_list[index])
            indice_usdt += self.le_morubozu(USDT_BTC_list[index])
            indice_usdt += self.opening_yang_bozu(USDT_BTC_list[index])
            indice_usdt += self.opening_yin_bozu(USDT_BTC_list[index])
            indice_usdt += self.closing_yang_bozu(USDT_BTC_list[index])
            indice_usdt += self.closing_yin_bozu(USDT_BTC_list[index])
            indice_usdt += self.avalement(USDT_BTC_list[index])
            indice_usdt += self.harami(USDT_BTC_list[index])
            indice_usdt += self.penetrante_baissiere(USDT_BTC_list[index])
            indice_usdt += self.penetrante_haussiere(USDT_BTC_list[index])
            indice_usdt += self.ligne_de_separation(USDT_BTC_list[index])
            indice_usdt += self.ligne_de_pousse(USDT_BTC_list[index])
            indice_usdt += self.les_etoiles(USDT_BTC_list[index])
            indice_usdt += self.bebe_abandonne(USDT_BTC_list[index])
            indice_usdt += self.les_trois_soldats_bleus(USDT_BTC_list[index])
            indice_usdt += self.les_trois_corbeaux_rouges(USDT_BTC_list[index])
            val_usdt.append(indice_usdt)
            index += 1
        index = 0
        for _ in BTC_ETH_list:
            indice_btc = 0
            if index < 4:
                index += 1
                continue
            indice_btc += self.le_marteau(USDT_BTC_list[index])
            indice_btc += self.le_pendu(USDT_BTC_list[index])
            indice_btc += self.le_doji(USDT_BTC_list[index])
            indice_btc += self.le_marubozu(USDT_BTC_list[index])
            indice_btc += self.le_morubozu(USDT_BTC_list[index])
            indice_btc += self.opening_yang_bozu(USDT_BTC_list[index])
            indice_btc += self.opening_yin_bozu(USDT_BTC_list[index])
            indice_btc += self.closing_yang_bozu(USDT_BTC_list[index])
            indice_btc += self.closing_yin_bozu(USDT_BTC_list[index])
            indice_btc += self.avalement(USDT_BTC_list[index])
            indice_btc += self.harami(USDT_BTC_list[index])
            indice_btc += self.penetrante_baissiere(USDT_BTC_list[index])
            indice_btc += self.penetrante_haussiere(USDT_BTC_list[index])
            indice_btc += self.ligne_de_separation(USDT_BTC_list[index])
            indice_btc += self.ligne_de_pousse(USDT_BTC_list[index])
            indice_btc += self.les_etoiles(USDT_BTC_list[index])
            indice_btc += self.bebe_abandonne(USDT_BTC_list[index])
            indice_btc += self.les_trois_soldats_bleus(USDT_BTC_list[index])
            indice_btc += self.les_trois_corbeaux_rouges(USDT_BTC_list[index])
            val_btc.append(indice_btc)
            index += 1
        index = 0
        for _ in USDT_ETH_list:
            indice_eth = 0
            if index < 4:
                index += 1
                continue
            indice_eth += self.le_marteau(USDT_ETH_list[index])
            indice_eth += self.le_pendu(USDT_ETH_list[index])
            indice_eth += self.le_doji(USDT_ETH_list[index])
            indice_eth += self.le_marubozu(USDT_ETH_list[index])
            indice_eth += self.le_morubozu(USDT_ETH_list[index])
            indice_eth += self.opening_yang_bozu(USDT_ETH_list[index])
            indice_eth += self.opening_yin_bozu(USDT_ETH_list[index])
            indice_eth += self.closing_yang_bozu(USDT_ETH_list[index])
            indice_eth += self.closing_yin_bozu(USDT_ETH_list[index])
            indice_eth += self.avalement(USDT_ETH_list[index])
            indice_eth += self.harami(USDT_ETH_list[index])
            indice_eth += self.penetrante_baissiere(USDT_ETH_list[index])
            indice_eth += self.penetrante_haussiere(USDT_ETH_list[index])
            indice_eth += self.ligne_de_separation(USDT_ETH_list[index])
            indice_eth += self.ligne_de_pousse(USDT_ETH_list[index])
            indice_eth += self.les_etoiles(USDT_ETH_list[index])
            indice_eth += self.bebe_abandonne(USDT_ETH_list[index])
            indice_eth += self.les_trois_soldats_bleus(USDT_ETH_list[index])
            indice_eth += self.les_trois_corbeaux_rouges(USDT_ETH_list[index])
            val_eth.append(indice_eth)
            index += 1
        index = 4
        self.can_trade(val_usdt, val_btc, val_eth)
        return 0
