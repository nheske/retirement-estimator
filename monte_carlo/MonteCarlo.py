import random


class MonteCarlo:
    name = "Monte Carlo Simulator"
    historicalData = [];

    def __init__(self, name, inputs):
        self.name = name
        self.inputs = inputs
        print("years = " + str(inputs["years"]))
        print("savings = " + str(inputs["savings"]))
        print("withdrawalRate = " + str(inputs["withdrawalRate"]))
        print("stocks = " + str(inputs["stocks"]))
        print("bonds = " + str(inputs["bonds"]))
        print("cash = " + str(inputs["cash"]))
        print("total_trials = " + str(inputs["total_trials"]))


def initialize():
    pass


def simulate():
    pass


def stop():
    pass


def monte_carlo(returns):
    lifetime_runs_counter = 0
    bankrupt_counter = 0
    lifetime_final_assets = []
    earliest_bankruptcy = 1000

    while lifetime_runs_counter < total_runs:
        assets_year_end = []
        assets_value = start_value
        start_year = random.randrange(0, len(returns))
#        duration = round(random.triangular(min_years, max_years, most_likely_years))
        duration = max_years
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
        for year, i in enumerate(lifespan_returns):
            infl = lifespan_infl[year]

            # don't adjust for inflation first year
            if year == 0:
                withdraw_infl_adj = withdrawal
            else:
                withdraw_infl_adj = int(withdraw_infl_adj * (1 + infl))
            assets_value -= withdraw_infl_adj
            assets_value = int(assets_value * (1 + i))
            assets_year_end.append(assets_value)
            if assets_value <= 0:
                bankrupt = 'yes'
                if earliest_bankruptcy > year:
                    earliest_bankruptcy = year
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
    return lifetime_final_assets, bankrupt_counter, earliest_bankruptcy


if __name__ == '__main__':
    input_values = {'years': 30, 'savings': 100000, 'withdrawalRate': 0.45, 'stocks': 0.5, 'bonds': 0.3, 'cash': 0.20, 'total_trials': 1000}
    monteCarlo = MonteCarlo("sim", input_values)
    print("I'm a MonteCarlo!")