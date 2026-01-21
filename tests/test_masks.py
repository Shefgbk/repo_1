import pytest
from masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, masked_card", zip(
    ['7000792289606361', '6361700079228960', '7000896063617922', '6361792289607000'],
    ['7000 79** **** 6361 ', '6361 70** **** 8960 ', '7000 89** **** 7922 ', '6361 79** **** 7000 ']
))
def test_get_mask_card_number(card_number: str, masked_card: str) -> bool:     # тестируем корректные данные
    assert get_mask_card_number(card_number) == masked_card


def test_simple() -> bool:       # тестируем корректные данные
    assert get_mask_card_number('1111111111111111') == '1111 11** **** 1111 '
    assert get_mask_card_number('6361700079228960') == '6361 70** **** 8960 '
    assert get_mask_card_number('7000896063617922') == '7000 89** **** 7922 '
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('11111111111111111111') == '**1111'


def test_mask_card_number_incorrect() -> bool:
    with pytest.raises(ValueError):
        get_mask_card_number('7000 7922 8960 6361')  # тестируем номер с пробелами

    with pytest.raises(ValueError):
        get_mask_card_number('700079228960636')  # тестируем короткий номер

    with pytest.raises(ValueError):
        get_mask_card_number('70000792289606369')  # тестируем длинный номер

    with pytest.raises(ValueError):
        get_mask_card_number('abcdefghijklmnop')  # тестируем номер из букв

    with pytest.raises(ValueError):
        get_mask_card_number('')  # тестируем пустую строку


@pytest.mark.parametrize("bank_account, masked_account", zip(
    ['73654108430135874305', '13587430573654108430', '73654174305084301358', '87430573654108430135'],
    ['**4305', '**8430', '**1358', '**0135']
))
def test_get_mask_account(bank_account: list, masked_account: list) -> bool:    # тестируем корректные данные
    assert get_mask_account(bank_account) == masked_account


def test_mask_account_incorrect() -> bool:
    with pytest.raises(ValueError):
        get_mask_account('7365 4108 4301 3587 4305')  # тестируем номер с пробелами

    with pytest.raises(ValueError):
        get_mask_account('1358743057365410843')  # тестируем короткий номер

    with pytest.raises(ValueError):
        get_mask_account('135874305736541084300')  # тестируем длинный номер

    with pytest.raises(ValueError):
        get_mask_account('abcdefghijklmnopqrst')  # тестируем номер из букв

    with pytest.raises(ValueError):
        get_mask_account('')  # тестируем пустую строку
