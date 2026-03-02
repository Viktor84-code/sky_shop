from src.transaction import Transaction


class Bank:
    def __init__(self) -> None:
        # Приватная история транзакций
        self._history: list[Transaction] = []

    def add_transaction(self, transaction: Transaction) -> None:
        """
        Добавляют транзакцию с проверкой типа(isinstance).
        """
        if isinstance(transaction, Transaction):
            self._history.append(transaction)
        else:
            print("❌ ОШИБКА: Попытка добавить невалидный объект в банк!")

    def get_total_amount(self) -> float:
        """
        Считает общую сумму всех транзакций в истории.
        """
        return sum(t.amount for t in self._history)

    def print_full_report(self) -> None:
        """
        Печатает красивый отчет по всем операциям.
        """
        print("=== АУДИТОРСКИЙ ОТЧЕТ БАНКА ===")
        for t in self._history:
            print(t.get_summary())
        print(f"ИТОГО В КАССЕ: {self.get_total_amount():.2f} USD")
