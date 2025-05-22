from django.urls import reverse
from django.test import TestCase, Client
from workspace.models import (
    Task,
    TaskType,
    Team,
    Worker,
)

class PublicTasksTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task_type = TaskType.objects.create(name="Test")
        self.task = Task.objects.create(
            name='Test',
            deadline='2023-12-31T23:59:59Z',
            is_complete=False,
            priority='MD',
            task_type=self.task_type
        )


    def test_login(self):
        url = reverse("workspace:task-detail", args=[self.task.id])
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)


class TestToggleTaskStatusView(TestCase):
    def setUp(self):
        self.user =  Worker.objects.create_user(username="test", password="1234")
        self.task_type = TaskType.objects.create(name="Test")
        self.task = Task.objects.create(
            name="Test",
            description="Test",
            deadline="2023-12-31T23:59:59Z",
            is_complete=False,
            priority='MD',
            task_type=self.task_type,
        )
        self.task.assignees.add(self.user)
        self.client.login(username="test", password="1234")

    def test_toggle_status_complete(self):
        url = reverse("workspace:toggle-status", args=[self.user.id, self.task.id])
        response = self.client.post(url)

        self.task.refresh_from_db()

        self.assertTrue(self.task.is_complete)

        self.assertEqual(response.status_code, 302)


class DeleteMemberTeamView(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.member = Worker.objects.create_user(username="test", password="<PASSWORD>")
        self.team.members.add(self.member)
        self.client.login(username="test", password="<PASSWORD>")

    def test_delete_team_member(self):
        url = reverse("workspace:remove-member", args=[self.team.id, self.member.id])
        response = self.client.post(url)
        self.member.refresh_from_db()

        self.assertNotIn(self.member, self.team.members.all())

        self.assertEqual(response.status_code, 302)
