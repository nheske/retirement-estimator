import unittest


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_inputs(self):
        inputs = {'years': 30, 'savings': 100000, 'withdrawalRate': 0.45, 'stocks': 0.5, 'bonds': 0.3, 'cash': 0.20}
        print("years = "+str(inputs["years"]))
        print("savings = "+str(inputs["savings"]))
        print("withdrawalRate = "+str(inputs["withdrawalRate"]))
        print("stocks = "+str(inputs["stocks"]))
        print("bonds = "+str(inputs["bonds"]))
        print("cash = "+str(inputs["cash"]))
        # MONTE_CARLO.inputs = {};
        # years = 30;
        # MONTE_CARLO.inputs.savings = 100000;
        # MONTE_CARLO.inputs.withdrawalRate = 0.045;
        # MONTE_CARLO.inputs.stocks = 0.50;
        # MONTE_CARLO.inputs.bonds = 0.30;
        # MONTE_CARLO.inputs.cash = 0.20;


if __name__ == '__main__':
    unittest.main()
