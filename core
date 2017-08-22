import finsymbols
from yahoo_finance import Share
from coinmarketcap import Market
import tweepy
import time

CONSUMER_KEY = 'These'
CONSUMER_SECRET = 'Are'
ACCESS_KEY = 'Very'
ACCESS_SECRET = 'Secret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

coinmarketcap = Market()
e = coinmarketcap.ticker('ethereum')
ethcap = float(e[0]['market_cap_usd'])/1000000000 # pulls and formats eth market cap data

eth = "Ethereum's market cap is $" + str(round(ethcap, 1)) + "B" # prep for bot

sp500 = finsymbols.get_sp500_symbols() # string of api call

emarket_caps = dict() # creates dictionary for S&P market caps

for d in sp500:
    ticker = d['symbol'] # pulls ticker from dictionary
    yahoodata = Share(ticker)
    yahformat = yahoodata.get_market_cap() # pulls market cap data from yahoo
    if yahformat is not None: # some market caps are none
        emarket_caps[ticker] = (float(filter(lambda x: x.isdigit(), yahformat)))/100 # formats market caps and takes out B
    elif yahformat is None: # if none, market cap is just 0
        emarket_caps[ticker] = 0

emarket_caps["Ethereum"] = ethcap # adds Ethereum's market cap to dictionary

sorted_caps = sorted(emarket_caps.items(), key = lambda t : t[1], reverse = True) # sorts the dictionary by market cap into the tuple

# here for the next 30 or so lines i am trying to define the next largest company (by market cap) after Ethereum

print sorted_caps

unicodedcaps = {k.decode('utf8'): v for k, v in sorted_caps} # the ticers in the tuple were unicoded

dictcaps = {}
for k, v in unicodedcaps:
    unicodedcaps[k] = v # puts tuple back into dictionary format

capnum = list(enumerate(dictcaps)) # ranks by market cap

dlist = {}
for k, v in capnum:
    dlist[k] = v
print dlist # puts tuple of ranks into dictionary format

for k, v in dlist.items():
    if v == "Ethereum":
        ahhaa = k # figures out Ethereum's rank...ahhaa was because it was an ahhaa moment for me

for k, v in dlist.items():
    if k == (ahhaa + 1):
        nextlargest = v # figures out the next largest market cap

othercompany = "If Ethereum was in the S&P 500, the next largest company would be"

completetweet = (eth, othercompany, nextlargest) # puts together the whole tweet
print completetweet

for line in completetweet: # writes to twitter and sleeps for 24 hours
    api.update_status(line)
    time.sleep(86400)
