from __future__ import absolute_import, unicode_literals
from .models import *
from celery import task
import datetime

@task()
def liability_check():
    all_liability=LiabilityInfoModel.objects.all()
    for liability in [1,2,3,4,5]:
        print(liability,datetime.datetime.now())