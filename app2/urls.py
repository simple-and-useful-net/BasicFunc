from django.urls import path
from . import views

app_name = "app2"

urlpatterns = [

    path("list/",                   views.一覧表示,       name="list_url" ),
    path("detail/<int:pk>/",        views.詳細表示,       name="detail_url" ),

    path("create/",                 views.作成処理,       name="create_url" ),
    path("update/<int:pk>/",        views.更新処理,       name="update_url" ),
    # path("delete/<int:pk>/",        views.削除処理,       name="delete_url" ),
]