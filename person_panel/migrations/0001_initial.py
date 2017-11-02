# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import person_panel.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParentInfoModel',
            fields=[
                ('id', models.CharField(default='1704001', max_length=8, primary_key=True, serialize=False)),
                ('person', models.CharField(max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('tcn', models.CharField(blank=True, max_length=11, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128)),
                ('email', models.EmailField(default='', max_length=254)),
                ('relative_degree', models.CharField(default='', max_length=20)),
                ('job', models.CharField(blank=True, max_length=20, null=True)),
                ('company_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'parent_info',
            },
        ),
        migrations.CreateModel(
            name='PersonalInfoModel',
            fields=[
                ('id', models.CharField(default='', max_length=7, primary_key=True, serialize=False)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='+905553332211', max_length=13)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('start_day', models.DateField(default=person_panel.models.get_date, max_length=10)),
                ('end_day', models.DateField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(choices=[('01', 'Adana'), ('02', 'Adıyaman'), ('03', 'Afyonkarahisar'), ('04', 'Ağrı'), ('68', 'Aksaray'), ('05', 'Amasya'), ('06', 'Ankara'), ('07', 'Antalya'), ('75', 'Ardahan'), ('08', 'Artvin'), ('09', 'Aydın'), ('10', 'Balıkesir'), ('74', 'Bartın'), ('72', 'Batman'), ('69', 'Bayburt'), ('11', 'Bilecik'), ('12', 'Bingöl'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'), ('17', 'Çanakkale'), ('18', 'Çankırı'), ('19', 'Çorum'), ('20', 'Denizli'), ('21', 'Diyarbakır'), ('81', 'Düzce'), ('22', 'Edirne'), ('23', 'Elazığ'), ('24', 'Erzincan'), ('25', 'Erzurum'), ('26', 'Eskişehir'), ('27', 'Gaziantep'), ('28', 'Giresun'), ('29', 'Gümüşhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('76', 'Iğdır'), ('32', 'Isparta'), ('33', 'Mersin'), ('34', 'İstanbul'), ('35', 'İzmir'), ('78', 'Karabük'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'), ('39', 'Kırklareli'), ('40', 'Kırşehir'), ('41', 'Kocaeli'), ('42', 'Konya'), ('43', 'Kütahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmaraş'), ('70', 'Karaman'), ('71', 'Kırıkkale'), ('79', 'Kilis'), ('47', 'Mardin'), ('48', 'Muğla'), ('49', 'Muş'), ('50', 'Nevşehir'), ('51', 'Niğde'), ('52', 'Ordu'), ('80', 'Osmaniye'), ('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'), ('73', 'Şırnak'), ('59', 'Tekirdağ'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', 'Şanlıurfa'), ('64', 'Uşak'), ('65', 'Van'), ('77', 'Yalova'), ('66', 'Yozgat'), ('67', 'Zonguldak')], default='1', max_length=20)),
                ('town', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_type', models.CharField(choices=[('0', '0 rh +'), ('1', '0 rh -'), ('2', 'A rh +'), ('3', 'A rh -'), ('4', 'B rh +'), ('5', 'B rh -'), ('6', 'AB rh+'), ('7', 'AB rh-')], default='1', max_length=20)),
                ('health_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('special_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('image_field', models.ImageField(default='', upload_to='profile_pic/')),
                ('company_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'personal_info',
            },
        ),
        migrations.CreateModel(
            name='PersonIDInfoModel',
            fields=[
                ('tcn', models.CharField(default='', max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('birth_day', models.DateField(default='1990-12-31', max_length=10)),
                ('birth_place', models.CharField(choices=[('01', 'Adana'), ('02', 'Adıyaman'), ('03', 'Afyonkarahisar'), ('04', 'Ağrı'), ('68', 'Aksaray'), ('05', 'Amasya'), ('06', 'Ankara'), ('07', 'Antalya'), ('75', 'Ardahan'), ('08', 'Artvin'), ('09', 'Aydın'), ('10', 'Balıkesir'), ('74', 'Bartın'), ('72', 'Batman'), ('69', 'Bayburt'), ('11', 'Bilecik'), ('12', 'Bingöl'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'), ('17', 'Çanakkale'), ('18', 'Çankırı'), ('19', 'Çorum'), ('20', 'Denizli'), ('21', 'Diyarbakır'), ('81', 'Düzce'), ('22', 'Edirne'), ('23', 'Elazığ'), ('24', 'Erzincan'), ('25', 'Erzurum'), ('26', 'Eskişehir'), ('27', 'Gaziantep'), ('28', 'Giresun'), ('29', 'Gümüşhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('76', 'Iğdır'), ('32', 'Isparta'), ('33', 'Mersin'), ('34', 'İstanbul'), ('35', 'İzmir'), ('78', 'Karabük'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'), ('39', 'Kırklareli'), ('40', 'Kırşehir'), ('41', 'Kocaeli'), ('42', 'Konya'), ('43', 'Kütahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmaraş'), ('70', 'Karaman'), ('71', 'Kırıkkale'), ('79', 'Kilis'), ('47', 'Mardin'), ('48', 'Muğla'), ('49', 'Muş'), ('50', 'Nevşehir'), ('51', 'Niğde'), ('52', 'Ordu'), ('80', 'Osmaniye'), ('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'), ('73', 'Şırnak'), ('59', 'Tekirdağ'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', 'Şanlıurfa'), ('64', 'Uşak'), ('65', 'Van'), ('77', 'Yalova'), ('66', 'Yozgat'), ('67', 'Zonguldak')], default='1', max_length=20)),
                ('father', models.CharField(default='', max_length=20)),
                ('mother', models.CharField(default='', max_length=20)),
                ('nation', models.CharField(choices=[('1', 'Türkiye')], default='1', max_length=30)),
                ('idcard_type', models.CharField(choices=[('1', 'Nüfus Cüzdanı'), ('2', 'TC Kimliği'), ('3', 'Ehliyet'), ('4', 'Pasaport'), ('5', 'Diğer')], default='1', max_length=50)),
                ('register_vilage', models.CharField(choices=[('01', 'Adana'), ('02', 'Adıyaman'), ('03', 'Afyonkarahisar'), ('04', 'Ağrı'), ('68', 'Aksaray'), ('05', 'Amasya'), ('06', 'Ankara'), ('07', 'Antalya'), ('75', 'Ardahan'), ('08', 'Artvin'), ('09', 'Aydın'), ('10', 'Balıkesir'), ('74', 'Bartın'), ('72', 'Batman'), ('69', 'Bayburt'), ('11', 'Bilecik'), ('12', 'Bingöl'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'), ('17', 'Çanakkale'), ('18', 'Çankırı'), ('19', 'Çorum'), ('20', 'Denizli'), ('21', 'Diyarbakır'), ('81', 'Düzce'), ('22', 'Edirne'), ('23', 'Elazığ'), ('24', 'Erzincan'), ('25', 'Erzurum'), ('26', 'Eskişehir'), ('27', 'Gaziantep'), ('28', 'Giresun'), ('29', 'Gümüşhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('76', 'Iğdır'), ('32', 'Isparta'), ('33', 'Mersin'), ('34', 'İstanbul'), ('35', 'İzmir'), ('78', 'Karabük'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'), ('39', 'Kırklareli'), ('40', 'Kırşehir'), ('41', 'Kocaeli'), ('42', 'Konya'), ('43', 'Kütahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmaraş'), ('70', 'Karaman'), ('71', 'Kırıkkale'), ('79', 'Kilis'), ('47', 'Mardin'), ('48', 'Muğla'), ('49', 'Muş'), ('50', 'Nevşehir'), ('51', 'Niğde'), ('52', 'Ordu'), ('80', 'Osmaniye'), ('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'), ('73', 'Şırnak'), ('59', 'Tekirdağ'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', 'Şanlıurfa'), ('64', 'Uşak'), ('65', 'Van'), ('77', 'Yalova'), ('66', 'Yozgat'), ('67', 'Zonguldak')], default='1', max_length=50)),
                ('register_town', models.CharField(default='', max_length=50)),
                ('register_distinct', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(choices=[('1', 'Kadın'), ('2', 'Erkek')], default='1', max_length=5)),
                ('nufus_cilt', models.CharField(default='', max_length=4)),
                ('nufus_ailesira', models.CharField(default='', max_length=5)),
                ('nufus_sirano', models.CharField(default='', max_length=4)),
                ('medeni_hali', models.CharField(choices=[('1', 'Bekar'), ('2', 'Evli'), ('3', 'Dul'), ('4', 'Diğer')], default='1', max_length=10)),
                ('company_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'personid_info',
            },
        ),
        migrations.CreateModel(
            name='StudentInfoModel',
            fields=[
                ('id', models.CharField(default='1701001', max_length=7, primary_key=True, serialize=False)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='+905553332211', max_length=13)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('start_day', models.DateField(default=person_panel.models.get_date, max_length=10)),
                ('leave_day', models.DateField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(choices=[('01', 'Adana'), ('02', 'Adıyaman'), ('03', 'Afyonkarahisar'), ('04', 'Ağrı'), ('68', 'Aksaray'), ('05', 'Amasya'), ('06', 'Ankara'), ('07', 'Antalya'), ('75', 'Ardahan'), ('08', 'Artvin'), ('09', 'Aydın'), ('10', 'Balıkesir'), ('74', 'Bartın'), ('72', 'Batman'), ('69', 'Bayburt'), ('11', 'Bilecik'), ('12', 'Bingöl'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'), ('17', 'Çanakkale'), ('18', 'Çankırı'), ('19', 'Çorum'), ('20', 'Denizli'), ('21', 'Diyarbakır'), ('81', 'Düzce'), ('22', 'Edirne'), ('23', 'Elazığ'), ('24', 'Erzincan'), ('25', 'Erzurum'), ('26', 'Eskişehir'), ('27', 'Gaziantep'), ('28', 'Giresun'), ('29', 'Gümüşhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('76', 'Iğdır'), ('32', 'Isparta'), ('33', 'Mersin'), ('34', 'İstanbul'), ('35', 'İzmir'), ('78', 'Karabük'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'), ('39', 'Kırklareli'), ('40', 'Kırşehir'), ('41', 'Kocaeli'), ('42', 'Konya'), ('43', 'Kütahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmaraş'), ('70', 'Karaman'), ('71', 'Kırıkkale'), ('79', 'Kilis'), ('47', 'Mardin'), ('48', 'Muğla'), ('49', 'Muş'), ('50', 'Nevşehir'), ('51', 'Niğde'), ('52', 'Ordu'), ('80', 'Osmaniye'), ('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'), ('73', 'Şırnak'), ('59', 'Tekirdağ'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', 'Şanlıurfa'), ('64', 'Uşak'), ('65', 'Van'), ('77', 'Yalova'), ('66', 'Yozgat'), ('67', 'Zonguldak')], default='1', max_length=20)),
                ('town', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('room_id', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('0', 'Normal'), ('1', 'Geçici'), ('2', 'Misafir')], default='1', max_length=10)),
                ('school_name', models.CharField(blank=True, max_length=30, null=True)),
                ('education_year', models.CharField(choices=[('0', 'Preparation'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='1', max_length=20)),
                ('blood_type', models.CharField(choices=[('0', '0 rh +'), ('1', '0 rh -'), ('2', 'A rh +'), ('3', 'A rh -'), ('4', 'B rh +'), ('5', 'B rh -'), ('6', 'AB rh+'), ('7', 'AB rh-')], default='1', max_length=20)),
                ('health_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('special_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('image_field', models.ImageField(default='', upload_to='profile_pic/')),
                ('position', models.BooleanField(default='1')),
                ('company_id', models.CharField(max_length=20)),
                ('tcn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='person_panel.PersonIDInfoModel')),
            ],
            options={
                'db_table': 'student_info',
            },
        ),
        migrations.AddField(
            model_name='personalinfomodel',
            name='tcn',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='person_panel.PersonIDInfoModel'),
        ),
    ]
