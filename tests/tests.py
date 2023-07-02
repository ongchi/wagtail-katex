from django.contrib.auth.models import Group, User
from django.test import TestCase

from .models import HomePage


class TestRichTextField(TestCase):
    def setUp(self):
        User.objects.create_superuser(
            username="admin", email="admin@example.com", password="password"
        )
        editor = User.objects.create_user(
            username="editor", email="editor@example.com", password="password"
        )
        editor.groups.add(Group.objects.get(name="Editors"))

    def test_get(self):
        self.assertTrue(self.client.login(username="admin", password="password"))

        page = HomePage.objects.first()
        self.assertTrue(page is not None)

        response = self.client.get(f"/admin/pages/{page.id}/edit/")
        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            """window.draftail.initEditor('#id_text', {"entityTypes": [{"type": "KATEX-EMBED", "icon": "square-root-variable", "description": "Equation"}]}, document.currentScript)""",
            html=True,
        )
