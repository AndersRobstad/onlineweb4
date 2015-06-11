from django.contrib import admin

from django.contrib import admin
from django.contrib.contenttypes import generic

from apps.payment.models import Payment
from apps.payment.models import PaymentRelation
from apps.payment.models import PaymentDelay
from apps.payment.models import PaymentPrice


class PaymentInline(generic.GenericStackedInline):
    model = Payment
    extra = 0
    classes = ('grp-collapse grp-open',)  # style
    inline_classes = ('grp-collapse grp-open',)  # style
    exclude = ("added_date", "last_changed_date", "last_changed_by")

    #TODO add proper history updates in dashboard
    #def save_model(self, request, obj, form, change):
    #    obj.last_changed_by = request.user
    #    obj.save()


class PaymentPriceInline(admin.StackedInline):
    model = PaymentPrice
    extra = 0
    classes = ('grp-collapse grp-open',)  # style
    inline_classes = ('grp-collapse grp-open',)  # style

class PaymentAdmin(admin.ModelAdmin):
    inlines = (PaymentPriceInline, )
    model = Payment
    list_display = ('__unicode__', 'stripe_key_index', 'payment_type')

class PaymentRelationAdmin(admin.ModelAdmin):
    model = PaymentRelation
    list_display = ('__unicode__', 'refunded')
    exclude = ('stripe_id',)

class PaymentDelayAdmin(admin.ModelAdmin):
    model = PaymentDelay
    list_display = ('__unicode__', 'valid_to', 'active')

admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentRelation, PaymentRelationAdmin)
admin.site.register(PaymentDelay, PaymentDelayAdmin)
