import math
import random
import json
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import statistics


def _format_currency(value):
    return "${:,.2f}".format(value)


def _format_percentage(decimal):
    return ("%0.1f%%" % (decimal * 100.0))


def _calculate_avg_rate_return(final_value, init_value, num_years):
    return (final_value / init_value) ** (1 / num_years) - 1


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
    inputs = None
    TOTAL_TRIALS = 0
    MAX_YEARS = 0

    def __init__(self, values={'years': 30, 'savings': 1000000, 'withdrawalRate': 0.045, 'stocks': 0.50, 'bonds': 0.30, 'cash': 0.20}, num_trials=1000):
        self.inputs = Inputs(values)
        self.TOTAL_TRIALS = num_trials
        self.MAX_YEARS = values["years"]
        with open('data/historical.json') as file:
            raw_data_from_json_file = json.load(file)
        historical_list_of_dicts = raw_data_from_json_file["data"]
        historical_data = []
        for y in historical_list_of_dicts:
            some_year_perf = HistoricalData(y.get('years'), y.get('stocks'), y.get('bonds'), y.get('cash'), y.get('cpi'))
            historical_data.append(some_year_perf)
        self.historicalData = historical_data


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quickSort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

#
# Value formatting functions:
#
def _format_currency(value):
    return "${:,.2f}".format(value)


def _format_percentage(decimal):
    return ("%0.1f%%" % (decimal * 100.0))

def simulate(MONTE_CARLO):
    # savings: 1000000 years: 30 withdrawalRate: 0.045 stocks: 0.5 bonds: 0.3 cash: 0.2 MONTE_CARLO.historicalData = [];
    #     print(MONTE_CARLO.TOTAL_TRIALS)
    #     print(MONTE_CARLO.inputs.savings)
    #     print(len(MONTE_CARLO.historicalData))
    #     print(MONTE_CARLO.historicalData[1].cpi)
    start = time.time()
    periods = 0
    averageRateOfReturn =0
    trials = []  # trials[num_years][num_trials]
    probabilities = []
    # results will be [8][num_years] where 8 represents 97.5%, 87.5%...2.5%, ____
    # results for initial state is starting savings
    results = [[MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings],
           [MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings],
           [MONTE_CARLO.inputs.savings], [MONTE_CARLO.inputs.savings]]
    #probability of survival is 1 for initial state
    probabilities.append(1)
    initial_withdrawal = MONTE_CARLO.inputs.savings * MONTE_CARLO.inputs.withdrawalRate
    # for i in range(1, MONTE_CARLO.MAX_YEARS + 1):
    for some_year in range(1, MONTE_CARLO.MAX_YEARS+1):
        # for the range of total years (e.g. 1 to 50 (as opposed to 0 to 49) have a list in trials ready
        trials.append([])
        probabilities.append(0)
    for some_trial in range(MONTE_CARLO.TOTAL_TRIALS):
        balance = MONTE_CARLO.inputs.savings
        withdrawal = initial_withdrawal
        for some_year in range(1, MONTE_CARLO.MAX_YEARS + 1):
            random_year = math.floor(random.random() * len(MONTE_CARLO.historicalData))
            withdrawal *= (1 + MONTE_CARLO.historicalData[random_year].cpi)
            if balance < withdrawal:
                if(withdrawal > 0):
                    balance = 0
                else:
                    balance -= withdrawal
            else:
                arr = 1
                periods += 1
                arr = MONTE_CARLO.historicalData[random_year].stocks * MONTE_CARLO.inputs.stocks + MONTE_CARLO.historicalData[random_year].bonds * MONTE_CARLO.inputs.bonds + MONTE_CARLO.historicalData[random_year].cash * MONTE_CARLO.inputs.cash;
                averageRateOfReturn += arr
                balance = (balance - withdrawal) * (1 + arr)
                probabilities[some_year-1] += 1
            # add a small amount of randomness; otherwise, the quickSort will cause recursion errors
            trials[some_year-1].append(balance + random.random() / 100)

    i100 = round(MONTE_CARLO.TOTAL_TRIALS)
    i975 = round(MONTE_CARLO.TOTAL_TRIALS * 0.975);
    i875 = round(MONTE_CARLO.TOTAL_TRIALS * 0.875);
    i750 = round(MONTE_CARLO.TOTAL_TRIALS * 0.75);
    i500 = round(MONTE_CARLO.TOTAL_TRIALS * 0.5);
    i250 = round(MONTE_CARLO.TOTAL_TRIALS * 0.25);
    i125 = round(MONTE_CARLO.TOTAL_TRIALS * 0.125);
    i025 = round(MONTE_CARLO.TOTAL_TRIALS * 0.025);

    averageRateOfReturn /= periods

    for some_year in range(0, MONTE_CARLO.MAX_YEARS):
    #for i in range(1, MONTE_CARLO.MAX_YEARS + 1):
        probabilities[some_year] = max(0, min(1, probabilities[some_year] / MONTE_CARLO.TOTAL_TRIALS))
        l = len(trials[some_year])
    # note trials does not have initial value but end of 1st yr, 2nd yr, ...final yr.
    # trials is [ [year1 val1, val2, val3, ... val_trial], [year2 val1, val2, val3, etc.],....,[final year val1, val2, val3, etc.]]
    # trials are sorted such that trial[year_num] is arranged worst to best
    # I dont think you can do this --> because of compounding effects the trial 3 of year 3 should be kept with trial 3 of year 2. what if trial 3 had the best possible yr 1 and yr 2..than it had the best opportunity to be big at end of yr 3..
    # on the other hand maybe its ok because this was a possible outcome of year 3 and the sorting is just for probabilities and not for stringing together the sample lifetime
        quickSort(trials[some_year], 0, l - 1)
        # After the trials are sorted, get the 97.5% best result, 87.5% best result, etc. and save these for plotting.
        # get the 97.5% best return among all the trials for some_year
        results[0].append(round(trials[some_year][i975]))
        results[1].append(round(trials[some_year][i875]))
        results[2].append(round(trials[some_year][i750]))
        results[3].append(round(trials[some_year][i500]))
        results[4].append(round(trials[some_year][i250]))
        results[5].append(round(trials[some_year][i125]))
        results[6].append(round(trials[some_year][i025]))
    #This saves results for plotting of the target years (e.g. 30 of 50)
    index = min(l - 1, round(MONTE_CARLO.TOTAL_TRIALS * (1 - probabilities[MONTE_CARLO.inputs.years])));
    for some_year in range(0, MONTE_CARLO.MAX_YEARS):
    #for i in range(1, MONTE_CARLO.MAX_YEARS + 1):
        results[7].append(round(trials[some_year][index]))

    final_outcomes = trials[MONTE_CARLO.inputs.years - 1]
    mean_final_outcome = statistics.mean(final_outcomes)
    std_dev_final_outcome = statistics.stdev(final_outcomes)
    worst_outcome = np.min(final_outcomes)
    best_outcome = np.max(final_outcomes)
    p100 = np.percentile(final_outcomes, 10, interpolation='nearest')
    p250 = np.percentile(final_outcomes, 25, interpolation='nearest')
    median_outcome = np.median(final_outcomes)
    p750 = np.percentile(final_outcomes, 75, interpolation='nearest')
    p900 = np.percentile(final_outcomes, 90, interpolation='nearest')

    print("Monte Carlo results")

    strn = "\n------------------------------------------------------\n"
    strn += "Initial value:      " + _format_currency(MONTE_CARLO.inputs.savings) + "\n"
    strn += "Withdrawal Rate:    " + str(MONTE_CARLO.inputs.withdrawalRate) + "\n"
    strn += "Num runs:           " + str(MONTE_CARLO.TOTAL_TRIALS) + "\n"
    strn += "Num Years:          " + str(MONTE_CARLO.inputs.years) + " years\n"
    strn += "Stocks/Bonds/Cash:  " + str(MONTE_CARLO.inputs.stocks) +"/"+ str(MONTE_CARLO.inputs.bonds) +"/"+ str(MONTE_CARLO.inputs.cash)+ "\n"
    strn += "Duration:           " + str(MONTE_CARLO.inputs.years) + " years\n"

    strn += "Calculation Time:   " + str((time.time() - start)) + "\n"
    strn += "\n"
    strn += "Mean outcome:       " + _format_currency(mean_final_outcome) + "\n"
    strn += "Std Dev:            " + _format_currency(std_dev_final_outcome) + "\n"
    strn += "Avg rate of return: " + _format_percentage(averageRateOfReturn) + "\n"
    strn += "68–95–99.7 rule \n"
    # strn += "1 sigma runs        " + _format_percentage(one_sigma) + "\n"
    # strn += "2 sigma runs        " + _format_percentage(two_sigma) + "\n"
    # strn += "3 sigma runs        " + _format_percentage(three_sigma) + "\n"
    # strn += "\n"
    # strn += "Median final outcome:" + _format_currency(self.median_final_outcome) + "\n"
    # # strn += "  MAD:       " + _format_currency(astropy.stats.median_absolute_deviation(self.values)) + "\n"
    strn += "Worst outcome:      " + _format_currency(worst_outcome) + "\n"
    strn += "10% outcome:        " + _format_currency(p100) + "\n"
    strn += "25% outcome:        " + _format_currency(p250) + "\n"
    strn += "Median outcome:     " + _format_currency(median_outcome) + "\n"
    strn += "75% outcome:        " + _format_currency(p750) + "\n"
    strn += "90% outcome:        " + _format_currency(p900) + "\n"
    strn += "Best outcome:       " + _format_currency(best_outcome) + "\n"

    print(strn)



    # print("json_results_i975" + json.dumps(results[0]))
    # print("json_results_i875" + json.dumps(results[1]))
    # print("json_results_i750" + json.dumps(results[2]))
    # print("json_results_i500" + json.dumps(results[3]))
    # print("json_results_i250" + json.dumps(results[4]))
    # print("json_results_i125" + json.dumps(results[5]))
    # print("json_results_i025" + json.dumps(results[6]))
    # print("probabilities len=" + str(len(probabilities)))
    # json_probabilities = json.dumps(probabilities)
    # print(json_probabilities)          # ["1", "2", "3"]
    # print(type(json_probabilities))    # <class 'str'>

    num = MONTE_CARLO.inputs.years + 1
    y97_5 = np.array(results[0][:num])
    y87_5 = np.array(results[1][:num])
    y75 = np.array(results[2][:num])
    y25 = np.array(results[4][:num])
    y12_5 = np.array(results[5][:num])
    y2_5 = np.array(results[6][:num])
    year_num = np.arange(0, MONTE_CARLO.MAX_YEARS + 1, 1)
    year_num = np.arange(0, num, 1)

#plot
    f = plt.figure()
    figure = f
    # Plot data:
    plt.figure(figure.number)
    plt.rcParams['axes.xmargin'] = 0
    plt.margins(x=0)
    plt.margins(y=0)
    ax = plt.gca()
    #fmt = '$%.0f'
    fmt = '${x:,.0f}'
    #tick = mtick.FormatStrFormatter(fmt)
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
#    ax.yaxis.grid() '''horiz grid only'''
    plt.grid(True)
    plt.ylim([0, 3*MONTE_CARLO.inputs.savings])

#    plt.ticklabel_format(style='plain', axis='y', scilimits=(0, 6))
    dark = '#44697d'  # 68 105 125
    med = '#007db3'  # 0 125 179
    light = '#409ec6'  # 64 158 198
    plt.fill_between(year_num, y97_5, y87_5, color=light, label="95% likelihood")
    plt.fill_between(year_num, y87_5, y75, color=med, label="75%")
    plt.fill_between(year_num, y75, y25, color=dark, label="50%")
    plt.fill_between(year_num, y25, y12_5,  color=med)
    plt.fill_between(year_num, y12_5, y2_5, color=light)
    plt.xlabel('year')
    plt.yticks(rotation=25)
    plt.ylabel('Portfolio Value ($M)')
    plt.yticks(fontsize=6)
    plt.title('Portfolio Value Over Time')
    plt.legend()
    plt.show()

#stocker style plot
    # color='steelblue'
    # label="Value"
    # plt.plot(data, lw=1, color=color, label=label + ' (' + _format_currency(self.history[-1].value()) + ')')
    # plt.plot(data, lw=1, color=color, label=label + ' (' + _format_currency(self.history[-1].value()) + ')')
    # plt.fill_between(year_num, y97_5, y87_5, color=light, label="95% likelihood")
    # plt.fill_between(year_num, y87_5, y75, color=med, label="75%")
    # plt.fill_between(year_num, y75, y25, color=dark, label="50%")
    # plt.fill_between(year_num, y25, y12_5, color=med)
    # plt.fill_between(year_num, y12_5, y2_5, color=light)
    # plt.fill_between(list(range(len(data))), data, interpolate=False, facecolor=color, alpha=0.5)
    # plt.ylim(bottom=0.0)
    # plt.xlim(0, len(data) - 1)
    # plt.xlabel('Year')
    # plt.ylabel('Portfolio Value ($M)')
    # plt.title('Portfolio Value Over Time')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

# save results, probabilities, arr
    # SELF.postMessage({
    #     msg: "SIMULATION COMPLETE",
    #     results: results,
    #     probabilities: probabilities,
    #     averageRateOfReturn: averageRateOfReturn,
    #     simulationRetirementYears: MONTE_CARLO.inputs.years,
    #     elapsed: ((new Date()).getTime() - startTime)
    # });

if __name__ == '__main__':
    input_values = {'years': 30, 'savings': 1000000, 'withdrawalRate': 0.04, 'stocks': 0.5, 'bonds': 0.5, 'cash': 0.0}
    MONTE_CARLO = MonteCarloSim(input_values, num_trials=100)
    simulate(MONTE_CARLO)
    # print("I'm a MonteCarloSim!")
    # MONTE_CARLO = MonteCarloSim()
    # print(MONTE_CARLO.TOTAL_TRIALS)
    # print(MONTE_CARLO.inputs.savings)
    # print(len(MONTE_CARLO.historicalData))
    # print(MONTE_CARLO.historicalData[1].get('cpi'))
