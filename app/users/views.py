from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import ToDoItem
from .serializers import ToDoItemSerializer
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
from .serializers import UserSignupSerializer, ToDoItemSerializer
# from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer


class ToDoItemCreateListView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoItemSerializer

    def get(self, request, pk=None):

        if not pk:
            user = request.user
            todos = ToDoItem.objects.filter(user=user)
            serializer = ToDoItemSerializer(todos, many=True)
            return Response({
                'status': True,
                'data': serializer.data,
                'message': 'todo fetched successfully'
            })
            
        else:
            user = request.user
            todo = ToDoItem.objects.filter(user=user, id=pk).first()
            serializer = ToDoItemSerializer(todo)
            return Response({
                'status': True,
                'data': serializer.data,
                'message': 'ToDoItem fetched successfully'
            })

    def post(self, request):
        try:
            user = request.user
            data = request.data
            data['user'] = user.id
            serializer = ToDoItemSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'invalid fields',
                    'data': serializer.errors
                })

            serializer.save()
            return Response({
                'status': True,
                'messsage': 'Todo is created',
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {'error_message': str(e)}
            })

    def delete(self, request, pk):
        try:
            todo_id = pk

            todo = ToDoItem.objects.filter(
                id=todo_id, user=request.user).first()

            if not todo:
                return Response({
                    'status': False,
                    'message': 'Invalid ID or unauthorized',
                    'data': {}
                }, status=status.HTTP_404_NOT_FOUND)
            
            if todo.image:
                todo.image.delete()

            todo.delete()

            return Response({
                'status': True,
                'message': 'Todo is deleted successfully',
                'data': {}
            })

        except Exception as e:
            return Response({
                'status': False,
                'message': 'Something went wrong',
                'data': {'error_message': str(e)}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            data = request.data
            obj = ToDoItem.objects.filter(id=pk).first()
            previous_image = obj.image if obj.image else None
            if 'image' in data and previous_image:
                previous_image.delete(save=True)


            serializer = ToDoItemSerializer(obj, data=data, partial=True)
            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'invalid fields',
                    'data': serializer.errors
                })
            
            serializer.save()

            return Response({
                'status': True,
                'messsage': 'Todo is created',
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {'error_message': str(e)}
            })