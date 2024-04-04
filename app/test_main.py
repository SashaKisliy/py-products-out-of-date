from unittest import mock
from datetime import date

from app.main import outdated_products


@mock.patch("datetime.date")
def test_outdated_products(mock_date: mock.MagicMock) -> None:
    mock_data = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]
    mock_date.today.return_value = date(2022, 2, 2)

    assert outdated_products(mock_data) == ["duck"]
