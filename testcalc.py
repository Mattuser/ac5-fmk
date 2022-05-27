from unittest import TestCase, main
from calcular import app


class Testes(TestCase):
    def test_exponenciacao(self):
        tester = app.test_client(self)
        response = tester.post('/calc', data=dict(n1='10', n2='2', operation='potencia'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'100.0' in response.data)

    def test_raiz_quadrada(self):
        tester = app.test_client(self)
        response = tester.post('/calc', data=dict(n1='81', operation='raiz_quadrada'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'9.0' in response.data)

    def test_logaritmo(self):
        tester = app.test_client(self)
        response = tester.post('/calc', data=dict(n1='81', operation='logaritmo'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'1.9084850188786497' in response.data)

if __name__ == '__main__':
    main()