from django.db import models
import datetime

class RoomInfoModel(models.Model):
    room_people_list=[('1','One Person'),('2','Two People'),('3','Three People'),('4','Four People'),('5','Five People')]
    room_type_list=[('1','With Shower'),('2','Double-Decker'),('3','Normal'),('4','Kitchen')]
    room_no=models.CharField(max_length=20,primary_key=True,verbose_name='Room No: ')
    room_floor=models.CharField(max_length=20,verbose_name='Room Floor: ',null=False)
    room_people=models.CharField(max_length=20,choices=room_people_list,verbose_name='Room People: ',null=False)
    room_type=models.CharField(max_length=20,choices=room_type_list,verbose_name='Room Type: ',null=False)
    room_desc=models.CharField(max_length=100,verbose_name='Room Description',blank=True,null=True)
    room_image=models.ImageField(upload_to='room_image/',default=None, null=True,blank=True,verbose_name='Room Image: ')

    class Meta:
        db_table='room_info'

    def __str__(self):
        return self.room_no

    def __unicode__(self):
        return str(self.room_no)

    def room_people_name(self):
        return self.room_people_list[int(self.room_people)-1][1]
    def room_type_name(self):
        return self.room_type_list[int(self.room_type)-1][1]

class FixtureInfoModel(models.Model):
    fixture_type_list=[('1','Box Spring'),('2','Bed'),('3','Wardrobe'),('4','Carpet'),('5','Night Stand'),('6','Tulle'),('7','Veil'),('8','Table'),('9','Chair'),('10','Coat Hanger'),('11','Bookcase'),('12','Lamp'),('13','Klima'),('14','Mirror')]
    fixture_no = models.CharField(max_length=10,primary_key=True,verbose_name='Fixture No: ')
    room_no=models.ForeignKey(RoomInfoModel,null=True,unique=False,verbose_name='Room No: ')
    fixture_type=models.CharField(max_length=20,choices=fixture_type_list,verbose_name='Fixture Type:')
    fixture_notes=models.CharField(max_length=100,null=True,blank=True, verbose_name='Fixture Notes: ')
    fixture_image = models.ImageField(upload_to='fixture_image/', default=None, null=True, blank=True,verbose_name='Fixture Image: ')

    class Meta:
        db_table='fixture_info'

    def __str__(self):
        return self.fixture_no

    def fixture_type_name(self):
        return self.fixture_type_list[int(self.fixture_type)-1][1]
