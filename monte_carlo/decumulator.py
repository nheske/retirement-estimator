import math
import random
import json


class HistoricalData:

    def __init__(self, year, stocks, bonds, cash, cpi):
        self.year = year
        self.stocks = stocks
        self.bonds = bonds
        self.cash = cash
        self.cpi = cpi


class Inputs:

    def __init__(self, input_vals):
        self.years = input_vals.get('years')
        self.savings = input_vals.get('savings')
        self.withdrawalRate = input_vals.get('withdrawalRate')
        self.stocks = input_vals.get('stocks')
        self.bonds = input_vals.get('bonds')
        self.cash = input_vals.get('cash')


class MonteCarloSim:
    name = "Monte Carlo Simulator"
    historicalData = []
    years = 30
    savings = 1000000
    withdrawalRate = 0.045
    stocks = 0.50
    bonds = 0.30
    cash = 0.20
    input_values = {'years': 30, 'savings': 1000000, 'withdrawalRate': 0.045, 'stocks': 0.50, 'bonds': 0.30, 'cash': 0.20}
    inputs = Inputs(input_values)
    TOTAL_TRIALS = 100000
    MAX_YEARS = 50

    def __init__(self):
        with open('../data/historical.json') as file:
            raw_data_from_json_file = json.load(file)
        historical_list_of_dicts = raw_data_from_json_file["data"]
        historical_data = []
        for y in historical_list_of_dicts:
            some_year_perf = HistoricalData(y.get('years'), y.get('stocks'), y.get('bonds'), y.get('cash'), y.get('cpi'))
            historical_data.append(some_year_perf)
        self.historicalData = historical_data


def simulate():
# savings: 1000000 years: 30 withdrawalRate: 0.045 stocks: 0.5 bonds: 0.3 cash: 0.2 MONTE_CARLO.historicalData = [];
    MONTE_CARLO = MonteCarloSim()
    print(MONTE_CARLO.TOTAL_TRIALS)
    print(MONTE_CARLO.inputs.savings)
    print(len(MONTE_CARLO.historicalData))
    print(MONTE_CARLO.historicalData[1].cpi)
    periods = 0
    averageRateOfReturn =0
    trials = []
    probabilities = []
    results = [[MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings],
           [MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings],
           [MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings]]
    probabilities.append(1)
    initialWithdrawal = MONTE_CARLO.inputs.savings * MONTE_CARLO.inputs.withdrawalRate
    for i in range(1, MONTE_CARLO.MAX_YEARS + 1):
        trials.append([])
        probabilities.append(0)
    for t in range(MONTE_CARLO.TOTAL_TRIALS):
        balance = MONTE_CARLO.inputs.savings
        withdrawal = initialWithdrawal
        for i in range(1, MONTE_CARLO.MAX_YEARS + 1):
            randomYear = math.floor(random.random() * len(MONTE_CARLO.historicalData))
            withdrawal *= (1 + MONTE_CARLO.historicalData[randomYear].cpi)
            if balance < withdrawal:
                balance -= withdrawal
            else:
                arr = 1
                periods += 1
                arr = MONTE_CARLO.historicalData[randomYear].stocks * MONTE_CARLO.inputs.stocks + MONTE_CARLO.historicalData[randomYear].bonds * MONTE_CARLO.inputs.bonds + MONTE_CARLO.historicalData[randomYear].cash * MONTE_CARLO.inputs.cash;
                averageRateOfReturn += arr
                balance = (balance - withdrawal) * (1 + arr)
                probabilities[i] += 1

            # add a small amount of randomness; otherwise, the quickSort will cause recursion errors
            trials.append(balance + random.random() / 100)


if __name__ == '__main__':
    simulate()
    # print("I'm a MonteCarloSim!")
    # MONTE_CARLO = MonteCarloSim()
    # print(MONTE_CARLO.TOTAL_TRIALS)
    # print(MONTE_CARLO.inputs.savings)
    # print(len(MONTE_CARLO.historicalData))
    # print(MONTE_CARLO.historicalData[1].get('cpi'))
