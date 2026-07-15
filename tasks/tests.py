from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task


class TaskAPITest(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="Test@123"
        )

        # Authenticate the user
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        data = {
            "title": "Test Task",
            "description": "Testing Task API",
            "completed": False
        }

        response = self.client.post("/api/tasks/", data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, "Test Task")

    def test_get_tasks(self):
        Task.objects.create(
            title="Sample Task",
            description="Testing",
            completed=False,
            owner=self.user
        )

        response = self.client.get("/api/tasks/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_task(self):
        task = Task.objects.create(
            title="Old Title",
            description="Old Description",
            completed=False,
            owner=self.user
        )

        data = {
            "title": "New Title",
            "description": "Updated Description",
            "completed": True
        }

        response = self.client.put(
            f"/api/tasks/{task.id}/",
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        task.refresh_from_db()

        self.assertEqual(task.title, "New Title")
        self.assertEqual(task.completed, True)

    def test_delete_task(self):
        task = Task.objects.create(
            title="Delete Me",
            description="Delete Test",
            completed=False,
            owner=self.user
        )

        response = self.client.delete(f"/api/tasks/{task.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)