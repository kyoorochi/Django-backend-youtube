from django.shortcuts import render
from rest_framework.views import APIView
from .models import (ChatRoom, ChatMessage)
from .serializers import (ChatRoomSerializer, ChatMessageSerializer)
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import (get_object_or_404, render)

# Create your views here.
# ChatRoom
## (1) ChatRoomList
### [GET]: 전체 채팅방 조회 // AUTH - request.user
### [POST]: 채팅방 생성

class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all() # objects -> json (직렬화)
        serializer = ChatRoomSerializer(chatrooms, many=True)

        return Response(serializer.data) # 200

    def post(self, request):
        user_data = request.data # 유저가 보내준 데이터
        serializer = ChatRoomSerializer(data=user_data)
        print(user_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # 데이터 저장 성공        
        return Response(serializer.errors) # 데이터 저장 실패
        

## (2) ChatRoomDetail
# api/v1/chat/{room_id}
### [PUT]: 채팅방 관련 수정 (방제, 인원수 제한 외)
### [DELETE]: 방폭


# ChatMessage
## (1) ChatMessageList
# api/v1/chat/{room_id}/messages
### [GET]: 채팅방의 전체 채팅내역 조회
### [POST]: 메세지 송신 (채팅 메세지 생성)
def chat_html(request):
    return render(request, 'index.html') # html 뿌려주는 역할

class ChatMessageList(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)

        # 직렬화
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, room_id):
        user_data = request.data
        chatroom = get_object_or_404(ChatRoom, id=room_id)

        serializer = ChatMessageSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(room=chatroom, sender=request.user)

        return Response(serializer.data, 201)