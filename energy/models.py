from __future__ import unicode_literals

from django.db import models

class gasFutures(models.Model):
    key = models.AutoField(primary_key=True)
    product = models.CharField(max_length=20)
    tradedate = models.DateTimeField('Trade Date')
    month = models.CharField(max_length=10)
    Open = models.DecimalField(max_digits=4, decimal_places=3)
    high = models.TextField(max_length=5)
    low = models.TextField(max_length=5)
    settle =  models.TextField(max_length=5)
    volume = models.CommaSeparatedIntegerField(max_length=20)
    openInterest = models.CommaSeparatedIntegerField(max_length=20)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s' %(self.product, self.tradedate, self.month, self.Open, self.high, self.low, self.settle)
    class meta():
        db_table='gas_futures'


class basisFutures(models.Model):
    key = models.AutoField(primary_key=True)
    product = models.CharField(max_length=20)
    tradedate = models.DateTimeField('Trade Date')
    month = models.CharField(max_length=10)
    Open = models.DecimalField(max_digits=4, decimal_places=3)
    high = models.TextField(max_length=5)
    low = models.TextField(max_length=5)
    settle =  models.TextField(max_length=5)
    volume = models.CommaSeparatedIntegerField(max_length=20)
    openInterest = models.CommaSeparatedIntegerField(max_length=20)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s %s %s' %(self.product, self.tradedate, self.month, self.Open, self.high, self.low, self.settle, self.volume, self.openInterest)

    class meta():
        db_table='basis_futures'

class gasStorage(models.Model):
    key = models.AutoField(primary_key=True)
    source = models.TextField(max_length=50)
    reportDate = models.DateTimeField('report date')
    thisWeekBcf = models.IntegerField(default=0)
    lastWeekBcf = models.IntegerField(default=0)
    yearAgoBcf = models.IntegerField(default=0)
    fiveYearAvgBcf = models.IntegerField(default=0)
    summary = models.TextField(max_length=2000)


    def __str__(self):
        return '%s, %s, s%, s%' %(self.reportDate, self.stock, self.yearAgo, self.fiveYearAverage)
    class meta():
        db_table = 'gas_storage'

class forwardStrips(models.Model):
      key = models.AutoField(primary_key=True)
      product = models.CharField(max_length=20)
      twelve = models.DecimalField(max_digits=4, decimal_places=3)
      twentyFour = models.DecimalField(max_digits=4, decimal_places=3)

      def __str__(self):
          return '%s, %s, %s' %(self.product, self.twelve, self.twentyFour)
      class meta():
          db_table = 'forwardStrips'
