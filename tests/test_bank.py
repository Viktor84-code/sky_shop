import pytest

from src.bank import Bank
from src.transaction import Transaction


@pytest.fixture
def empty_bank():
    """Фикстура для создания чистого банка перед каждым тестом."""
    return Bank()


def test_add_valid_transaction(empty_bank):
    """Тест: Добавление корректного объекта Transaction."""
    tx = Transaction("Alice", "Bob", "100.0")
    empty_bank.add_transaction(tx)
    assert len(empty_bank._history) == 1
    assert empty_bank.get_total_amount() == 100.0


def test_add_invalid_type(empty_bank):
    """Тест: Попытка добавить число вместо объекта (должно игнорироваться)."""
    empty_bank.add_transaction(100500)  # Это не Transaction
    assert len(empty_bank._history) == 0


def test_add_string_recovery(empty_bank):
    """Тест: Авто-создание транзакции из строки (наш будущий функционал)."""
    # Сейчас этот тест УПАДЕТ, потому что кода еще нет. Это ПРАВИЛЬНО.
    empty_bank.add_transaction("500.0")
    assert len(empty_bank._history) == 1
    assert empty_bank.get_total_amount() == 500.0


def test_get_total_amount(empty_bank):
    """Тест: Проверка правильности подсчета общей суммы (строки 37-40)."""
    empty_bank.add_transaction(Transaction("A", "B", "100"))
    empty_bank.add_transaction(Transaction("C", "D", "200.50"))
    # Проверяем, что сумма считается корректно
    assert empty_bank.get_total_amount() == 300.50


def test_print_report(empty_bank, capsys):
    """Тест: Проверка вывода отчета (строки 53-54)."""
    empty_bank.add_transaction(Transaction("System", "User", "100"))
    empty_bank.print_full_report()

    # Перехватываем то, что ушло в консоль
    captured = capsys.readouterr()
    assert "АУДИТОРСКИЙ ОТЧЕТ БАНКА" in captured.out
    assert "ИТОГО В КАССЕ: 100.00 USD" in captured.out


def test_add_invalid_trash(empty_bank):
    """Закрываем ветку else (строка 29): подаем полный мусор."""
    empty_bank.add_transaction(None)  # Не Transaction и не str
    assert len(empty_bank._history) == 0


def test_add_invalid_string(empty_bank):
    """Закрываем ветку ValueError (строки 24-27): подаем строку с буквами."""
    empty_bank.add_transaction("abc")  # Строка, но не число
    assert len(empty_bank._history) == 0


def test_print_report_coverage(empty_bank, capsys):
    """Закрываем метод отчета (строки 53-54)."""
    tx = Transaction("A", "B", "100")
    empty_bank.add_transaction(tx)
    empty_bank.print_full_report()  # Вызываем метод!
    captured = capsys.readouterr()
    assert "АУДИТОРСКИЙ ОТЧЕТ" in captured.out


def test_add_transaction_object(empty_bank):
    """Закрываем строки 14-16: передаем живой объект."""
    tx = Transaction("Alice", "Bob", 100)
    empty_bank.add_transaction(tx)
    assert len(empty_bank._history) == 1


def test_add_invalid_string_error(empty_bank):
    """Закрываем строки 26-28: передаем буквы 'abc'."""
    # Теперь, когда в Transaction стоит raise ValueError,
    # банк поймает ошибку и НЕ добавит транзакцию.
    empty_bank.add_transaction("abc")
    assert len(empty_bank._history) == 0


def test_add_total_trash(empty_bank):
    """Закрываем строку 29: передаем None или список."""
    empty_bank.add_transaction(None)
    assert len(empty_bank._history) == 0
