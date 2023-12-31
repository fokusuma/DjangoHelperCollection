import pytest
from tools.lionparcel_helper import LionParcelHelper
from django.conf import settings


@pytest.fixture
def lion_parcel_helper():
    api_key = 'YOUR API KEY'
    return LionParcelHelper(api_key)


def test_get_tariff(lion_parcel_helper):
    # Arrange
    origin = "ORIGIN"
    destination = "DESTINATION"
    weight = 10
    commodity = "COMMODITY"

    # Act
    result = lion_parcel_helper.get_tariff(origin, destination, weight, commodity)

    # Assert
    assert "forward_area" in result


def test_make_booking(lion_parcel_helper):
    # Arrange
    booking_data = {
        "stt_goods_estimate_price": 300000,
        "stt_origin": "ORIGIN",
        "stt_destination": "DESTINATION",
        "stt_sender_name": "TEST",
        "stt_sender_phone": "08123456789",
        "stt_sender_address": "JL. TEST",
        "stt_recipient_name": "TEST 2",
        "stt_recipient_address": "JL. TEST 2",
        "stt_recipient_phone": "081234567892",
        "stt_product_type": "TYPE",
        "stt_commodity_code": "COMMODITY",
        "stt_pieces": [
            {
                "stt_piece_gross_weight": 10,
                "stt_piece_length": 10,
                "stt_piece_width": 10,
                "stt_piece_height": 10,
            }
        ],
    }

    # Act
    result = lion_parcel_helper.make_booking(booking_data)

    # Assert
    assert "stt_no" in result["data"]["stt"][0]


def test_track_booking(lion_parcel_helper):
    # Arrange
    booking_id = "YOUR BOOKING ID"

    # Act
    result = lion_parcel_helper.track_booking(booking_id)

    # Assert
    assert "current_status" in result["stts"][0]
