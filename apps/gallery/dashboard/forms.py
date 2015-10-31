# -*- coding: utf8 -*-
#
# Created by 'myth' on 10/24/15

from django import forms

from taggit.forms import TagWidget

from apps.gallery.models import ResponsiveImage


class ResponsiveImageForm(forms.ModelForm):

    class Meta(object):
        model = ResponsiveImage
        fields = ['name', 'description', 'tags']
        widgets = {
            'tags': TagWidget(attrs={
                'placeholder': u'Eksempel: kontoret, kjelleren, åre',
            })
        }
        labels = {
            'tags': u'Tags'
        }
