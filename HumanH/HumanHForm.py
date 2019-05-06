from django import forms
from .models import Tutorial as T


class HumanHForm(forms.ModelForm):
	"""docstring for """
	class Meta:
		model = T
		fields = [
			'title',
			'content',
			'tutorial_published'
		]