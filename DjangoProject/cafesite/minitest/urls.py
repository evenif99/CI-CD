from django.urls import path

from minitest import views

app_name = 'minitest'

# App url 파일 : minitest App에서만 사용하는 url 경로 지정파일입니다.
urlpatterns = [
    path('fruit/', views.fruit, name='fruit'), # http://127.0.0.1:8000/minitest/fruit/
    path('fruit/list', views.fruit_list, name='fruit_list'), # http://127.0.0.1:8000/minitest/fruit/list/
]