from django import forms
from django.forms import widgets
from .models import Home, People_data, activity_data

from django.utils.translation import gettext_lazy as _
from django.db import models
# from django.forms import ModelChoiceField
from django.core import validators


class login_form(forms.Form):

    user_name = forms.CharField(label='請輸入帳號', )
    password = forms.CharField(label='請輸入密碼', widget=forms.PasswordInput)


class choose_form(forms.Form):
    activity_ID = forms.ModelChoiceField(label="請選擇活動名稱",initial=1,
        queryset=activity_data.objects.all()
    )

class find_home(forms.Form):
    homephone = forms.CharField(label="輸入家庭電話", max_length=20, required=False)


class activity_form(forms.Form):
    name = forms.CharField(label="活動名稱", required=False)
    x_file = forms.FileField(label="檔案上傳", required=False)
    use_table = forms.CharField(label="請輸入要使用的欄位格式,欄位格式之間已、符號分隔。欄位格式為 欄位名稱_是否連接出生年月日。 範:光明燈_F ", required=False)
    # required=False

    # class Meta:
    #     model = activity_data
    #     fields = '__all__'


class homeform(forms.Form):
    address = forms.CharField(label="地址")
    phone = forms.CharField(label="家庭電話",
                            validators=[
                                validators.RegexValidator(
                                    "^\d{2}-?\d{3}-?\d{4}$",
                                    message='請輸入正確格式的電話號碼！')
                            ])


class peopleform(forms.Form):
    name = forms.CharField(required=False, label="輸入香客名稱",max_length=20)
    birthday = forms.DateTimeField(
        label="生日",
        required=False,
        widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    gender = forms.ChoiceField(label='性別',
                               required=False,
                               choices=(('male', '男'), ('female', '女')),
                               initial="男",
                               widget=forms.widgets.Select())
    # homephone = forms.CharField(
    #     label="輸入家庭電話"
    # )


# queryset=Home.objects.all().values_list(
#            'id', 'home_phone')