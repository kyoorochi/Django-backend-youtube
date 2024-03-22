from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer
from .models import Subscription
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
# 구독관련 REST API

# SubscriptionList
# api/v1/subscription
# [GET] : pk = 나 자신, (pk 입력 받을 필요 없음)
# [POST] : 구독하기
class SubscriptionList(APIView):
    # 내가 구독한 유튜버(들) 리스트 조회
    def get(self, request):
        subs = Subscription.objects.filter(subscriber=request.user)
        serializer = SubSerializer(subs, many=True) # objects -> json

        return Response(serializer.data)

    def post(self, request):
        user_data = request.data # json -> object (Serializer)
        serializer = SubSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, 201)

# SubscriptionDetail
# api/v1/subscription/{user_id}
# [GET] : 특정 유저의 구독자 리스트 조회
class SubscriptionDetail(APIView):
    def get(self, request, pk):
        subs = Subscription.objects.filter(subscribed_to=pk) # objects -> json
        serializer = SubSerializer(subs, many=True)

        return Response(serializer.data)

# [DELETE] : 구독취소
    def delete(self, request, pk):
        sub = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        sub.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)