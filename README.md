# retirement-estimator
Initially based on the book Impractical Python Projects chapter 12: Net Egg Calculator

## Methodology
- Method 1: As used in book, from an 88 year of historical data, randomly choose a start year within the history and proceed through subsequent historical years.
- Method 2: As used by Vanguard's Nest Egg calculator, each year is randomly chosen with replacement. So, one lifetime could have 1931, 1931, 2001, 2008, 2008, 2001, etc. 

## TODOs
- calculate annualized returns
  - https://www.buyupside.com/calculators/annualizedreturn.htm

- Risk
  - Sharpe Ratio
  - portfolio risk using variance and standard deviations 
  - https://codingandfun.com/portfolio-risk-and-returns-python/
  - apply Modern Portfolio Theory 
  - https://medium.com/analytics-vidhya/constructing-a-killer-investment-portfolio-with-python-51f4f0d344be
- Graphs
  - Make graphs like vanguard
  - https://retirementplans.vanguard.com/VGApp/pe/pubeducation/calculators/RetirementNestEggCalc.jsf
  - https://python-graph-gallery.com/254-pandas-stacked-area-chart/
- Potential Data Sorces S&P returns 
    - Vanguard historical from their nest egg calculator
    - S&P Returns from [Slick Charts](https://www.slickcharts.com/sp500/returns)
    - Equity Labs backtest data(https://www.equitieslab.com/)
- OOP
- Introduce
  - explain at meetup https://www.meetup.com/pythonsd/events/wxfkzrybcqbgc/  5-7 minute lightning talks : http://pysd.io/talk

Methods
*Vanguard formula*

According to [NewJobPFThrowaway on financialindependence Reddit](https://www.reddit.com/r/financialindependence/comments/d6wl6q/why_is_the_vanguard_retirement_nest_egg/)

Vanguard's nest egg simulation is driven by 90 years of historical actual returns data. The actual config file used by the simulation is [here](https://retirementplans.vanguard.com//web/angular/app/nesteggcalculator/data/config.json).

Here's a brief explanation of their code:

For each year (do this N times, where N is the # years chosen):
- Pick a random year from the list of 90
- Increase/Decrease expenses by CPI for that year, set the new expenses value
- Withdraw the new expenses value from the balance
- Factor in returns (weighted by fund allocation) from that year, and update the new balance
- Repeat.

This appears to be a basic, functional, Monte Carlo simulation.

The reason it has more failures is because it's possible to get multiple 1931s in a row (-43% stocks), or some other combination of bad years in a streak (1931, 1973, 1974, 2000, 2008). They're not picking one starting year and moving forward, so there's no "cyclical nature" to their simulation. Two of those catastrophic years in a row will sink almost any FIRE plan.


