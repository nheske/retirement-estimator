import sys
import random
import matplotlib.pyplot as plt
import statistics

def read_to_list(file_name):
    """Open a file of data in percent, convert to decimal and return a list"""
    with open("data/"+file_name) as in_file:
        lines = [float(line.strip()) for line in in_file]
        decimal = [round(line/100,5) for line in lines]
        return decimal

def default_input(prompt, default=None):
    """Allow use of default values in input."""
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response


print("\nNote: Input data should be in percent, not decimal!\n")
try:
    bonds = read_to_list('10-yr_TBond_returns_1926-2013_pct.txt')
    stocks = read_to_list('SP500_returns_1926-2013_pct.txt')
    blend_40_50_10 = read_to_list('S-B-C_blend_1926-2013_pct.txt')
    blend_50_50 = read_to_list('S-B_blend_1926-2013_pct.txt')
    infl_rate = read_to_list('annual_infl_rate_1926-2013_pct.txt')
except IOError as e:
    print("{}, \nTerminating program.".format(e), file=sys.stderr)
    sys.exit(1)
investment_type_args = {'bonds': bonds, 'stocks': stocks, 'sb_blend': blend_50_50, 'sbc_blend': blend_40_50_10}

print("   stocks = SP500")
print("    bonds = 10-yr Treasury Bond")
print(" sb_blend = 50% SP500/50% TBond")
print("sbc_blend = 40% SP500/50% TBond/10% Cash\n")

print("Press ENTER to take default value shown in [brackets]. \n")

auto = True
if auto:
    invest_type = 'sbc_blend'
    start_value = 2000000
    withdrawal = 80000
    min_years = 10
    most_likely_years = 20
    max_years = 40
    total_runs = 50000
else:
    invest_type = default_input("Enter investment number 1. SP500 stocks , 2. 10-yr Treasury Bond, 3. 50% SP500/50% TBond,  4. 40% SP500/50% TBond/10% Cash (default): \n", '4').lower()
    while invest_type not in investment_type_args:
        if invest_type == '1':
          invest_type = 'stocks'
        elif invest_type == '2':
          invest_type = 'bonds'
        elif invest_type == '3':
          invest_type = 'sb_blend'
        elif invest_type == '4':
          invest_type = 'sbc_blend'
        else:
          invest_type = input("Invalid investment. Enter investment type " \
                            "as listed in prompt: ")
    print(invest_type + " chosen")
    start_value = default_input("Input starting value of investments: [2000000]\n", '2000000')
    while not start_value.isdigit():
        start_value = input("Invalid input! Input integer only: ")

    withdrawal = int(default_input("Input annual pre-tax withdrawal  (today's dollars): [$80000] \n", '80000'))
    min_years = int(default_input("Input minimum years in retirement: [5] \n", '5'))
    most_likely_years = int(default_input("Input most-likely years in retirement: [10] \n",'10'))
    max_years = int(default_input("Input maximum years in retirement: [20] \n", '20'))
    total_runs = int(default_input("Input number of cases to run: [5000]\n", '5000'))
    while not total_runs.isdigit():
        total_runs = input("Invalid input! Input integer only: ")

    if not int(min_years) < int(most_likely_years) < int(max_years)  or int(max_years) > 99:
        print("\nProblem with input years.", file=sys.stderr)
        print("Requires Min < ML < Max & Max <= 99.", file=sys.stderr)
        sys.exit(1)


def monte_carlo(returns):
    lifetime_runs_counter = 0
    bankrupt_counter = 0
    lifetime_final_assets = []

    while lifetime_runs_counter < total_runs:
        assets_year_end = []
        assets_value = start_value
        start_year = random.randrange(0, len(returns))
        duration = round(random.triangular(min_years, max_years, most_likely_years))
        end_year = start_year + duration
        lifespan = [i for i in range(start_year, end_year)]
        bankrupt = 'no'

        #build temporary lists for each case
        lifespan_returns = []
        lifespan_infl = []
        for i in lifespan:
            lifespan_returns.append(returns[i % len(returns)])
            lifespan_infl.append(infl_rate[i % len(infl_rate)])

        # loop through each year of retirement for each case run
        for index, i in enumerate(lifespan_returns):
            infl = lifespan_infl[index]

            # don't adjust for inflation first year
            if index == 0:
                withdraw_infl_adj = withdrawal
            else:
                withdraw_infl_adj = int(withdraw_infl_adj * (1 + infl))
            assets_value -= withdraw_infl_adj
            assets_value = int(assets_value * (1 + i))
            assets_year_end.append(assets_value)
            if assets_value <= 0:
                bankrupt = 'yes'
                break
        if bankrupt == 'yes':
            lifetime_final_assets.append(0)
            bankrupt_counter += 1
        else:
            lifetime_final_assets.append(assets_value)
            if assets_value == max(i for i in lifetime_final_assets):
              print("best outcome so far with ${:,.2f}".format(assets_value) +" in case: "+str(lifetime_runs_counter) + " over " + str(duration) + " years")
 #             print(*assets_year_end)
              # Annualized Return Formula when given the annual returns for each year of the investment period:
              # ar = ( ( (1+R1)*(1+R2)*(1+R3)...*(1+Rn) )(1/n) -1) * 100)
              product = 1
              for r in lifespan_returns:
                  product *= (1 + r)
              annual_return = (product ** (1 / len(lifespan_returns)) - 1) * 100
              print("annualized return = "+str(round(annual_return, 1)) +"%")
        lifetime_runs_counter += 1
    return lifetime_final_assets, bankrupt_counter

def bankrupt_prob(outcome, bankrupt_count):
    """Calculate and return chance of running out of money & other stats."""
    total = len(outcome)
    odds = round(100 * bankrupt_count / total, 1)

    print("\nInvestment type: {}".format(invest_type))
    print("Starting value: ${:,}".format(int(start_value)))
    print("Annual withdrawal: ${:,}".format(int(withdrawal)))
    print("Years in retirement (min-ml-max): {}-{}-{}"
          .format(min_years, most_likely_years, max_years))
    print("Number of runs: {:,}\n".format(len(outcome)))
    print("Odds of running out of money: {}%\n".format(odds))
    print("Mean outcome: ${:,}".format(int(sum(outcome) / total)))
    print("Median outcome:  ${:,}".format(int(statistics.median(outcome))))
    print("Minimum outcome: ${:,}".format(min(i for i in outcome)))
    print("Maximum outcome: ${:,}".format(max(i for i in outcome)))

#TODO calculate annualized return
#TODO portfolio risk using variance and standard deviations https://codingandfun.com/portfolio-risk-and-returns-python/
#TODO apply Modern Portfolio Theory https://medium.com/analytics-vidhya/constructing-a-killer-investment-portfolio-with-python-51f4f0d344be

    return odds

def main():
    """ Call MCS and bankrupt functions and draw bar chart of results."""
    outcome, bankrupt_count = monte_carlo(investment_type_args[invest_type])
    odds = bankrupt_prob(outcome, bankrupt_count)

    # generate matplotlib bar chart
    plotdata = outcome[:3000]  # only plot first 3000 runs
    plt.figure('Outcome by Case (showing first {} runs)'.format(len(plotdata)),
               figsize=(16, 5))  # size is width, height in inches
    index = [i + 1 for i in range(len(plotdata))]
    plt.bar(index, plotdata, color='black')
    plt.xlabel('Simulated Lives', fontsize=18)
    plt.ylabel('$ Remaining', fontsize=18)
    plt.ticklabel_format(style='plain', axis='y')
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}"
                                                         .format(int(x))))
    plt.title('Probability of running out of money = {}%'.format(odds),
              fontsize=20, color='red')
    plt.show()


# run program
if __name__ == '__main__':
    main()