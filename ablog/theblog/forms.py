from django import forms
from . models import Post, Category, Comment

#=choices=[('coding','coding'),('sports','sports')]
choices=Category.objects.all().values_list('name','name')
choices_list=[]
for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ('title','title_tag','header_image','author','category','body','snippet')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title-tag'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            #'author':forms.Select(attrs={'class':'form-control',}),
            'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Start writing now'}),
            'snippet':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter snippet for your blog'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ('title','title_tag','header_image','category','body','snippet')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title-tag'}),
            'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Start writing now'}),
            'snippet':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter snippet for your blog'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields= ('name','body')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Write your view'}),
        }