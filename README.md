# cryptfolio

This is a script that will calculate your crypto portfolio's current amount and net value based upon two things:

How many of each coin do you have, and how much (in $USD) did you pay for those coins.

It then goes out to coinmarketcap.com's API, grabs the current price for what you have in your portfolio settings file, then multiplies that by the number of the coin you have, and subtracts the amount you paid for those coins to give you a current total of what your portfolio of coins is worth and your profit/loss.

As an example, using the included demo portfolio_details.yml settings file, you would see output like this:

lothlorien:cryptfolio gloria.silveira$ python ./cryptfolio.py
======================================================================
                       Portfolio Value                                
======================================================================
       Total Amount    Current Price    Current USD Value    Profit/Loss
---  --------------  ---------------  -------------------  -------------
BTC               2         9591.35             19182.7        18682.7
ETH               5          726.161             3630.8         3430.8
LTC               5          187.377              936.885        736.885
======================================================================
Total Gross Value: $23750.39
Total Net Value: $23050.39
 

