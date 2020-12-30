import unittest
import monte_carlo.MonteCarlo as mc


class MonteCarloTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_monte_carlo(self):
        inputs = {'years': 30, 'savings': 100000, 'withdrawalRate': 0.45, 'stocks': 0.5, 'bonds': 0.3, 'cash': 0.20, 'total_trials' : 1000}
        print("years = "+str(inputs["years"]))
        print("savings = "+str(inputs["savings"]))
        print("withdrawalRate = "+str(inputs["withdrawalRate"]))
        print("stocks = "+str(inputs["stocks"]))
        print("bonds = "+str(inputs["bonds"]))
        print("cash = "+str(inputs["cash"]))
        monte_carlo = mc.MonteCarlo('a', inputs)
        print(monte_carlo.name)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()