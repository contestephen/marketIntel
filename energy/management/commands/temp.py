
 '''
            nymexGasScrape.product= 'hh_natural_gas'
            nymexGasScrape.tradedate = stamp
            nymexGasScrape.month = b[0].text.strip()
            nymexGasScrape.Open = c[0].text.strip()
            nymexGasScrape.high= c[1].text.strip()
            nymexGasScrape.low = c[2].text.strip()
            nymexGasScrape.settle = c[5].text.strip()
            nymexGasScrape.volume = c[6].text.strip()
            nymexGasScrape.openInterest = c[7].text.strip()
            nymexGasScrape.save()
'''

