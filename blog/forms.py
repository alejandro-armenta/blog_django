from django import forms
from .models import Comment


class CommentBoundField(forms.BoundField):

    comment_class = "comment"

    #esto es para agregar mas clases css
    def css_classes(self, extra_classes=None):

        result = super().css_classes(extra_classes)

        if self.comment_class not in result:
            result += f" {self.comment_class}"

        return result.strip()


class CommentForm(forms.ModelForm):
    
    bound_field_class = CommentBoundField

    class Meta:
        model = Comment
        fields = ["name", "email", "body"]


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
