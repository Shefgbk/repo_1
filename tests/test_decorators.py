import pytest

from src.decorators import log


def test_log_ok_my_function(capsys: pytest.CaptureFixture[str]) -> None:   # Тестируем нормальную работу декоратора log
    @log()                                                                 # с выводом результатов в консоль
    def my_function(x: int | float, y: int | float) -> int | float:
        return x + y
    result = my_function(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert 'my_function OK.' in captured.out
    assert 'Start time:' in captured.out
    assert 'Result: 5.' in captured.out
    assert 'End time:' in captured.out


def test_log_ok_my_function_in_file() -> None:      # Тестируем нормальную работу декоратора log
    @log('mylog.txt')                               # с выводом результатов в файл 'mylog.txt'
    def my_function(x: int | float, y: int | float) -> int | float:
        return x + y
    result = my_function(2, 3)
    assert result == 5
    with open('mylog.txt', 'r') as file:
        msg = file.read()
        assert 'my_function OK.' in msg
        assert 'Start time:' in msg
        assert 'Result: 5.' in msg
        assert 'End time:' in msg


def test_log_err_my_function(capsys: pytest.CaptureFixture[str]) -> None:   # Тестируем работу декоратора log
    @log()                                                                  # с некорректными данными декорируемой
    def my_function(x: int | float, y: int | float) -> int | float:         # функции с выводом результатов в консоль
        return x + y
    result = my_function('2', 3)
    captured = capsys.readouterr()
    assert result is None
    assert 'my_function ERROR.' in captured.out
    assert 'Start time:' in captured.out
    assert "Error: <class 'TypeError'>." in captured.out
    assert "Inputs: ('2', 3),{}." in captured.out
    assert 'End time:' in captured.out


def test_log_err_my_function_in_file() -> None:                         # Тестируем работу декоратора log
    @log('mylog.txt')                                                   # с некорректными данными декорируемой функции
    def my_function(x: int | float, y: int | float) -> int | float:     # с выводом результатов в файл 'mylog.txt'
        return x + y
    result = my_function('2', 3)
    assert result is None
    with open('mylog.txt', 'r') as file:
        msg = file.read()
        assert 'my_function ERROR.' in msg
        assert 'Start time:' in msg
        assert "Error: <class 'TypeError'>." in msg
        assert "Inputs: ('2', 3),{}." in msg
        assert 'End time:' in msg
