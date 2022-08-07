import time

import pytest


@pytest.mark.data
def test_b_data_preparation(ui, db):
    db.clean_up_table()
    ui.open_landing()
    #time.sleep(10)  # Sleep to pass manually a robot check
    ui.landing.search_for_item('software testing')
    for page in range(2):
        search_results = ui.landing.get_items_from_page()
        items = ui.landing.build_item_objects_from_search_results(search_results)
        db.write_items_to_db(items)
        ui.landing.go_to_next_page()
        time.sleep(10)
    assert len(db.get_all_items_from_db()) > 0
