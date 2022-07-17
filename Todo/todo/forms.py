from django import forms
from .models import Todo

#form: 페이지 요청 시 전달되는 파라미터들을 관리하기 우해 사용하는 클래스
#forms.ModelForm: model과 연결된 폼, 폼을 저장하면 연결된 모델의 데이터를 저장할 수 있는 폼
#forms.ModelForm은 이너클래스 Meta가 필요 (사용할 모델, 모델의 속성)
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')
