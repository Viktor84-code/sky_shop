from typing import Any

from src.transaction import Transaction


class Bank:
    def __init__(self) -> None:
        self._history: list[Transaction] = []

    def add_transaction(self, transaction: Any) -> None:
        """Добавляет транзакцию с проверкой типа (isinstance)."""
        if isinstance(transaction, Transaction):
            self._history.append(transaction)

        elif isinstance(transaction, str):
            clean_amount = transaction.strip()
            try:
                # Именно здесь происходит магия спасения данных
                new_tx = Transaction("System", "System", clean_amount)
                self._history.append(new_tx)
                print(f"✅ УСПЕХ: Восстановлено {clean_amount}")
            except ValueError:
                print(f"❌ ОШИБКА: Некорректная сумма в строке '{transaction}'")
        else:
            print("❌ ОШИБКА: Попытка добавить невалидный объект!")

    def get_total_amount(self) -> float:
        return sum(t.amount for t in self._history)

    def print_full_report(self) -> None:
        print("\n=== АУДИТОРСКИЙ ОТЧЕТ БАНКА ===")
        for t in self._history:
            print(t.get_summary())
        print(f"ИТОГО В КАССЕ: {self.get_total_amount():.2f} USD")
