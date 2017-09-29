import finsymbols
from yahoo_finance import Share
from coinmarketcap import Market
import tweepy
import urllib2
import time
import sys

CONSUMER_KEY = 'These'
CONSUMER_SECRET = 'Are'
ACCESS_KEY = 'Secret'
ACCESS_SECRET = '.'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    coinmarketcap = Market()
    e = coinmarketcap.ticker('ethereum')
    ethcap = float(e[0]['market_cap_usd'])/1000000000 # pulls and formats eth market cap data
    eth = "The market cap of #ETH is $" + str(round(ethcap, 1)) + "B. " # prep for bot
    emarket_caps = dict()
    sp500 = finsymbols.get_sp500_symbols()
    for d in sp500:
        try:
            ticker = d['symbol'] # pulls ticker from dictionary
            print ticker
            yahoodata = Share(ticker)
            yahformat = yahoodata.get_market_cap() # pulls market cap data from yahoo
            print yahformat
            if yahformat is not None: # some market caps are none
                emarket_caps[ticker] = (float(filter(lambda x: x.isdigit(), yahformat)))/100 # formats market caps and takes out B
            elif yahformat is None: # if none, market cap is just 0
                emarket_caps[ticker] = 0
        except urllib2.HTTPError, e:
            time.sleep(601)
            yahoodata = Share(ticker)
            yahformat = yahoodata.get_market_cap() # pulls market cap data from yahoo
            print yahformat
            if yahformat is not None: # some market caps are none
                emarket_caps[ticker] = (float(filter(lambda x: x.isdigit(), yahformat)))/100 # formats market caps and takes out B
            elif yahformat is None: # if none, market cap is just 0
                emarket_caps[ticker] = 0
    emarket_caps["Ethereum"] = ethcap # adds Ethereum's market cap to dictionary
    below_stack = ((t, c) for t, c in emarket_caps.items() if c < emarket_caps['Ethereum'])
    next_cap = max(below_stack, key=lambda item: item[1])
    nextlargest = next_cap[0]
    othercompany = "If #ethereum was a company in the S&P 500, the next largest company would be "
    completetweet = str(eth + othercompany + "$" + nextlargest + ". #cryptocapcomps")
    api.update_status(completetweet)
    time.sleep(86400)
