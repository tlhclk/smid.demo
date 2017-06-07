# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.models import User,Group,Permission,ContentType


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Boyle bir kullanici yok")
            if not user.check_password(password):
                raise forms.ValidationError("Sifre yanlis veya eksik")

            return super(UserLoginForm, self).clean()

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email Adresi')
    password = forms.CharField(widget=forms.PasswordInput, label='Sifre',max_length=200)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Sifre Onay',max_length=200)
    groups = []
    groups1 = Group.objects.all()
    for gro in groups1:
        groups.append((gro.id, gro.name))
    group_choice = forms.ChoiceField(label='Group', choices=groups, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'password2',
            'email',
            'group_choice',
        ]

    def clean_password(self):
        email = self.cleaned_data.items()
        print email
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        print password, password2
        # if password != password2:
        # raise forms.ValidationError("Sifreler ayni olmali")
        return self.cleaned_data

class PermissionForm(forms.ModelForm):
    content_list = []
    for content in ContentType.objects.all():
        content_list.append((content.id, content.name))
    content_type_id = forms.ChoiceField(label='Content', choices=content_list, required=False)
    codename = forms.CharField(label='Permission Codename')
    name = forms.CharField(label='Permission Description')
    class Meta:
        model=Permission
        fields=['content_type_id','codename','name',]
    def clean(self):
        content = self.cleaned_data.get('content_type_id')
        permission_c = self.cleaned_data.get('codename')
        permission_list = Permission.objects.filter(content_type=content)
        for permis in permission_list:
            if permis.codename == permission_c:
                raise forms.ValidationError(
                    'There is a permission in selected content: %s, %s' % (content, permission_c))
        return self.cleaned_data

class UserGroupForm(forms.Form):
    pass

class UserPermissionForm(forms.Form):
    permission_list = []
    for per in Permission.objects.all():
        permission_list.append((per.id, per.name))
    user_list = []
    for user in User.objects.all():
        user_list.append((user.id, user.username))

    user_choice = forms.ChoiceField(label='User', choices=user_list, required=False)
    permission_choice = forms.MultipleChoiceField(label='Permission', widget=forms.CheckboxSelectMultiple,choices=permission_list, required=False)

    def clean_permission_choice(self):
        user_id = self.cleaned_data.get('user_choice')
        permission_list = self.cleaned_data.get('permission_choice')
        user = User.objects.get(pk=user_id)
        for per in permission_list:
            if user.has_perm(per):
                raise forms.ValidationError('user already has the permission %s' % per)
        return user_id, permission_list

class GroupPermissionForm(forms.Form):
    permission_list = []
    for per in Permission.objects.all():
        permission_list.append((per.id, per.name))
    group_list = []
    for group in Group.objects.all():
        group_list.append((group.id, group.name))

    group_choice = forms.ChoiceField(label='Group', choices=group_list, required=False)
    permission_choice = forms.MultipleChoiceField(label='Permissions', widget=forms.CheckboxSelectMultiple,choices=permission_list, required=False)

    def clean_permission_choice(self):
        group_id = self.cleaned_data.get('group_choice')
        permission_list = self.cleaned_data.get('permission_choice')
        kullanici = Group.objects.get(pk=group_id)
        for per in permission_list:
           if kullanici.has_perm(per):
               raise forms.ValidationError('user already has the permission %s'%per)
        return group_id, permission_list

class RemoverForm(forms.Form):
    remover_list = [(1, 'User'), (2, 'Permission'), (3, 'Group')]

    user_list = []
    group_list = []
    permission_list = []

    for user in User.objects.all():
        user_list.append((user.id, user.username))
    for permission in Permission.objects.all():
        permission_list.append((permission.id, permission.name))
    for group in Group.objects.all():
        group_list.append((group.id, group.name))

    remover_choice = forms.ChoiceField(label='Remove Choice', choices=remover_list, required=True)
    user_choice = forms.ChoiceField(label='User', choices=user_list, required=False)
    permission_choice = forms.ChoiceField(label='Permission', choices=permission_list, required=False)
    group_choice = forms.ChoiceField(label='Group', choices=group_list, required=False)