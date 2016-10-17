from django.core.management.base import BaseCommand
from energy.models import gasStorage
import datetime
import urllib2
from bs4 import BeautifulSoup
from datetime import time

stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class Command(BaseCommand):
    help='script to grab natural gas storage data and commentary from EIA website'

    def handle(self, *args, **options):
        self.stdout.write('\ngrabbed on %s' %stamp)

    def grabStorage(url, source):
        #get natural gas marks, and commentary from EIA webpage
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

                'product': source,
                'reportDate': stamp,
                'thisWeekBcf': thisWeek,
                'lastWeekBcf': lastWeek,
                'yearAgoBcf': lastYear,
                'fiveYearAvgBcf': fiveYear,
                'summary':summary,
                }
        print myGas
        myGetData = gasStorage(**myGas)
        myGetData.save()

grabStorage('http://ir.eia.gov/ngs/ngs.html', 'EIA')
#print ('%s, %s, %s, %s') %(thisWeek, lastWeek, lastYear, fiveYear)
