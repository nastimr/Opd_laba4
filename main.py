import unittest

from app import app

class TestDrive(unittest.TestCase):

    def test_page(self):  #тестируем функцию, которая отвечает за главную страницу
        tester = app.test_client(self)  #создаем клиент для тестирования
        response = tester.get('/')  #отправляем GET-запрос на главную страницу
        self.assertEqual(response.status_code, 200)  #проверяем, что код ответа равен 200

    def test_shar_page(self):  #тестируем функцию, которая отвечает за страницу с объемом шара
        tester = app.test_client(self)
        response = tester.get('/shar.html')
        self.assertEqual(response.status_code, 200)

    def test_kub_page(self):  #тестируем функцию, которая отвечает за страницу с объемом куба
        tester = app.test_client(self)
        response = tester.get('/kub.html')
        self.assertEqual(response.status_code, 200)

    def test_konus_page(self):  #тестируем функцию, которая отвечает за страницу с объемом конуса
        tester = app.test_client(self)
        response = tester.get('/konus.html')
        self.assertEqual(response.status_code, 200)

    def test_tcilindr_page(self):  #тестируем функцию, которая отвечает за страницу с объемом цилиндра
        tester = app.test_client(self)
        response = tester.get('/tcilindr.html')
        self.assertEqual(response.status_code, 200)

    def test_piramida_page(self):  #тестируем функцию, которая отвечает за страницу с объемом пирамиды
        tester = app.test_client(self)
        response = tester.get('/piramida.html')
        self.assertEqual(response.status_code, 200)

    def test_parallelepiped_page(self):  #тестируем функцию, которая отвечает за страницу с объемом параллелепипеда
        tester = app.test_client(self)
        response = tester.get('/parallelepiped.html')
        self.assertEqual(response.status_code, 200)

    def test_shar_V(self):  #тестируем функцию, которая отвечает за вычисление объема шара
        tester = app.test_client(self)
        response = tester.post('/shar.html', data={'R': 3, 'toch': 2})  #отправляем POST-запрос на страницу с объемом шара с тестовым набором данных
        correct_answer = '113.04  см^3'
        self.assertIn(correct_answer, response.data.decode())  #проверяем, содержит ли полученный ответ необходимый результат

    def test_kub_V(self):  #тестируем функцию, которая отвечает за вычисление объема куба
        tester = app.test_client(self)
        response = tester.post('/kub.html', data={'a': 10, 'toch': 0})
        correct_answer = '1000.0  см^3'
        self.assertIn(correct_answer, response.data.decode())

    def test_konus_V(self):  # тестируем функцию, которая отвечает за вычисление объема конуса
        tester = app.test_client(self)
        response = tester.post('/konus.html', data={'R': 1, 'h': 3, 'toch': 1})
        correct_answer = '3.1  см^3'
        self.assertIn(correct_answer, response.data.decode())

    def test_tcilindr_V(self):  # тестируем функцию, которая отвечает за вычисление объема цилиндра
        tester = app.test_client(self)
        response = tester.post('/tcilindr.html', data={'R': 2, 'h': 0.1, 'toch': 2})
        correct_answer = '1.26  см^3'
        self.assertIn(correct_answer, response.data.decode())

    def test_piramida_V(self):  # тестируем функцию, которая отвечает за вычисление объема пирамиды
        tester = app.test_client(self)
        response = tester.post('/piramida.html', data={'S': 4, 'h': 5, 'toch': 0})
        correct_answer = '7.0  см^3'
        self.assertIn(correct_answer, response.data.decode())

    def test_parallelepiped_V(self):  # тестируем функцию, которая отвечает за вычисление объема параллелепипеда
        tester = app.test_client(self)
        response = tester.post('/parallelepiped.html', data={'a': 0.1, 'b': 0.1, 'c': 5, 'toch': 2})
        correct_answer = '0.05  см^3'
        self.assertIn(correct_answer, response.data.decode())

if __name__ == '__main__':
    unittest.main()  #запускаем тесты