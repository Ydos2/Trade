class candlestick:
    m_high = 0
    m_low = 0
    m_open = 0
    m_close = 0

    def le_marteau(self) -> int:
        return 0

    def le_pendu(self) -> int:
        return 0

    def le_doji(self) -> int:
        return 0

    def le_marubozu(self) -> int:
        return 0

    def le_morubozu(self) -> int:
        return 0

    def opening_yang_bozu(self) -> int:
        return 0

    def opening_yin_bozu(self) -> int:
        return 0

    def closing_yang_bozu(self) -> int:
        return 0

    def closing_yin_bozu(self) -> int:
        return 0

    # Les configurations double
    def avalement(self) -> int:
        return 0

    def harami(self) -> int:
        return 0

    def penetrante_baissiere(self) -> int:
        return 0

    def penetrante_haussiere(self) -> int:
        return 0

    def ligne_de_separation(self) -> int:
        return 0

    def ligne_de_pousse(self) -> int:
        return 0

    def les_etoiles(self) -> int:
        return 0

    def bebe_abandonne(self) -> int:
        return 0

    def les_trois_soldats_bleus(self) -> int:
        return 0

    def les_trois_corbeaux_rouges(self) -> int:
        return 0

    def candlestick_japanese(self, high: int, low: int, open_val: int, close: int) -> int:
        self.m_high = high
        self.m_low = low
        self.m_open = open_val
        self.m_close = close
        return 0
