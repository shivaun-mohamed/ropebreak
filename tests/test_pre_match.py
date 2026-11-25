from src.pre_match.pre_match_frontend import (
    display_primary_match_type,
    display_secondary_match_type,
    get_primary_match_type,
    get_secondary_match_type,
)


def test_get_primary_match_type_returns_primary_types():
    match_data = {"primary_match_type": ["Singles", "Tag Team"]}

    assert get_primary_match_type(match_data) == ["Singles", "Tag Team"]


def test_get_secondary_match_type_returns_secondary_types():
    match_data = {"secondary_match_type": ["Normal Match", "TLC"]}

    assert get_secondary_match_type(match_data) == ["Normal Match", "TLC"]


def test_display_primary_match_type_puts_each_type_on_a_new_line():
    primary_types = ["Singles", "Tag Team"]

    assert display_primary_match_type(primary_types) == "Singles\nTag Team"


def test_display_primary_match_type_with_one_type_has_no_extra_newline():
    primary_types = ["Singles"]

    assert display_primary_match_type(primary_types) == "Singles"


def test_display_secondary_match_type_puts_each_type_on_a_new_line():
    secondary_types = ["Normal Match", "TLC"]

    assert display_secondary_match_type(secondary_types) == "Normal Match\nTLC"


def test_display_secondary_match_type_with_one_type_has_no_extra_newline():
    secondary_types = ["Normal Match"]

    assert display_secondary_match_type(secondary_types) == "Normal Match"
