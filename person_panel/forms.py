from django import forms
from .models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonIDInfoModel
#from fixturepanel.models import RoomInfoModel
import datetime

class ParentInfoForm(forms.ModelForm):
    class Meta:
        model=ParentInfoModel
        fields=('id',
                'student_id',
                'parent_name',
                'parent_lastname',
                'parent_TCN',
                'parent_phone',
                'parent_email',
                'relative_degree',
                'parent_job',
                )


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model=PersonalInfoModel
        fields=('id',
                'personal_tcn',
                'personal_name',
                'personal_lastname',
                'personal_phone',
                'personal_email',
                'personal_birthday',
                'personal_startday',
                'personal_endday',
                'personal_city',
                'personal_town',
                'personal_adress',
                'blood_type',
                'health_notes',
                'special_notes',
                'image_field'
                )

class PersonIDInfoForm(forms.ModelForm):
    s_birthday=forms.DateField(initial=datetime.date.today(),widget=forms.SelectDateWidget,label='Öğrencinin Doğum Tarihi')
    class Meta:
        model=PersonIDInfoModel
        fields=('s_nation',
                's_idcard_type',
                's_gender',
                's_tcn',
                's_name',
                's_lastname',
                's_father',
                's_mother',
                's_birthday',
                's_birth_place',
                's_medeni_hali',
                's_register_vilage',
                's_register_town',
                's_register_distinct',
                's_nufus_cilt',
                's_nufus_ailesira',
                's_nufus_sirano',
                )


class StudentInfoForm(forms.ModelForm):
    student_regday=forms.DateField(initial=datetime.date.today(),widget=forms.SelectDateWidget,label='Öğrencinin Kayıt Tarihi')
    student_tcn=forms.ModelChoiceField(queryset=PersonIDInfoModel.objects.all())
    class Meta:
        model=StudentInfoModel
        fields=(
                'id',
                'student_position',
                'student_tcn',
                'student_phone',
                'student_email',
                'student_regday',
                'student_city',
                'student_town',
                'room_no',
                'student_type',
                'school_name',
                'education_year',
                'blood_type',
                'health_notes',
                'special_notes',
                'file_field',
                'student_adress'
                )

    # def clean_room_number(self):
    #     print self.cleaned_data.get('room_number')
    #     room_max = int(RoomInfoModel.objects.get(pk=self.cleaned_data.get('room_number')).room_people)
    #     room_people = len(StudentInfoModel.objects.filter(room_number=self.cleaned_data.get('room_number')))
    #
    #     if room_people <=room_max:
    #         print (room_people, room_max)
    #     else:
    #         raise forms.ValidationError('Room has no quota',code='Room overload')

