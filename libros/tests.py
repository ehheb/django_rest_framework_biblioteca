from rest_framework.test import APITestCase

from autores.models import Autor
from editoriales.models import Editorial
from libros.models import Libro


class TestLibroCRUD(APITestCase):

    def setUp(self):
        self.host = 'http://127.0.0.1:8000'

        self.editorial = Editorial.objects.create(
            nombre='Edit_1',
            direccion='123',
            telefono='614259784',
            correo='editorial@gmail.com'
        )

        self.autores = Autor.objects.create(
            nombre='heb',
            apellido='villa',
            edad=25,
            telefono='614598745'
        )

        self.libro = Libro.objects.create(
            nombre='Libro_1',
            fecha_publicacion='2021-04-21',
            paginas=10,
            editorial=self.editorial
        )

    def test_get_libros(self):
        response = self.client.get(f'{self.host}/libros/')

        self.assertEqual(response.status_code, 200, 'Invalid status code')
        print("cantidad libros en get", Libro.objects.all().count())
        self.assertEqual(len(response.data), 1, 'Invalid resposne data')
        self.assertEqual(self.libro.id, response.data[0]['id'])

    def test_patch_libros(self):
        data = {
            'nombre': 'corregir Libro'
        }
        response = self.client.patch(f'{self.host}/libros/{self.libro.id}/', data)
        self.assertEqual(response.status_code, 200, response.data)
        print("cantidad libros en patch", Libro.objects.all().count())
        self.assertEqual(Libro.objects.all().count(), 1)

    def test_delete_libros(self):
        response = self.client.delete(f'{self.host}/libros/{self.libro.id}/')
        print('lirbo id en delete:', self.libro.id)

        self.assertEqual(response.status_code, 204, 'Invalid status code')
        print("cantidad libros en delete", Libro.objects.all().count())
        self.assertEqual(Libro.objects.all().count(), 0)

    def test_post_libros(self):
        data = {
            "nombre": "Libro_2",
            "fecha_publicacion": "2021-01-01",
            "paginas": 15,
            'editorial': self.editorial.id,
            'autores': [self.autores.id]
        }
        response = self.client.post(f'{self.host}/libros/', data)
        self.assertEqual(response.status_code, 201, response.data)
        print("cantidad libros en post", Libro.objects.all().count())
        self.assertEqual(Libro.objects.all().count(), 2)

    def test_put_libros(self):
        data = {
            "nombre": "Se corrige el nombre del libro",
            "fecha_publicacion": "2021-01-01",
            "paginas": 15,
            'editorial': self.editorial.id,
            'autores': [self.autores.id]
        }
        response = self.client.put(f'{self.host}/libros/{self.libro.id}/', data)
        self.assertEqual(response.status_code, 200, response.data)
        print("cantidad libros en put", Libro.objects.all().count())
        self.assertEqual(Libro.objects.all().count(), 1)






