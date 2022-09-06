from pdb import post_mortem
from django import forms
from posts.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'description', 'image')

    def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)
