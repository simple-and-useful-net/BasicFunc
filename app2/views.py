from django.shortcuts   import render,redirect,get_object_or_404
from django.http        import HttpResponse

# import forms
from app1.models import PkMnyNote



# 一覧表示
def 一覧表示( request ):
    data =PkMnyNote.objects.all()
    return render( request, "app2/一覧.html", {"items":data} )

# 詳細表示
def 詳細表示( request, pk ):
    data = PkMnyNote.objects.get( pk = pk ) 
    return render( request, "app2/詳細.html", {'detail_data': data})



# -----------------------------------------
# フォーム クラスなしの場合
# -----------------------------------------
def 作成処理( request ):

    # 入力フォームの表示
    if request.method == "GET":
        # テンプレートには通常の「input」タグあり
        # 
        # <form>
        #   <label for="item">費目:</label>
        #   <input type="text" name="item">
        #   ～
        # </form>
        print("処理まとめで input-tag使用")
        return render( request, "app2/登録.html")

    # 登録処理
    elif request.method == "POST":

        rec = PkMnyNote()
        rec.item  = request.POST.get("item")
        rec.price = request.POST.get("price")
        rec.notes = request.POST.get("notes")
        rec.save()

        return redirect("app2:list_url")
    else:
        pass



# -----------------------------------------
# フォーム クラスなしの場合
# -----------------------------------------
def 更新処理( request, pk ):

    rec = get_object_or_404( PkMnyNote, pk = pk)
    # rec = PkMnyNote.objects.get(pk=pk)

    if request.method =="GET":
        return render( request, "app2/更新.html", {"form":rec} )
        # pass

    elif request.method =="POST":
        rec.item = request.POST.get("item")
        rec.price= request.POST.get("price")
        rec.notes= request.POST.get("notes")
        rec.save()
        # return redirect("app2:list_url")
        link_url ="/app2/list"
        return HttpResponse("OK" + "<br><a href='%s'>一覧</a>" %link_url)

    else:
        pass

