import unittest

from gw2apy.client import Client
from gw2apy.endpoints import CommercePrices


class SimpleTest(unittest.TestCase):
    def test_prices_id(self):
        client = Client()
        endpoint = CommercePrices(client=client)
        response = endpoint._endpoint()
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
