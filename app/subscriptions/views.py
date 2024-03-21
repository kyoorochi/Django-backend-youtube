from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer

# Create your views here.
# 구독관련 REST API

# SubscriptionList
# api/v1/subscription
# [POST] : 구독하기
class SubscriptionList(APIView):
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
    def get(self, request):
        pass

# [DELETE] : 구독취소
    def delete(self, request):
        pass
