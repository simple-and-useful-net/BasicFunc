from django.shortcuts   import render,redirect,get_object_or_404
from django.http        import HttpResponse

# import forms
from .forms import PkMnyForm
from app1.models import PkMnyNote


# ******************************************************
# CURD
# ******************************************************

# 一覧表示
def 一覧表示( request ):
    data =PkMnyNote.objects.all()

    for i in data:
        p = i.__dict__
        print(p["item"], p["price"])
    return render( request, "app3/一覧.html", {"all_data":data} )

# 詳細表示
def 詳細表示( request, pk ):
    data = PkMnyNote.objects.get( pk = pk ) 
    return render( request, "app3/詳細.html", {'detail_data': data})



# -----------------------------------------
# フォーム クラスを使った場合
# -----------------------------------------
def 作成処理( request ):

    # 入力フォームの表示
    if request.method == "GET":

        # テンプレートにフームクラスの「.as_p」を
        # 使用するので「input」タグが無い
        # 
        # <form ～>
        #   {{ form.as_p }}
        # </form>
        fm = PkMnyForm()
        return render( request, "app3/更新.html", {"form":fm, "cre_title":"登録"} )

    # 登録処理
    elif request.method == "POST":

        fm = PkMnyForm( request.POST )
        fm.save()
        return redirect("app3:list_url")
    else:
        pass





# -----------------------------------------
# フォーム クラスを使った場合
# -----------------------------------------
def 更新処理( request, pk ):

    rec = get_object_or_404( PkMnyNote, pk = pk)

    if request.method =="GET":
        # フォーム内の各項目に値を設定する為に、instanceにDBの値を設定
        form = PkMnyForm(instance=rec)
        return render( request, "app3/更新.html", {"form":form} )

    elif request.method =="POST":
        form = PkMnyForm( request.POST, instance=rec )
        form.save()

        return redirect("app3:list_url")
        # return django.http.HttpResponse("OK")

    else:
        pass


# -----------------------------------------
# フォーム クラスを使った場合
# -----------------------------------------
def 削除処理( request, pk ):

    rec = PkMnyNote.objects.get( pk = pk ) 
    # 入力フォームの表示
    if request.method == "GET":
        # フォーム内の各項目に値を設定する為に、instanceにDBの値を設定
        form = PkMnyForm( instance=rec, read_only=True)
        return render( request, "app3/更新.html", {"form":form, "del_title":"削除"} )

    # 削除処理
    elif request.method == "POST":
        rec.delete()
        return redirect("app3:list_url")

    else:
        pass




