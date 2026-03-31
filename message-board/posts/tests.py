from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 建立一筆測試用資料
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        # 測試資料庫內容是否正確
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        # 測試 URL 路徑是否正常 (HTTP 200)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        # 綜合測試：名稱、模板與內容
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response, "This is a test!")