from django.db.models import Q

from rest_framework.response import Response

from rest_framework.generics import GenericAPIView

from .models import Todo
from .serializer import TodoSerializer
from rest_framework.permissions import IsAuthenticated


class TodoAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = TodoSerializer

    def get(self, request):
        todos = Todo.objects.all()
        todos_data = TodoSerializer(todos, many=True)
        return Response(todos_data.data)


class CreateTodoAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def post(self, request):
        todo_serializer = TodoSerializer(data=request.data)
        todo_serializer.is_valid(raise_exception=True)
        todo_serializer.save()
        return Response(todo_serializer.data)


class TodoUpdateAPIView(GenericAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request, pk):
        title = request.data.get('text', None)
        todo = Todo.objects.get(Q(pk=pk) & Q(owner_id=request.user))
        if title:
            todo.text = title
            todo.save()
        todo_serializer = TodoSerializer(todo)
        return Response(todo_serializer.data)

    def delete(self, request, pk):
        Todo.objects.get(pk=pk).delete()
        return Response(status=204)
