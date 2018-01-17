# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
#from .models import CityInfoModel,TownInfoModel,NeighborhoodInfoModel,PostalCodeInfoModel
#from slugify import slugify
#import xlrd,os

#TODO: adres bilgileri düzenlenecek
class OperationPanelConfig(AppConfig):
    name = 'operation_panel'

def create_adress_info(path):
    regions={}
    # workbook = xlrd.open_workbook('operation_panel/28_09_2017.xlsx')
    # sheet=workbook.sheet_by_index(0)
    # for row in range (1,sheet.nrows):
    #     city=sheet.row(row)[0].value
    #     town =sheet.row(row)[1].value.strip()
    #     neighborhood=sheet.row(row)[2].value.strip()
    #     part=sheet.row(row)[3].value.strip()
    #     postal_code=sheet.row(row)[4].value.strip()
    #     print (row)
    #     if len(CityInfoModel.objects.filter(city_name=city))==0:
    #         CityInfoModel(city_name=city,city_slug=city).save()
    #
    #     if len(TownInfoModel.objects.filter(town_name=town))==0:
    #         TownInfoModel(city=CityInfoModel.objects.filter(city_name=city)[0],town_name=town,town_slug=town).save()
    #
    #     if len(NeighborhoodInfoModel.objects.filter(neighborhood_name=neighborhood))==0:
    #         NeighborhoodInfoModel(town=TownInfoModel.objects.filter(town_name=town)[0],neighborhood_name=neighborhood,neighborhood_slug=neighborhood).save()
    #
    #     if len(PostalCodeInfoModel.objects.filter(pk_name=part))==0:
    #         PostalCodeInfoModel(neighborhood=NeighborhoodInfoModel.objects.filter(neighborhood_name=neighborhood)[0],pk_name=part,pk_slug=part,postal_code=postal_code).save()


#create_adress_info('city-town_info.xlsx')

