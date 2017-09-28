import finsymbols
from yahoo_finance import Share
from coinmarketcap import Market

coinmarketcap = Market()
e = coinmarketcap.ticker('ethereum')
ethcap = float(e[0]['market_cap_usd'])/1000000000 # pulls and formats eth market cap data

eth = "Ethereum's market cap is $" + str(round(ethcap, 1)) + "B" # prep for bot

emarket_caps = dict()

sp500 = finsymbols.get_sp500_symbols()

for d in sp500:
    ticker = d['symbol'] # pulls ticker from dictionary
    yahoodata = Share(ticker)
    yahformat = yahoodata.get_market_cap() # pulls market cap data from yahoo
    if yahformat is not None: # some market caps are none
        emarket_caps[ticker] = (float(filter(lambda x: x.isdigit(), yahformat)))/100 # formats market caps and takes out B
    elif yahformat is None: # if none, market cap is just 0
        emarket_caps[ticker] = 0

emarket_caps["Ethereum"] = ethcap # adds Ethereum's market cap to dictionary

below_stack = ((t, c) for t, c in emarket_caps.items() if c < database['Ethereum'])
next_cap = max(below_stack, key=lambda item: item[1])
nextlargest = next_cap[0]

othercompany = "If Ethereum was in the S&P 500, the next largest company would be"

completetweet = (eth, othercompany, nextlargest)

print completetweet
