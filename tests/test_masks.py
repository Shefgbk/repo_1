import pytest
from masks import get_mask_card_number, get_mask_account


# @pytest.fixture
# def card_numbers():
#     return ['7000792289606361', '6361700079228960', '7000896063617922', '6361792289607000']
#
#
# @pytest.mark.parametrize("masked_card", ['7000 79** **** 6361 ',
#                                          '6361 70** **** 8960 ',
#                                          '7000 89** **** 7922 ',
#                                          '6361 79** **** 7000 '])
# def test_get_mask_card_number(card_numbers, masked_card):
#     assert get_mask_card_number(card_numbers) == masked_card
assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361 '


