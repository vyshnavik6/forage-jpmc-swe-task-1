import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ Assert the calculated price """
    result = getDataPoint(quotes[0])
    expected = ('ABC', 120.48, 121.2, 120.84)
    self.assertEqual(result, expected)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ Assert the calculated price """
    result = getDataPoint(quotes[1])
    expected = ('DEF', 117.87, 121.68, 119.775)
    self.assertEqual(result, expected)

  def test_getRatio(self):
    """ Test the getRatio function """
    price_a = 120.48
    price_b = 121.2
    ratio = getRatio(price_a, price_b)
    expected_ratio = 0.993801652892562
    tolerance = 0.001  # Increase the tolerance
    self.assertAlmostEqual(ratio, expected_ratio, delta=tolerance)


if __name__ == '__main__':
  unittest.main()

