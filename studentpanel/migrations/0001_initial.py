# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 11:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParentInfoModel',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('parent_name', models.CharField(max_length=20)),
                ('parent_lastname', models.CharField(max_length=20)),
                ('parent_TCN', models.CharField(max_length=11)),
                ('parent_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('parent_email', models.EmailField(max_length=254)),
                ('relative_degree', models.CharField(max_length=20)),
                ('parent_job', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'parent_info',
            },
        ),
        migrations.CreateModel(
            name='PersonalInfoModel',
            fields=[
                ('id', models.CharField(help_text=b'ID', max_length=7, primary_key=True, serialize=False, verbose_name=b'Personal Id')),
                ('personal_tcn', models.CharField(default=b'00000000000', help_text=b'11 digit', max_length=11, verbose_name=b'TC No')),
                ('personal_name', models.CharField(default=b'Ahmet', help_text=b'Personal Name', max_length=200, verbose_name=b'Personal Name')),
                ('personal_lastname', models.CharField(default=b'Yilmaz', help_text=b'Personal Last Name', max_length=200, verbose_name=b'Personal Last Name')),
                ('personal_phone', phonenumber_field.modelfields.PhoneNumberField(default=b'+905553332211', help_text=b'+905553332211', max_length=128, verbose_name=b'Phone Number')),
                ('personal_email', models.EmailField(default=b'qwe@gam.com', help_text=b'aaaaa@aaaa.aaa', max_length=254, verbose_name=b'Personal Email')),
                ('personal_startday', models.DateField(default=datetime.date.today, help_text=b'1990-12-31', verbose_name=b'Start Day')),
                ('personal_endday', models.DateField(blank=True, help_text=b'1990-12-31', null=True, verbose_name=b'Quit Day')),
                ('personal_city', models.CharField(choices=[(b'01', b'Adana'), (b'02', b'Ad\xc4\xb1yaman'), (b'03', b'Afyon'), (b'04', b'A\xc4\x9fr\xc4\xb1'), (b'05', b'Amasya'), (b'06', b'Ankara'), (b'07', b'Antalya'), (b'08', b'Artvin'), (b'09', b'Ayd\xc4\xb1n'), (b'10', b'Bal\xc4\xb1kesir'), (b'11', b'Bilecik'), (b'12', b'Bing\xc3\xb6l'), (b'13', b'Bitlis'), (b'14', b'Bolu'), (b'15', b'Burdur'), (b'16', b'Bursa'), (b'17', b'\xc3\x87anakkale'), (b'18', b'\xc3\x87ank\xc4\xb1r\xc4\xb1'), (b'19', b'\xc3\x87orum'), (b'20', b'Denizli'), (b'21', b'Diyarbak\xc4\xb1r'), (b'22', b'Edirne'), (b'23', b'Elaz\xc4\xb1\xc4\x9f'), (b'24', b'Erzincan'), (b'25', b'Erzurum'), (b'26', b'Eski\xc5\x9fehir'), (b'27', b'Gaziantep'), (b'28', b'Giresun'), (b'29', b'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), (b'30', b'Hakkari'), (b'31', b'Hatay'), (b'32', b'Isparta'), (b'33', b'Mersin'), (b'34', b'\xc4\xb0stanbul'), (b'35', b'\xc4\xb0zmir'), (b'36', b'Kars'), (b'37', b'Kastamonu'), (b'38', b'Kayseri'), (b'39', b'K\xc4\xb1rklareli'), (b'40', b'K\xc4\xb1r\xc5\x9fehir'), (b'41', b'Kocaeli'), (b'42', b'Konya'), (b'43', b'K\xc3\xbctahya'), (b'44', b'Malatya'), (b'45', b'Manisa'), (b'46', b'Kahramanmara\xc5\x9f'), (b'47', b'Mardin'), (b'48', b'Mu\xc4\x9fla'), (b'49', b'Mu\xc5\x9f'), (b'50', b'Nev\xc5\x9fehir'), (b'51', b'Ni\xc4\x9fde'), (b'52', b'Ordu'), (b'53', b'Rize'), (b'54', b'Sakarya'), (b'55', b'Samsun'), (b'56', b'Siirt'), (b'57', b'Sinop'), (b'58', b'Sivas'), (b'59', b'Tekirda\xc4\x9f'), (b'60', b'Tokat'), (b'61', b'Trabzon'), (b'62', b'Tunceli'), (b'63', b'\xc5\x9eanl\xc4\xb1urfa'), (b'64', b'U\xc5\x9fak'), (b'65', b'Van'), (b'66', b'Yozgat'), (b'67', b'Zonguldak'), (b'68', b'Aksaray'), (b'69', b'Bayburt'), (b'70', b'Karaman'), (b'71', b'K\xc4\xb1r\xc4\xb1kkale'), (b'72', b'Batman'), (b'73', b'\xc5\x9e\xc4\xb1rnak'), (b'74', b'Bart\xc4\xb1n'), (b'75', b'Ardahan'), (b'76', b'I\xc4\x9fd\xc4\xb1r'), (b'77', b'Yalova'), (b'78', b'Karab\xc3\xbck'), (b'79', b'Kilis'), (b'80', b'Osmaniye'), (b'81', b'D\xc3\xbczce')], default=b'Ankara', help_text=b'City Where Personal From', max_length=20, null=True, verbose_name=b'Personal City')),
                ('personal_town', models.CharField(default=b'yok', help_text=b'Town Where Personal From', max_length=20, null=True, verbose_name=b'Personal Town')),
                ('personal_adress', models.CharField(default=b'yok', help_text=b'Distinct, Street, Building No, Flat No', max_length=50, null=True, verbose_name=b'Personal Address')),
                ('personal_birthday', models.DateField(default=b'1990-12-31', help_text=b'1990-12-31', verbose_name=b'Birthday')),
                ('blood_type', models.CharField(choices=[(b'0_rh_+', b'0 rh +'), (b'0_rh_-', b'0 rh -'), (b'A_rh_+', b'Arh +'), (b'A_rh_-', b'A rh -'), (b'B_rh_+', b'B rh +'), (b'B_rh_-', b'B rh -'), (b'AB_rh_+', b'AB rh+'), (b'AB_rh_-', b'AB rh-')], default=b'0 rh +', help_text=b'Blood Type', max_length=20, null=True, verbose_name=b'Blood Type')),
                ('health_notes', models.CharField(blank=True, default=b'-', help_text=b'Health Notes', max_length=100, null=True, verbose_name=b'Health Notes')),
                ('special_notes', models.CharField(blank=True, default=b'-', help_text=b'Special Notes', max_length=100, null=True, verbose_name=b'Special Notes')),
                ('image_field', models.ImageField(blank=True, default=b'Desktop/asd.jpg', help_text=b'Profile Image Path', null=True, upload_to=b'profile_pic/', verbose_name=b'Image Upload')),
            ],
            options={
                'db_table': 'personal_info',
            },
        ),
        migrations.CreateModel(
            name='StudentInfoModel',
            fields=[
                ('id', models.CharField(help_text=b'ID', max_length=7, primary_key=True, serialize=False, verbose_name=b'Student Id')),
                ('student_tcn', models.CharField(default=b'00000000000', help_text=b'11 digit', max_length=11, verbose_name=b'TC No')),
                ('student_name', models.CharField(default=b'Ahmet', help_text=b'Student Name', max_length=200, verbose_name=b'Student Name')),
                ('student_lastname', models.CharField(default=b'Yilmaz', help_text=b'Student Last Name', max_length=200, verbose_name=b'Student Last Name')),
                ('student_phone', phonenumber_field.modelfields.PhoneNumberField(default=b'+905553332211', help_text=b'+905553332211', max_length=128, verbose_name=b'Phone Number')),
                ('student_email', models.EmailField(default=b'qwe@gam.com', help_text=b'aaaaa@aaaa.aaa', max_length=254, verbose_name=b'Student Email')),
                ('student_birthday', models.DateField(default=b'1990-12-31', help_text=b'1990-12-31', verbose_name=b'Birthday')),
                ('student_regday', models.DateField(default=datetime.date.today, help_text=b'1990-12-31', verbose_name=b'Registration Day')),
                ('student_city', models.CharField(choices=[(b'01', b'Adana'), (b'02', b'Ad\xc4\xb1yaman'), (b'03', b'Afyon'), (b'04', b'A\xc4\x9fr\xc4\xb1'), (b'05', b'Amasya'), (b'06', b'Ankara'), (b'07', b'Antalya'), (b'08', b'Artvin'), (b'09', b'Ayd\xc4\xb1n'), (b'10', b'Bal\xc4\xb1kesir'), (b'11', b'Bilecik'), (b'12', b'Bing\xc3\xb6l'), (b'13', b'Bitlis'), (b'14', b'Bolu'), (b'15', b'Burdur'), (b'16', b'Bursa'), (b'17', b'\xc3\x87anakkale'), (b'18', b'\xc3\x87ank\xc4\xb1r\xc4\xb1'), (b'19', b'\xc3\x87orum'), (b'20', b'Denizli'), (b'21', b'Diyarbak\xc4\xb1r'), (b'22', b'Edirne'), (b'23', b'Elaz\xc4\xb1\xc4\x9f'), (b'24', b'Erzincan'), (b'25', b'Erzurum'), (b'26', b'Eski\xc5\x9fehir'), (b'27', b'Gaziantep'), (b'28', b'Giresun'), (b'29', b'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), (b'30', b'Hakkari'), (b'31', b'Hatay'), (b'32', b'Isparta'), (b'33', b'Mersin'), (b'34', b'\xc4\xb0stanbul'), (b'35', b'\xc4\xb0zmir'), (b'36', b'Kars'), (b'37', b'Kastamonu'), (b'38', b'Kayseri'), (b'39', b'K\xc4\xb1rklareli'), (b'40', b'K\xc4\xb1r\xc5\x9fehir'), (b'41', b'Kocaeli'), (b'42', b'Konya'), (b'43', b'K\xc3\xbctahya'), (b'44', b'Malatya'), (b'45', b'Manisa'), (b'46', b'Kahramanmara\xc5\x9f'), (b'47', b'Mardin'), (b'48', b'Mu\xc4\x9fla'), (b'49', b'Mu\xc5\x9f'), (b'50', b'Nev\xc5\x9fehir'), (b'51', b'Ni\xc4\x9fde'), (b'52', b'Ordu'), (b'53', b'Rize'), (b'54', b'Sakarya'), (b'55', b'Samsun'), (b'56', b'Siirt'), (b'57', b'Sinop'), (b'58', b'Sivas'), (b'59', b'Tekirda\xc4\x9f'), (b'60', b'Tokat'), (b'61', b'Trabzon'), (b'62', b'Tunceli'), (b'63', b'\xc5\x9eanl\xc4\xb1urfa'), (b'64', b'U\xc5\x9fak'), (b'65', b'Van'), (b'66', b'Yozgat'), (b'67', b'Zonguldak'), (b'68', b'Aksaray'), (b'69', b'Bayburt'), (b'70', b'Karaman'), (b'71', b'K\xc4\xb1r\xc4\xb1kkale'), (b'72', b'Batman'), (b'73', b'\xc5\x9e\xc4\xb1rnak'), (b'74', b'Bart\xc4\xb1n'), (b'75', b'Ardahan'), (b'76', b'I\xc4\x9fd\xc4\xb1r'), (b'77', b'Yalova'), (b'78', b'Karab\xc3\xbck'), (b'79', b'Kilis'), (b'80', b'Osmaniye'), (b'81', b'D\xc3\xbczce')], default=b'Ankara', help_text=b'City Where Student From', max_length=20, null=True, verbose_name=b'Student City')),
                ('student_town', models.CharField(default=b'yok', help_text=b'Town Where Student From', max_length=20, null=True, verbose_name=b'Student Town')),
                ('student_adress', models.CharField(default=b'yok', help_text=b'Distinct, Street, Building No, Flat No', max_length=50, null=True, verbose_name=b'Student Address')),
                ('room_number', models.CharField(default=b'101', help_text=b'Room Number Student Assigned', max_length=3, null=True, verbose_name=b'Room Number')),
                ('student_type', models.CharField(choices=[(b'Guest', b'Guest'), (b'Temporary', b'Temporary'), (b'Permanent', b'Permanent')], default=b'Permanent', help_text=b'Student Accommodation Type', max_length=10, verbose_name=b'Student Type')),
                ('birth_place', models.CharField(choices=[(b'01', b'Adana'), (b'02', b'Ad\xc4\xb1yaman'), (b'03', b'Afyon'), (b'04', b'A\xc4\x9fr\xc4\xb1'), (b'05', b'Amasya'), (b'06', b'Ankara'), (b'07', b'Antalya'), (b'08', b'Artvin'), (b'09', b'Ayd\xc4\xb1n'), (b'10', b'Bal\xc4\xb1kesir'), (b'11', b'Bilecik'), (b'12', b'Bing\xc3\xb6l'), (b'13', b'Bitlis'), (b'14', b'Bolu'), (b'15', b'Burdur'), (b'16', b'Bursa'), (b'17', b'\xc3\x87anakkale'), (b'18', b'\xc3\x87ank\xc4\xb1r\xc4\xb1'), (b'19', b'\xc3\x87orum'), (b'20', b'Denizli'), (b'21', b'Diyarbak\xc4\xb1r'), (b'22', b'Edirne'), (b'23', b'Elaz\xc4\xb1\xc4\x9f'), (b'24', b'Erzincan'), (b'25', b'Erzurum'), (b'26', b'Eski\xc5\x9fehir'), (b'27', b'Gaziantep'), (b'28', b'Giresun'), (b'29', b'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), (b'30', b'Hakkari'), (b'31', b'Hatay'), (b'32', b'Isparta'), (b'33', b'Mersin'), (b'34', b'\xc4\xb0stanbul'), (b'35', b'\xc4\xb0zmir'), (b'36', b'Kars'), (b'37', b'Kastamonu'), (b'38', b'Kayseri'), (b'39', b'K\xc4\xb1rklareli'), (b'40', b'K\xc4\xb1r\xc5\x9fehir'), (b'41', b'Kocaeli'), (b'42', b'Konya'), (b'43', b'K\xc3\xbctahya'), (b'44', b'Malatya'), (b'45', b'Manisa'), (b'46', b'Kahramanmara\xc5\x9f'), (b'47', b'Mardin'), (b'48', b'Mu\xc4\x9fla'), (b'49', b'Mu\xc5\x9f'), (b'50', b'Nev\xc5\x9fehir'), (b'51', b'Ni\xc4\x9fde'), (b'52', b'Ordu'), (b'53', b'Rize'), (b'54', b'Sakarya'), (b'55', b'Samsun'), (b'56', b'Siirt'), (b'57', b'Sinop'), (b'58', b'Sivas'), (b'59', b'Tekirda\xc4\x9f'), (b'60', b'Tokat'), (b'61', b'Trabzon'), (b'62', b'Tunceli'), (b'63', b'\xc5\x9eanl\xc4\xb1urfa'), (b'64', b'U\xc5\x9fak'), (b'65', b'Van'), (b'66', b'Yozgat'), (b'67', b'Zonguldak'), (b'68', b'Aksaray'), (b'69', b'Bayburt'), (b'70', b'Karaman'), (b'71', b'K\xc4\xb1r\xc4\xb1kkale'), (b'72', b'Batman'), (b'73', b'\xc5\x9e\xc4\xb1rnak'), (b'74', b'Bart\xc4\xb1n'), (b'75', b'Ardahan'), (b'76', b'I\xc4\x9fd\xc4\xb1r'), (b'77', b'Yalova'), (b'78', b'Karab\xc3\xbck'), (b'79', b'Kilis'), (b'80', b'Osmaniye'), (b'81', b'D\xc3\xbczce')], default=(b'01', b'Adana'), help_text=b'City Where Student Birth', max_length=20, null=True, verbose_name=b'Birth City')),
                ('school_name', models.CharField(default=b'okulsuz', help_text=b'School Name', max_length=50, null=True, verbose_name=b'School Name')),
                ('education_year', models.CharField(choices=[(b'Prep', b'Preparation'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')], default=(b'Prep', b'Preparation'), help_text=b'Education Year', max_length=20, null=True, verbose_name=b'Education Year')),
                ('blood_type', models.CharField(choices=[(b'0_rh_+', b'0 rh +'), (b'0_rh_-', b'0 rh -'), (b'A_rh_+', b'Arh +'), (b'A_rh_-', b'A rh -'), (b'B_rh_+', b'B rh +'), (b'B_rh_-', b'B rh -'), (b'AB_rh_+', b'AB rh+'), (b'AB_rh_-', b'AB rh-')], default=b'0 rh +', help_text=b'Blood Type', max_length=20, null=True, verbose_name=b'Blood Type')),
                ('health_notes', models.CharField(blank=True, default=b'-', help_text=b'Health Notes', max_length=100, null=True, verbose_name=b'Health Notes')),
                ('special_notes', models.CharField(blank=True, default=b'-', help_text=b'Special Notes', max_length=100, null=True, verbose_name=b'Special Notes')),
                ('file_field', models.ImageField(blank=True, default=b'Desktop/asd.jpg', help_text=b'Profile Image Path', null=True, upload_to=b'profile_pic/', verbose_name=b'Image Upload')),
            ],
            options={
                'db_table': 'student_info',
            },
        ),
    ]
