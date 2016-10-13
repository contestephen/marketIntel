from django.core.management.base import BaseCommand
import datetime
from pprint import pformat
import logging
from energy.models import basisFutures
from bs4 import BeautifulSoup
import urllib2

#basis prices seem to be posted the next morning on CME, use todays date -1

today=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
stamp = yesterday.strftime('%Y-%m-%d %H:%M')
logging.basicConfig(filename='django_scrape.log', level=logging.INFO)

class Command(BaseCommand):
    help="script to scrape nymex basis marks.  Add new Urls into /management/commands/basis_futures.py"

    def handle(self, *args, **options):
        self.stdout.write('\nscraping started at %s' %today)

    def getWebPage(url, product):
        page = urllib2.Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
        cmeHtml = urllib2.urlopen(page).read()
        soup = BeautifulSoup(cmeHtml, "html.parser")

        table = soup.find('table', attrs ={'class': 'cmeTable'})
        table_body = table.find('tbody')
        rows= table_body.find_all('tr')

         #log it!
        logging.info('starting basis scrape on %s for product %s', today, product)

        for row in rows[0:len(rows)-1]:
            c = row.findChildren('td')
            b = row.findChildren('th')
            #create instance of myGas dict

            myGas={
                  'product': product,
                  'tradedate': stamp,
                  'month':b[0].text.strip(),
                  'Open':c[0].text.strip(),
                  'high':c[1].text.strip(),
                  'low':c[2].text.strip(),
                  'settle':c[5].text.strip(),
                  'volume':c[6].text.strip(),
                  'openInterest':c[7].text.strip()
                    }
            #debug
            #print myGas
            logging.info(myGas)
            #print pformat(myGas)

            #save data
            myGetData = basisFutures(**myGas)
            myGetData.save()
            #self.stdout.write('\nbasis scrape complete.  Check log for more info')


    getWebPage('http://www.cmegroup.com/trading/energy/natural-gas/transco-zone-6-new-york-natural-gas-basis-swap-futures-platts-iferc_quotes_settlements_futures.html','TranscoZ6NY')
    getWebPage('http://www.cmegroup.com/trading/energy/natural-gas/transco-zone-6-non-ny-platts-iferc-basis-swap_quotes_settlements_futures.html','TranscoZ6NonNY')
    getWebPage('http://www.cmegroup.com/trading/energy/natural-gas/texas-eastern-zone-m-3-natural-gas-basis-swap-futures-platts-iferc_quotes_settlements_futures.html','TexasM3')
    getWebPage('http://www.cmegroup.com/trading/energy/natural-gas/algonquin-citygates-natural-gas-basis-futures_quotes_settlements_futures.html','AlgonquinCityGates')

