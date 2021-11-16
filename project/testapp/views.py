from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def thankyouview(request):
    return render(request,'testapp/news.html')


def feedbackview(request):
    form = forms.FeedbackForm()
    
    if request.method == 'GET':
        return render(request,'testapp/register.html', {'form':form})
    
    if request.method == 'POST':
        form=forms.FeedbackForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            print('student Name:', form.cleaned_data['name'])
            print('student no:', form.cleaned_data['no'])
            print('student email:', form.cleaned_data['email'])
            print('student feedback:', form.cleaned_data['feedback'])
            return thankyouview(request)
#            return render(request,'news/register.html', {'form':form})
    return render(request,'testapp/register.html', {'form':form})
