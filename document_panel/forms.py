# -*- coding: utf-8 -*-
from django import forms
from .models import DocumentInfoModel

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