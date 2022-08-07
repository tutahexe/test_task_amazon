import pytest


@pytest.mark.db
def test_b_1(db):
    medium_rate = db.get_medium_rate()
    assert medium_rate > 3.5

@pytest.mark.db
def test_b_2(db):
    title = "kek"
    search_results = db.get_items_with_title(title)
    assert len(search_results) > 0

@pytest.mark.db
def test_b_3(db):
    item = db.get_newest_item()
    assert item.get_name() == "Accelerate DevOps"
