from django import forms
from .models import FixtureInfoModel,RoomInfoModel,LiabilityInfoModel


class FixtureInfoForm(forms.ModelForm):

    class Meta:
        model=FixtureInfoModel
        fields=('fixture_no',
                'room_no',
                'fixture_type',
                'fixture_notes',
                'fixture_image'
                )

class RoomInfoForm(forms.ModelForm):
    class Meta:
        model=RoomInfoModel
        fields=('room_no',
                'room_floor',
                'room_people',
                'room_type',
                'room_desc',
                'room_image'
                )

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