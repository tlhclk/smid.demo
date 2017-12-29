# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import AccountInfoModel,PeriodicPaymentModel,PersonAssetInfoModel,TransactionInfoModel,BillInfoModel
from django.contrib import admin

admin.site.register(AccountInfoModel)
admin.site.register(BillInfoModel)
admin.site.register(TransactionInfoModel)
admin.site.register(PersonAssetInfoModel)
admin.site.register(PeriodicPaymentModel)