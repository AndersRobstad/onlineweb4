# -*- coding: utf8 -*-
#
# Created by 'myth' on 10/18/15

from tastypie.resources import ModelResource

from apps.gallery.models import ResponsiveImage


class ImageResource(ModelResource):

    def dehydrate(self, bundle):
        bundle.data['original'] = bundle.data['image_original']
        bundle.data['wide'] = bundle.data['image_wide']
        bundle.data['lg'] = bundle.data['image_lg']
        bundle.data['md'] = bundle.data['image_md']
        bundle.data['sm'] = bundle.data['image_sm']
        bundle.data['xs'] = bundle.data['image_xs']

        del(bundle.data['image_original'])
        del(bundle.data['image_wide'])
        del(bundle.data['image_lg'])
        del(bundle.data['image_md'])
        del(bundle.data['image_sm'])
        del(bundle.data['image_xs'])

        return bundle

    class Meta(object):
        queryset = ResponsiveImage.objects.all()
        resource_name = 'image'
        fields = [
            'name',
            'description',
            'timestamp',
            'image_original',
            'image_thumbnail',
            'image_wide',
            'image_lg',
            'image_md',
            'image_sm',
            'image_xs'
        ]
