import sender_stand_request
def positive_assert():
    order_response = sender_stand_request.get_order_on_number()
    assert order_response.status_code == 200

    def test_order_on_number_get_response_200():
        positive_assert()