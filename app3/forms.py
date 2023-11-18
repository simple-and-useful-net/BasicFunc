from django.forms import ModelForm
from app1.models import PkMnyNote

class PkMnyForm( ModelForm ):
	class Meta:
		model = PkMnyNote
		fields = [ "item", "price", "notes" ]
		labels={
				 "item":"費目", "price":"金額", "notes":"ノート"
		}
		
	def __init__( self, *args, **kwargs): 

		read_only = False
		if 'read_only' in kwargs:
			read_only = kwargs.pop('read_only')

		super( PkMnyForm, self).__init__(* args, **kwargs) 
		
		for field in self.fields.values(): 
			field.widget.attrs["class"] = "form-control"
			# field.widget.attrs["readonly"] = "readonly"
			if read_only:
				field.widget.attrs["disabled"] = "disabled"
			field.required=False