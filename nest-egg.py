import sys
import random
import matplotlib.pyplot as plt

def read_to_list(file_name):
    """Open a file of data in percent, convert to decimal and return a list"""
    with open("data\\"+file_name) as in_file:
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


values = read_to_list("3_mo_TBill_rate_1926-2013_pct.txt")
print(len(values))
print("\nNothe: Input data should be in percent, not decimal!\n")
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

invest_type = default_input("Enter investment type: (stocks, bonds, sb_blend,  sbc_blend): \n", 'bonds').lower()
while invest_type not in investment_type_args:
    invest_type = input("Invalid investment. Enter investment type " \
                        "as listed in prompt: ")

start_value = default_input("Input starting value of investments: \n", '2000000')
while not start_value.isdigit():
    start_value = input("Invalid input! Input integer only: ")

withdrawal = default_input("Input annual pre-tax withdrawal  (today's $): \n", '80000')
while not withdrawal.isdigit():
    withdrawal = input("Invalid input! Input integer only: ")
min_years = default_input("Input minimum years in retirement: \n", '18')
while not min_years.isdigit():
    min_years = input("Invalid input! Input integer only: ")

most_likely_years = default_input("Input most-likely years in retirement: \n",
                                  '25')
while not most_likely_years.isdigit():
    most_likely_years = input("Invalid input! Input integer only: ")

max_years = default_input("Input maximum years in retirement: \n", '40')
while not max_years.isdigit():
    max_years = input("Invalid input! Input integer only: ")

num_cases = default_input("Input number of cases to run: \n", '50000')
while not num_cases.isdigit():
    num_cases = input("Invalid input! Input integer only: "

if not int(min_years) < int(most_likely_years) < int(max_years) or int(max_years) > 99:
    print("\nProblem with input years.", file=sys.stderr)
    print("Requires Min < ML < Max with M")

