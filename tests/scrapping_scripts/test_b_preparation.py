def test_b_data_preparation(ui, db):
    ui.open_landing()
    ui.landing.search_for_item('software testing')
    search_results = ui.landing.get_items_from_page()
    items = ui.landing.build_item_objects_from_search_results(search_results)
    db.write_items_to_db(items)
    items2 = db.get_all_items_from_db()
    print(items2)
