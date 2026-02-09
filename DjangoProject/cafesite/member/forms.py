from django import forms

class LoginForm(forms.Form): # 로그인 폼에서 사용할 화면을 위한 Form 클래스 정의
    email = forms.EmailField(label='이메일', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'이메일을 입력해 주세요.'}))

    password = forms.CharField(label='비밀 번호', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'비밀 번호를 입력해 주세요.'}))
