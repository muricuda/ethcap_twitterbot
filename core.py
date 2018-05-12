import finsymbols
#from yahoo_finance import Share
from iexfinance import Stock
from coinmarketcap import Market
import urllib3
import tweepy
import time
import sys
import datetime

CONSUMER_KEY = 'these'
CONSUMER_SECRET = 'are'
ACCESS_KEY = 'secret'
ACCESS_SECRET = '.'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:

    coinmarketcap = Market()

    e = coinmarketcap.ticker('ethereum')
    ethcap = float(e[0]['market_cap_usd'])/1000000000 # pulls and formats eth market cap data
    eth = "The market cap of $ETH is $" + str(round(ethcap, 1)) + "B. "  # prep for bot

    b = coinmarketcap.ticker('bitcoin')
    bitcap = float(b[0]['market_cap_usd'])/1000000000
    bitcoin = "The market cap of $BTC is $" + str(round(bitcap, 1)) + "B. " # prep for bot

    l = coinmarketcap.ticker('litecoin')
    litecap = float(l[0]['market_cap_usd']) / 1000000000
    litecoin = "The market cap of $LTC is $" + str(round(litecap, 1)) + "B. "  # prep for bot

    bc = coinmarketcap.ticker('bitcoin-cash')
    bchcap = float(bc[0]['market_cap_usd']) / 1000000000
    bch = "The market cap of $BCH is $" + str(round(bchcap, 1)) + "B. "  # prep for bot

    emarket_caps = dict()
    sp500 = finsymbols.get_sp500_symbols()
    for d in sp500:
        try:
            ticker = d['symbol'] # pulls ticker from dictionary
            print (ticker)
            yahoodata = Stock(ticker)
            yahformat = yahoodata.get_market_cap() # pulls market cap data from yahoo
            print (yahformat)
            if yahformat is not None: # some market caps are none
                emarket_caps[ticker] = yahformat/1000000000 # formats market caps and takes out B
            elif yahformat is None: # if none, market cap is just 0
                emarket_caps[ticker] = 0
        except urllib3:
            print ("The time is: ")
            print (datetime.datetime.now())
            for i in xrange(61, 0, -1):
                time.sleep(10)
                sys.stdout.write(str(i) + ' ')
                sys.stdout.flush()
            yahoodata = Share(ticker)
            yahformat = yahoodata.get_market_cap() # pulls market cap data from yahoo
            print (yahformat)
            if yahformat is not None: # some market caps are none
                emarket_caps[ticker] = yahformat/1000000000 # formats market caps and takes out B
            elif yahformat is None: # if none, market cap is just 0
                emarket_caps[ticker] = 0
        except urllib3:
            time.sleep(3)
            yahoodata = Share(ticker)
            yahformat = yahoodata.get_market_cap()  # pulls market cap data from yahoo
            print (yahformat)
            if yahformat is not None:  # some market caps are none
                emarket_caps[ticker] = yahformat/1000000000  # formats market caps and takes out B
            elif yahformat is None:  # if none, market cap is just 0
                emarket_caps[ticker] = 0

    emarket_caps["Ethereum"] = ethcap # adds Ethereum's market cap to dictionary
    below_stack_eth = ((t, c) for t, c in emarket_caps.items() if c < emarket_caps['Ethereum'])
    next_cap_eth = max(below_stack_eth, key=lambda item: item[1])
    nextlargest_eth = next_cap_eth[0]
    othercompany_eth = "If #Ethereum was a company in the S&P 500, the next largest company would be "
    completetweet_eth = str(eth + othercompany_eth + "$" + nextlargest_eth + ". #cryptocapcomps")
    api.update_status(completetweet_eth)

    emarket_caps["Bitcoin"] = bitcap
    below_stack_bit = ((t, c) for t, c in emarket_caps.items() if c < emarket_caps['Bitcoin'])
    next_cap_bit = max(below_stack_bit, key=lambda item: item[1])
    nextlargest_bit = next_cap_bit[0]
    othercompany_bit = "If #Bitcoin was a company in the S&P 500, the next largest company would be "
    completetweet_bit = str(bitcoin + othercompany_bit + "$" + nextlargest_bit + ". #cryptocapcomps")
    api.update_status(completetweet_bit)

    emarket_caps["Litecoin"] = litecap
    below_stack_lite = ((t, c) for t, c in emarket_caps.items() if c < emarket_caps['Litecoin'])
    next_cap_lite = max(below_stack_lite, key=lambda item: item[1])
    nextlargest_lite = next_cap_lite[0]
    othercompany_lite = "If #Litecoin was a company in the S&P 500, the next largest company would be "
    completetweet_lite = str(litecoin + othercompany_lite + "$" + nextlargest_lite + ". #cryptocapcomps")
    api.update_status(completetweet_lite)

    emarket_caps["Bitcoin Cash"] = bchcap
    below_stack_bch = ((t, c) for t, c in emarket_caps.items() if c < emarket_caps['Bitcoin Cash'])
    next_cap_bch = max(below_stack_bch, key=lambda item: item[1])
    nextlargest_bch = next_cap_bch[0]
    othercompany_bch = "If #BitcoinCash was a company in the S&P 500, the next largest company would be "
    completetweet_bch = str(bch + othercompany_bch + "$" + nextlargest_bch + ". #cryptocapcomps")
    api.update_status(completetweet_bch)

    print ("Tweets were tweeted. They say: ")
    print (completetweet_bit)
    print (completetweet_eth)
    print (completetweet_lite)
    print (completetweet_bch)
    print ("The time is: ")
    print (datetime.datetime.now())
    print ("Minutes left until next tweet:")
    for i in range(1440, 0, -1):
        time.sleep(60)
        sys.stdout.write(str(i) + ' ')
        sys.stdout.flush()
