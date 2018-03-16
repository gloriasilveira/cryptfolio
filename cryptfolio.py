#!/usr/bin/env python

import yaml
import requests
import json
from tabulate import tabulate

# Step 1: Grab Portfolio Details
################################

config = yaml.safe_load(open("portfolio_details.yml"))

#BTC
BTC_COUNT = config["Bitcoin"]["BTC_COUNT"]
BTC_USD_SPENT = config["Bitcoin"]["BTC_USD_SPENT"]

# ETH
ETH_COUNT = config["Ethereum"]["ETH_COUNT"]
ETH_USD_SPENT = config["Ethereum"]["ETH_USD_SPENT"]

# LTC
LTC_COUNT = config["Litecoin"]["LTC_COUNT"]
LTC_USD_SPENT = config["Litecoin"]["LTC_USD_SPENT"]

# LEND
LEND_COUNT = config["Ethlend"]["LEND_COUNT"]
LEND_USD_SPENT = config["Ethlend"]["LEND_USD_SPENT"]


# Step 2: Get current coin values
####################################
BTC_response = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
for coin in BTC_response.json():
    btc_current_price = float(coin["price_usd"])

ETH_response = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
for coin in ETH_response.json():
    eth_current_price = float(coin["price_usd"])

LTC_response = requests.get('https://api.coinmarketcap.com/v1/ticker/litecoin/')
for coin in LTC_response.json():
    ltc_current_price = float(coin["price_usd"])

LEND_response = requests.get('https://api.coinmarketcap.com/v1/ticker/ethlend/')
for coin in LEND_response.json():
    lend_current_price = float(coin["price_usd"])


# Step 3: Calculate Total value based on # of coins
###################################################

#BTC
btc_gross_value = BTC_COUNT * btc_current_price
btc_net_value = btc_gross_value - BTC_USD_SPENT


#ETH
eth_gross_value = ETH_COUNT * eth_current_price
#print 'ETH - Total Gross Value: ' + str(eth_gross_value)

eth_net_value = eth_gross_value - ETH_USD_SPENT
#print 'ETH - Total NET Value: $' + str(eth_net_value)


# LTC
ltc_gross_value = LTC_COUNT * ltc_current_price
ltc_net_value = ltc_gross_value - LTC_USD_SPENT

# LEND
lend_gross_value = LEND_COUNT * lend_current_price
lend_net_value = lend_gross_value - LEND_USD_SPENT

# Calculate Portfolio as a whole
port_gross = btc_gross_value + eth_gross_value + ltc_gross_value + lend_gross_value 
port_net = btc_net_value + eth_net_value + ltc_net_value + lend_net_value

# Step 4: Display results to user
##################################

print '======================================================================'
print '                       Portfolio Value                                '
print '======================================================================'

print tabulate([['BTC', BTC_COUNT, btc_current_price, btc_gross_value, btc_net_value], ['ETH', ETH_COUNT, eth_current_price, eth_gross_value, eth_net_value], ['LTC', LTC_COUNT, ltc_current_price, ltc_gross_value, ltc_net_value], ['LEND', LEND_COUNT, lend_current_price, lend_gross_value, lend_net_value]], headers=[' ', 'Total Amount', 'Current Price', 'Current USD Value', 'Profit/Loss'])

print '======================================================================'
print 'Total Gross Value: $' + str(port_gross)
print 'Total Net Value: $' + str(port_net)
print ' '
