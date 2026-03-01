import sys # модуль управления выходом
from src.transaction import Transaction
from src.bank import Bank


def main():
    """
    Главная функция запуска.
    """
    try:
        # инициализация
        t1 = Transaction('Viktor', 'Ivan', '5000.50')
        t2 = Transaction('Mark', 'Oleg', '2500.00')

        my_bank = Bank()
        my_bank.add_transaction(t1)
        my_bank.add_transaction(t2)

        # Работа системы
        my_bank.print_full_report()

        # Проверка безопасности
        print("\n--- ТЕСТ ИНКАПСУЛЯЦИИ ---")
        try:
            t1.amount = 999999
        except AttributeError:
            print("Защита: Прямое изменение суммы заблокировано!")

        # если все прошло успешно
        return 0

    except Exception as e:
        # если не прошло
        print(f"❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())