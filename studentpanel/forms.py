from django import forms
from .models import StudentInfoModel,ParentInfoModel

class StudentInfoForm(forms.ModelForm):

    class Meta:
        model=StudentInfoModel
        fields=('student_tcn',
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

class ParentInfoForm(forms.ModelForm):
    class Meta:
        model=ParentInfoModel
        fields=('student_id',
                'parent_name',
                'parent_lastname',
                'parent_TCN',
                'parent_phone',
                'parent_email',
                'relative_degree',
                'parent_job',
                )


# sehirler
# oda listesi
# okul adi

class ParentEditForm(forms.Form):
    pass