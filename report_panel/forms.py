# -*- coding: utf-8 -*-
from django import forms
from account_panel.models import AccountInfoModel,TransactionInfoModel
from person_panel.models import StudentInfoModel

class FilterAccountForm(forms.Form):#TODO html ve javaya aktarılacak ajax ile birlikte
    month_list=[('',''),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12')]
    day_list=[('',''),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31')]
    account_no=forms.ModelChoiceField(AccountInfoModel.objects.all(),widget=forms.Select(attrs={"class":"select2"}),required=False)
    year=forms.CharField(widget=forms.DateInput(attrs={"format": "yyyy","class":"date-picker"}),required=False)
    month=forms.ChoiceField(choices=month_list,required=False)
    day=forms.ChoiceField(choices=day_list,required=False)
    transaction_type=forms.ChoiceField(choices=TransactionInfoModel.transaction_type_list,widget=forms.Select,required=False)
    student_id=forms.ModelChoiceField(StudentInfoModel.objects.all(),widget=forms.Select,required=False)
    deposito=forms.BooleanField(required=False)

