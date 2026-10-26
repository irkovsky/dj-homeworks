from django.test import TestCase
from django.urls import reverse
from .models import Student, Teacher

class ModelTests(TestCase):
    def test_student_creation(self):
        """Проверяем, что студент создается и его имя сохраняется"""
        student = Student.objects.create(name="Иван", age=20)
        self.assertEqual(student.name, "Иван")
        self.assertEqual(str(student), "Иван") # Если у вас в модели есть __str__

class ViewTests(TestCase):
    def test_home_page_status_code(self):
        """Проверяем, что главная страница (или список студентов) отдает код 200"""
        # Замените 'students_list' на имя вашего URL-паттерна, если оно другое
        # Если не знаете имя, можно просто вписать путь: '/'
        response = self.client.get('/') 
        self.assertEqual(response.status_code, 200)