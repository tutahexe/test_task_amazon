import pytest


@pytest.mark.db
def test_b_1(db):
    medium_rate = db.get_medium_rate()
    assert medium_rate > 3.5, f"Medium rate is {medium_rate}"


@pytest.mark.db
def test_b_2(db):
    title = "Modern CMake"
    search_results = db.get_items_with_title(title)
    assert len(search_results) > 0, f"{title} not present in DB"


@pytest.mark.db
def test_b_3(db):
    expected_name = "Accelerate DevOps"
    item = db.get_newest_item()
    first_item_name = item.get_name()
    assert first_item_name == expected_name, f"First item is {first_item_name} while was expected  {expected_name}"
