#path関数をインポート
from django.urls import path

#views.py関数をインポート
from . import views

urlpatterns = [
    path("",views.index, name = "index"),#viewsのindex関数を呼び出す
]

