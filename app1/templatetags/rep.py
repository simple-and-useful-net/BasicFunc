from django import template

register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムフィルタとして登録する
@register.filter
def multiply(value1, value2):
    return value1 * value2


@register.filter
def rep_lf(value1):
    s = value1.replace("\r","")
    s = s.replace("\n","_")
    return s

# カスタムタグとして登録する
@register.simple_tag
def url_ex( val1, val2 ):
    return f"<a href= '{val1}{val2}' >[削除]</a>"

# カスタムタグとして登録する
@register.simple_tag
def testStr():
    return "abcdefg"


# カスタムタグとして登録する
@register.simple_tag
def dispEx( val1, val2, val3, val4, val5 ):
    s ="<table>"
    for i in val1:
        p = i.__dict__

        s += "A<tr>"
        s += f"<td><a href={val2}{ p['id'] }/>{val3}</a>"
        s += f"<a href={val4}{ p['id'] }/>{val5}</a></td>"
        s += f'<td><b>{ p["item"] }</b></td><td>  { p["price"] }円 </td> <td> { p["notes"] } </td>'
        s += "</tr>"

    s +="</table>"
    return s

@register.filter
def dispFl( val1 ):
    s ="<table>"
    for i in val1:
        p = i.__dict__
        s += "<tr>"
        s += f'<td><b>{ p["item"] }</b></td><td>  { p["price"] }円 </td> <td> { p["notes"] } </td>'
        s += "</tr>"

    s +="</table>"
    return s
