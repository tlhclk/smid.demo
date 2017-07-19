# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person_panel', '0004_auto_20170715_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personidinfomodel',
            name='s_birth_place',
            field=models.CharField(choices=[('01', 'Adana'), ('02', 'Adıyaman'), ('03', 'Afyonkarahisar'), ('04', 'Ağrı'), ('68', 'Aksaray'), ('05', 'Amasya'), ('06', 'Ankara'), ('07', 'Antalya'), ('75', 'Ardahan'), ('08', 'Artvin'), ('09', 'Aydın'), ('10', 'Balıkesir'), ('74', 'Bartın'), ('72', 'Batman'), ('69', 'Bayburt'), ('11', 'Bilecik'), ('12', 'Bingöl'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'), ('17', 'Çanakkale'), ('18', 'Çankırı'), ('19', 'Çorum'), ('20', 'Denizli'), ('21', 'Diyarbakır'), ('81', 'Düzce'), ('22', 'Edirne'), ('23', 'Elazığ'), ('24', 'Erzincan'), ('25', 'Erzurum'), ('26', 'Eskişehir'), ('27', 'Gaziantep'), ('28', 'Giresun'), ('29', 'Gümüşhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('76', 'Iğdır'), ('32', 'Isparta'), ('33', 'Mersin'), ('34', 'İstanbul'), ('35', 'İzmir'), ('78', 'Karabük'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'), ('39', 'Kırklareli'), ('40', 'Kırşehir'), ('41', 'Kocaeli'), ('42', 'Konya'), ('43', 'Kütahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmaraş'), ('70', 'Karaman'), ('71', 'Kırıkkale'), ('79', 'Kilis'), ('47', 'Mardin'), ('48', 'Muğla'), ('49', 'Muş'), ('50', 'Nevşehir'), ('51', 'Niğde'), ('52', 'Ordu'), ('80', 'Osmaniye'), ('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'), ('73', 'Şırnak'), ('59', 'Tekirdağ'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', 'Şanlıurfa'), ('64', 'Uşak'), ('65', 'Van'), ('77', 'Yalova'), ('66', 'Yozgat'), ('67', 'Zonguldak')], default=('01', 'Adana'), help_text='City Where Student Birth', max_length=20, null=True, verbose_name='Doğduğu Şehir'),
        ),
        migrations.AlterField(
            model_name='studentinfomodel',
            name='id',
            field=models.CharField(default='1701001', help_text='ID', max_length=7, primary_key=True, serialize=False, verbose_name='Öğrenci No'),
        ),
        migrations.AlterField(
            model_name='studentinfomodel',
            name='room_no',
            field=models.ForeignKey(default='101', help_text='Room Number Student Assigned', null=True, on_delete=django.db.models.deletion.CASCADE, to='stock_panel.RoomInfoModel', verbose_name='Oda Numarası'),
        ),
        migrations.AlterField(
            model_name='studentinfomodel',
            name='student_tcn',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='person_panel.PersonIDInfoModel', verbose_name='Öğrencinin Kimlik Numarası'),
        ),
    ]
