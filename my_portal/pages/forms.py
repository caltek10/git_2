from django import forms

"""
    text = models.TextField()
    page = models.ForeignKey(Pages, null=True, blank=True, on_delete=models.CASCADE)
"""

class CommentForm(forms.Form):
    text = forms.CharField(label='Текст комментария', max_length=250)
    page = forms.IntegerField(label='id страницы')

    def clean_page(self):
        page_id = self.cleaned_data['page']
        if not Pages.objects.filter(pk=self.cleaned_data['page']).exist():
            raise forms.ValidationError("Page with id = %s doesn't exist." % self.cleaned_data['page'])

        return page_id
