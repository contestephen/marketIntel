from django.core.management.base import BaseCommand
from pprint import pformat
from energy.models import gasFutures, forwardStrips
from django.core.exceptions import *
import datetime
import logging
import ast

stamp  = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
logging.basicConfig(filename='django_scrape.log', level=logging.INFO)

class Command(BaseCommand):
    help="script to scrape nymex henry hub gas marks.  Add new Urls into /management/commands/natgas_futures.py"

    def handle(self, *args, **options):
        from energy.models import gasFutures, forwardStrips
        from bs4 import BeautifulSoup
        import urllib2

        self.stdout.write('\nscraping started at %s' %stamp)
        logging.info('starting scrape on %s', stamp)
        page = urllib2.Request('http://www.cmegroup.com/trading/energy/natural-gas/natural-gas_quotes_settlements_futures.html', headers = {'User-Agent': 'Mozilla/5.0'})
        cmeHtml = urllib2.urlopen(page).read()
        soup = BeautifulSoup(cmeHtml, "html.parser")

        table = soup.find('table', attrs ={'class': 'cmeTable'})
        table_body = table.find('tbody')
        rows= table_body.find_all('tr')
        settles = []
        x = []
        for row in rows[0:35]:
            c=row.findChildren('td')
            b=row.findChildren('th')
            #create instance of myGas dict
            try:
                x.append(c[5].text.strip())

                myGas = {
                    'product':'hh_natural_gas',
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
                logging.info(myGas)


            except ValidationError:
                print 'settlements are not posted yet'
                logging.info('settlements are not posted')



        print x
        '''
        settles to estimate 12/24 month forward prices
        x = list(map(int, ast.literal_eval(x)))
        averages = {
                'product': 'hh_natgas',
                'twelve': sum(int(x)[:11])/12,
                'twentyFour':sum(int(x)[:23])/24
                }
        print x
        print averages
        save scrape data '''
        myGetData = gasFutures(**myGas)
        myGetData.save()
        #self.stdout.write('\nbasis scrape complete.  Check log for more info')
        '''
        #save 12/24 month averages
        MyAverage = forwardStrips(**averages)
        myAverage.save()
       '''
