from django.shortcuts   import render,redirect,get_object_or_404
from django.http        import HttpResponse

# import forms
from .forms import PkMnyForm
from .models import PkMnyNote


def index( response ):
    return HttpResponse("こんにちは!")

def test( response ):
    # return django.http.HttpResponse("testと表示されましたか？")
    return render( response, "app1/index.html")

# ******************************************************
# CURD
# ******************************************************
# メニュー表示（テンプレートファイルを使わない）
def menu( response ):

    menu_str ="""
        <h1>***　メニュー　***</h1>
        
        <a href="/app1/list/">一覧表示</a>
        <br>
        <a href="/app1/create/">新規作成</a>
        <br>
        <br>

        <a href="{% url 'list_url' %}">一覧表示　( urls.pyのname 使用 )</a>
        <br>
        <a href="{% url 'create_url' %}">新規作成　( urls.pyのname 使用 )</a>
        <br>
    """

    return render( response, "app1/menu.html")
    # return django.http.HttpResponse( menu_str )


# 一覧表示
def 一覧表示( request ):
    data =PkMnyNote.objects.all()
    return render( request, "app1/一覧表示.html", {"items":data} )

# 詳細表示
def 詳細表示( request, pk ):
    data = PkMnyNote.objects.get( pk = pk ) 
    return render( request, "app1/詳細表示.html", {'detail_data': data})

# レコード削除
def 削除処理( request, pk ):
    rec = PkMnyNote.objects.get( pk = pk ) 
    rec.delete()
    return redirect("app1:list_url")


    # 入力フォームの表示
    if request.method == "GET":

        # フォーム内の各項目に値を設定する為に、instanceにDBの値を設定
        kodukai = get_object_or_404( PkMnyNote, pk = pk)
        form = PkMnyForm( instance=kodukai, read_only=True)
        print("form-type    ->",type(form) )
        print("form         =>",form        )
        return render( request, "更新.html", {"form":form, "pk":pk, "del_title":"削除"} )

        kodukai = get_object_or_404( PkMnyNote, pk = pk)
        print("form===>",kodukai)
        return render( request, "更新0.html", {"form":kodukai, "pk":pk} )

        kodukai = get_object_or_404( PkMnyNote, pk = pk)




    # 処理
    elif request.method == "POST":


        rec = PkMnyNote.objects.get( pk = pk ) 
        rec.delete()
        return redirect("list_url")
    else:
        pass



# -----------------------------------------
# フォーム クラスなしの場合
# -----------------------------------------
# 新規登録（登録フォームを表示）
def create( request ):
    print("入力フォーム表示")

    return render( request, "app1/create.html")

# 新規登録（登録処理）
def create_post( request ):
    print("入力データ登録")

    mdl = PkMnyNote()
    mdl.item  = request.POST.get("item")
    mdl.price = request.POST.get("price")
    mdl.notes = request.POST.get("notes")
    mdl.save()
    return redirect("app1:list_url")


# -----------------------------------------
# フォーム クラスなしの場合
# -----------------------------------------
def update( request, pk ):
    rec = PkMnyNote.objects.get( pk = pk ) 

    return render( request, "app1/update.html", {"form":rec, "pk":pk} )


def update_post( request, pk ):
    rec = PkMnyNote.objects.get( pk = pk ) 

    rec.item = request.POST.get("item")
    rec.price= request.POST.get("price")
    rec.notes= request.POST.get("notes")
    rec.save()

    return redirect("app1:list_url")
    # return django.http.HttpResponse("OK")






