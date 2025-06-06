from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Users, Tasks
from .serializers import UsersSerializer, Taskserializers
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


# Create your views here.
class MarkTaskCompleteView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = Taskserializers

    def patch(self, request, pk):
        try:
            task = Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            return Response({'error: Task not found'})

        if task.Status == 'COMPLETED':
            return Response({'error: Task is already completed'}, status=status.HTTP_400_BAD_REQUEST)

        elif task.User != self.request.user:
            return Response({'error: You are not Authorised'}, status=status.HTTP_400_BAD_REQUEST)

        task.Status = 'COMPLETED'
        task.Completed_at = timezone.now()
        task.save()

        return Response({'message': 'Task marked as completed.', 'completed_at': task.Completed_at}, status=status.HTTP_200_OK)


class MarkTaskInCompleteView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = Taskserializers
    queryset = Tasks.objects.all()

    def patch(self, request, pk):
        try:
            task = Tasks.objects.get(pk=pk)

        except Tasks.DoesNotExist:
            return Response({'error: Task not found'})

        if task.Status == 'PENDING':
            return Response({"error": "Task is not marked as complete."}, status=status.HTTP_400_BAD_REQUEST)

        elif task.User != self.request.user:
            return Response({'error: You are not Authorised'}, status=status.HTTP_400_BAD_REQUEST)

        task.Status = 'PENDING'
        task.Completed_at = None
        task.save()
        return Response({'message': 'Task marked as incompleted.'}, status=status.HTTP_200_OK)


class UserCreateView(generics.CreateAPIView):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer


class UserDetailsView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UsersSerializer

    def get_queryset(self):
        # Filter the queryset to return only the authenticated user's details
        return Users.objects.filter(pk=self.request.user.pk)


class UserlistViews(generics.ListAPIView):
    queryset = Users.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UsersSerializer


class UserDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = UsersSerializer

    def get_queryset(self):
        return Users.objects.filter(pk=self.request.user.pk)


class TaskCreateView(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = Taskserializers

    def perform_create(self, serializer):
        User = serializer.validated_data['User']
        if User != self.request.user:
            raise PermissionError({'you are not authorised'})
        serializer.save(User=self.request.user)


class TaskListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = Taskserializers
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['Status', 'Priority_Level', 'Due_Date']
    Ordering_fields = ['Due_Date', 'Priority_Level']
    ordering = ['Due_Date']

    def get_queryset(self):
        # Filter the queryset to return only the authenticated user's details
        return Tasks.objects.filter(User=self.request.user)


class TaskDeleteView(generics.DestroyAPIView):
    queryset = Tasks.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = Taskserializers

    def perform_destroy(self, instance):
        if instance.User != self.request.user:
            raise PermissionError({'you do not have the permission'})
        instance.delete()
