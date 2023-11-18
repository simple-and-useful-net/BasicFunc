from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from .models import PkMnyNote

class MyModelCreateViewTest(TestCase):

    def test_test( self ):

        mny = PkMnyNote.objects.create( item="弁当",price=600, notes="") 

        id=1
        mny = PkMnyNote.objects.get( pk = id) 
        print(mny)
        print(mny.item)
        print(mny.price)


    def test_create_view2(self):
        print("test2")

    def test_create_view3(self):
        print("test3")


    def test_create_view_get(self):
        print("test1")

        # createビューにPOSTリクエストを送信
        response = self.client.get('/app1/create3/')

        html = response.content.decode("utf-8")
        print( "status_code=", response.status_code)
        print( "html=",html)


    def test_create_view(self):
        print("test1")
        # テスト用のデータ
        data = {'item': 'Test Name', 'price': 510, 'notes': 'Description'}

        # createビューにPOSTリクエストを送信
        response = self.client.post('/app1/create3/', data)

        print( "status_code=", response.status_code)

        html = response.content.decode("utf-8")
        print( html)

        print( PkMnyNote.objects.all().values() )
        self.assertEqual(PkMnyNote.objects.count(), 1)




    def tearDown( self ):
        print("start---------------------")
        print( PkMnyNote.objects.all().values() )
        print("end")

