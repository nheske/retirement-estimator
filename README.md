# retirement-estimator
Initially based on the book Impractical Python Projects chapter 12: Net Egg Calculator

## Modeling Retirement With Monte Carlo Simulations
* Forecast models: (e.g.  [simulation models described here](https://www.portfoliovisualizer.com/monte-carlo-simulation) )
    * Method 1: Forecast based on historical data
        * As used in book, from 88 year historical data, randomly choose start year and process block of years with circular bootstrapping. No rebalancing. Historical inflation.
        * As used by Vanguard's Nest Egg calculator, each year is randomly chosen with replacement. So, one could theoretically have the bad luck of 1931, 1931, 2001, 2008, 2008, 2001, etc. 
    * Method 2: Forecast based on mean and standard deviation of asset performance
    * Method 3: Forecast based on mean, volatility and correlations of portfolios assets
    * Method 4: Forecast based on expected return and volatility
* Examples:    
    * [Vanguard's Nest Egg Calculator](https://retirementplans.vanguard.com/VGApp/pe/pubeducation/calculators/RetirementNestEggCalc.jsf)
    * FIRE(Financial independence Retirement Estimator)
        * [Engaging FIRE calculator](https://engaging-data.com/fire-calculator/)
        * [cFIREsim](https://www.cfiresim.com/)
        * [cFIREsim-open source](https://github.com/boknows/cFIREsim-open)
    * [Portfolio Visualizer](https://www.portfoliovisualizer.com/monte-carlo-simulation)
    * [The Flexible Retirement Planner (Java)](https://www.flexibleretirementplanner.com/wp/)
    * [retirement-mc (Python)](https://github.com/jhykes/retirement-mc)
        * use Schiller CPI, stock perform, int rates http://www.econ.yale.edu/~shiller/data/chapt26.xlsx
        * use CDC life expectancy http://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/60_09/

## Dependencies
   * matplotlib, pandas
   
## TODOs
* OOP
* Tests
* Calculate annualized returns
  * [buyupside annualized return calculator](https://www.buyupside.com/calculators/annualizedreturn.htm)
* Graphs
  * Make graphs like vanguard
  * https://retirementplans.vanguard.com/VGApp/pe/pubeducation/calculators/RetirementNestEggCalc.jsf
  * https://python-graph-gallery.com/254-pandas-stacked-area-chart/
* Numpy
* scipy
* Introduce
  * explain at meetup https://www.meetup.com/pythonsd/events/wxfkzrybcqbgc/  5-7 minute lightning talks : http://pysd.io/talk  
## Other Considerations
####  Risk
  * Sharpe Ratio
  * portfolio risk using variance and standard deviations 
  * https://codingandfun.com/portfolio-risk-and-returns-python/
  * apply Modern Portfolio Theory 
  * https://medium.com/analytics-vidhya/constructing-a-killer-investment-portfolio-with-python-51f4f0d344be
#### Investment Strategies
   * Lazy Portfolios:  https://www.bogleheads.org/wiki/Lazy_portfolio
      * Bogleheads Two fund portfolio 60%	Vanguard Total World Stock Index Fund/40%	Vanguard Total Bond Market Index Fund
      * Scott Burns' Couch Potato portfolio / Andrew Tobias' Three Fund portfolio 33% Vanguard Inflation-Protected Securities Fund/34% Total US Stock/33% Total Int'l
      * David Swensen's lazy portfolio Total Stock Mkt 30%/Intl Developed Mkt	15%/Emerging Markets	10%/Real Estate 15%/US Treasury Bonds	15%/TIPS	15%
  * dividend investing
    * https://www.mrfreeat33.com/
    * Right now, Vanguard's High Dividend Yield index ETF VYM's trailing 4 quarters' dividends divided by its price = 3.1%. Current portfolio is 400 companies.
    * International High Dividend ETF VYMI yield is 4.3%. - from a portfolio of 1,000 companies.
    * tax disadvantage As an example, let's say the s&p 500 gets a 8% return (before inflation) from price growth and has a 2% dividend yield over that time for a 10% total return. Let's say you pay a 15% tax on the dividends, so your total return was 2*0.85 + 8 or 9.7%. Then let's say another person had a portfolio with a dividend yield of 3% but a growth rate of only 7%. Then that person would have a total return of 3*0.85+7 = 9.55%. Of course all that assumes you invest in a taxable account. If you're in a tax protected account (401k, IRA, etc...) then you still get the tax shield of those accounts 
  * portfolio rebalancing https://github.com/williamgilpin/portbalance
* Candidate Historical Data Sources  
    * S&P returns 
        * Vanguard historical from their nest egg calculator
        * S&P Returns from [Slick Charts](https://www.slickcharts.com/sp500/returns)
        * Equity Labs backtest data(https://www.equitieslab.com/)
    * [Robert Shiller/data](hhttp://www.econ.yale.edu/~shiller/data.htm)
        * [US Home Prices 1890-Present](http://www.econ.yale.edu/~shiller/data.htm)
    * [pages.stern.nyu.edu/~adamodar](http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html)
    * [MoneyChimp CAGR history](http://www.moneychimp.com/features/market_cagr.htm)
    * [Historical Inflation Rates: 1914-2020](https://www.usinflationcalculator.com/inflation/historical-inflation-rates/)
    * [Historical Annual U.S. Inflation Rate from 1913 to the present](https://inflationdata.com/Inflation/Inflation_Rate/HistoricalInflation.aspx)
#### Additional Tools
* https://github.com/Gregable/social-security-tools
* SS Strategy https://github.com/MikePiper/open-social-security
* [FIRE on Reddit](https://www.reddit.com/r/financialindependence/)
* [FatFIRE](https://www.reddit.com/r/fatFIRE/)


##### Notes on Vanguard's tool/formula
According to [NewJobPFThrowaway on financialindependence Reddit](https://www.reddit.com/r/financialindependence/comments/d6wl6q/why_is_the_vanguard_retirement_nest_egg/)

>Vanguard's nest egg simulation is driven by 90 years of historical actual returns data. The actual config file used by the simulation is [here](https://retirementplans.vanguard.com//web/angular/app/nesteggcalculator/data/config.json).
Here's a brief explanation of their code:
For each year (do this N times, where N is the # years chosen):
>- Pick a random year from the list of 90
>- Increase/Decrease expenses by CPI for that year, set the new expenses value
>- Withdraw the new expenses value from the balance
>- Factor in returns (weighted by fund allocation) from that year, and update the new balance
>- Repeat.
>This appears to be a basic, functional, Monte Carlo simulation.
>The reason it has more failures is because it's possible to get multiple 1931s in a row (-43% stocks), or some other combination of bad years in a streak (1931, 1973, 1974, 2000, 2008). They're not picking one starting year and moving forward, so there's no "cyclical nature" to their simulation. Two of those catastrophic years in a row will sink almost any FIRE plan.


