from django.core.management.base import BaseCommand
from energy.models import gasStorage
import datetime
import urllib2
from bs4 import BeautifulSoup
from datetime import time
from pprint import pformat
import logging
stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
logging.basicConfig(filename='eia_log.log', level=logging.INFO)

class Command(BaseCommand):
    help='script to grab natural gas storage data and commentary from EIA website'

    def handle(self, *args, **options):

        self.stdout.write('\ngrabbed on %s' %stamp)
        url = 'http://ir.eia.gov/ngs/ngs.html'
        source = 'EIA'
        page = urllib2.Request(url, headers = {'User-Agent':'Mozilla/5.0'})
        Html = urllib2.urlopen(page).read()
        soup = BeautifulSoup(Html, "html.parser")

        rows = soup.find_all('tr')
        thisWeek = rows[11].find_all('td')[1].text.strip()
        lastWeek = rows[11].find_all('td')[4].text.strip()
        lastYear = rows[11].find_all('td')[14].text.strip()
        fiveYear = rows[11].find_all('td')[20].text.strip()
        summary = soup.find_all('p')[3].text.strip()
        myGas = {

                'source': source,
                'reportDate': stamp,
                'thisWeekBcf': thisWeek,
                'lastWeekBcf': lastWeek,
                'yearAgoBcf': lastYear,
                'fiveYearAvgBcf': fiveYear,
                'summary':summary,
                }
        logging.info(myGas)
        print pformat(myGas)
        myGetData = gasStorage(**myGas)
        myGetData.save()

#print ('%s, %s, %s, %s') %(thisWeek, lastWeek, lastYear, fiveYear)
