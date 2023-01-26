class MoneyExchange:
    def __init__(self, rate, commission_pct, from_currency_symbol, to_currency_symbol) -> None:
        self.rate = rate
        self.commission_pct = commission_pct
        self.from_currency_amount = 0
        self.from_currency_symbol = from_currency_symbol
        self.to_currency_amount = 0
        self.to_currency_symbol = to_currency_symbol
        
    def calc_from_to_currency_amount(self, from_amount):
        calculation = from_amount * self.rate
        calculation += calculation * self.commission_pct
        self.to_currency_amount = round(calculation, 4)
        # In addition set from_currency_amount
        self.from_currency_amount = round(from_amount + (from_amount * self.commission_pct), 4)

    def calc_to_from_currency_amount(self, to_amount):
        calculation = to_amount / self.rate
        calculation += calculation * self.commission_pct
        self.from_currency_amount = round(calculation, 4)
        # In addition set to_currency_amount
        self.to_currency_amount = round(to_amount + to_amount * self.commission_pct, 4)
    
    def get_all_currency_amount(self):
        return {
            'from_currency': {
                'amount': self.from_currency_amount,
                'symbol': self.from_currency_symbol
            },
            'to_currency': {
                'amount': self.to_currency_amount,
                'symbol': self.to_currency_symbol
            }
        }

class USD_VES_Exchange(MoneyExchange):
    def __init__(self, rate, commission_pct=0) -> None:
        super().__init__(rate, commission_pct, from_currency_symbol="$", to_currency_symbol="Bs")

    def usd_to_ves(self, usd_amount: float):
        self.calc_from_to_currency_amount(from_amount=usd_amount)

    def ves_to_usd(self, ves_amount: float):
        self.calc_to_from_currency_amount(to_amount=ves_amount)

    def get_all_currency_amount(self):
        return {
            'usd': {
                'amount': self.from_currency_amount,
                'symbol': self.from_currency_symbol
            },
            'ves': {
                'amount': self.to_currency_amount,
                'symbol': self.to_currency_symbol
            }
        }
