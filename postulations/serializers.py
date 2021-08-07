from rest_framework import serializers
from .models import Postulations
from coupon.models import Coupon


class PostulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulations
        fields = ['id', 'username', 'phone', 'email', 'product', 'coupon']

    def create(self, data):
        postulationsCreate = Postulations.objects.model(username=self.data['username'], phone=data['phone'], email=self.data['email'], product=data['product'], coupon=data['coupon'])
        postulationsCreate.save()

        couponX = Coupon.objects.model(email=self.data['email'], code=data['coupon'])
        couponX.save()
        return couponX, postulationsCreate