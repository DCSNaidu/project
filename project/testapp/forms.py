# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 15:19:03 2021

@author: ADMIN
"""

from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField()
    no=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget = forms.Textarea)
