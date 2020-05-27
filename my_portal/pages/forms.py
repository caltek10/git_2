from django import forms

"""
    text = models.TextField()
    page = models.ForeignKey(Pages, null=True, blank=True, on_delete=models.CASCADE)
"""

class CommentForm(forms.Form):
    text = forms.CharField(label='Текст комментария', max_length=250)
    page = forms.IntegerField(label='id страницы')
