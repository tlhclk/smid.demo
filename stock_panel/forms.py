# -*- coding: utf-8 -*-
from django import forms
from .models import FixtureInfoModel,RoomInfoModel


class FixtureInfoForm(forms.ModelForm):

    class Meta:
        model=FixtureInfoModel
        fields=('fixture_no',
                'room_id',
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
