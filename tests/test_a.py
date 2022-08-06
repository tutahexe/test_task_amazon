def test_a(ui):
    ui.open_landing()
    ui.landing.search_for_item('software testing')
    first_item_name = ui.landing.get_first_item_title()
    ui.landing.open_item(0)
    ui.item_details.add_to_cart()
    ui.landing.open_cart()
    item_in_cart = ui.cart.get_item_in_cart_title()
    assert (first_item_name == item_in_cart)
