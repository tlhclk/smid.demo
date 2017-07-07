from django import forms
from .models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonLeaveModel,DocumentInfoModel,EntranceLeaveModel,LiabilityInfoModel
from fixturepanel.models import RoomInfoModel

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model=StudentInfoModel
        fields=(
                'id',
                'student_position',
                'student_tcn',
                'student_name',
                'student_lastname',
                'student_phone',
                'student_email',
                'student_birthday',
                'student_regday',
                'student_city',
                'student_town',
                'room_number',
                'student_type',
                'birth_place',
                'school_name',
                'education_year',
                'blood_type',
                'health_notes',
                'special_notes',
                'file_field',
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

class PersonLeaveForm(forms.ModelForm):
    class Meta:
        model=PersonLeaveModel
        fields=('leave_id',
                'leave_start',
                'leave_end',
                'leave_person_id',
                'leave_reason',
                )

class DocumentInfoForm(forms.ModelForm):
    class Meta:
        model=DocumentInfoModel
        fields=['document_id',
                'person_id',
                'document_type',
                'document_description',
                'document_date',
                'document_image',
                ]

class EntranceLeaveForm(forms.ModelForm):
    in_list=[('1','in'),('2','out')]
    in_or_out= forms.TypedChoiceField(choices=in_list,widget=forms.RadioSelect,coerce=str)
    class Meta:
        model=EntranceLeaveModel
        fields=['person_id',
                'traffic_date',
                'in_or_out']

class LiabilityInfoForm(forms.ModelForm):
    class Meta:
        model=LiabilityInfoModel
        fields=['record_no',
                'person_id',
                'liability_type',
                'liability_name',
                'liability_desc',
                'liability_date',
                'liability_return',
                'liability_lastday',
                'liability_penalty',

                ]