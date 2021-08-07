from rest_framework import serializers
from .models import Postulations
from coupon.models import Coupon
import random

def get_promo_code(num_chars):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code
        
class PostulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulations
        fields = ['id', 'username', 'phone', 'email', 'product', 'coupon']

    def create(self, data):
        promo_code = get_promo_code(5)
        postulationsCreate = Postulations.objects.model(username=self.data['username'], phone=data['phone'], email=self.data['email'], product=data['product'], coupon=promo_code)
        postulationsCreate.save()

        couponX = Coupon.objects.model(email=self.data['email'], code=promo_code)
        couponX.save()
        return couponX, postulationsCreate