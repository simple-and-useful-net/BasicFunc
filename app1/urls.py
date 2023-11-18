from django.urls import path
from . import views
# import views
app_name ="app1"

urlpatterns = [

    path("",                        views.menu  ),

    path("list/",                   views.一覧表示,         name="list_url" ),
    path("delete/<int:pk>/",        views.削除処理,         name="delete_url" ),
    path("detail/<int:pk>/",        views.詳細表示,         name="detail_url" ),

    path("create/",                 views.create,           name="create_url" ),
    path("create_post/",            views.create_post,      name="create_post_url" ),

    path("update/<int:pk>/",        views.update,           name="update_url" ),
    path("update_post/<int:pk>/",   views.update_post,      name="update_post_url" ),

]