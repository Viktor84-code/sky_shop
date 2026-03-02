class Transaction:

    def __init__(self, sender, receiver, amount):
        self.sender = sender.strip().lower()
        self.receiver = receiver.strip().lower()

        try:
            self._amount = float(amount)
        except ValueError:
            self._amount = 0.0

    @property
    def amount(self):
        """
        Датчик суммы (только для чтения)
        """
        return self._amount

    def is_valid(self):
        return 0 < self._amount <= 500000

    def get_summary(self):
        return f"Отправитель:{self.sender.capitalize()}, Сумма: {self._amount:.2f} USD"

    def is_fraud(self):
        return self.sender == self.receiver

    def apply_fee(self, percent):
        self._amount = self._amount * (1 - percent / 100)
        return self.amount


def compare_transactions(t1, t2):
    if t1.amount > t2.amount:
        return t1.sender.capitalize()
    elif t2.amount > t1.amount:
        return t2.sender.capitalize()
    else:
        return "Равны"
