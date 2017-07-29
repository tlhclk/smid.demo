# -*- coding: utf-8 -*-
from django import forms
from .models import DocumentInfoModel,LiabilityInfoModel

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

class LiabilityInfoForm(forms.ModelForm):
    class Meta:
        model = LiabilityInfoModel
        fields = [#'record_no',
                  'person_id',
                  'liability_type',
                  #'liability_name',
                  'liability_desc',
                  'liability_date',
                  'liability_return',
                  'liability_lastday',
                  'liability_penalty',
                  ]