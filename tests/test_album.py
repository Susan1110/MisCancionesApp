from faker import Faker
import random
import unittest
from src.logica.coleccion import Coleccion
from src.modelo.album import Album, Medio
from src.modelo.cancion import Cancion, AlbumCancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import Session

class AlbumTestCase(unittest.TestCase):
    def setUp(self):
        '''Crea una colección para hacer las pruebas'''
        self.coleccion = Coleccion()

        '''Abre la sesión'''
        self.session = Session()

        '''Crea una instance de Faker'''
        self.data_factory = Faker ( )

        '''Se programa para que Faker cree los mismos datos cuando se ejecuta'''
        Faker.seed ( 1000 )

        '''Genera 10 datos en data y creamos los álbumes'''
        self.data = [ ]
        self.albumes = [ ]
        self.medios = [ Medio.CD , Medio.CASETE , Medio.DISCO ]
        for i in range ( 0 , 10 ) :
            self.data.append ( (
                self.data_factory.unique.name ( ) ,
                self.data_factory.random_int ( 1800 , 2021 ) ,
                self.data_factory.text ( ) ,
                random.choice ( self.medios )) )
            self.albumes.append (
                Album (
                    titulo = self.data[ -1 ][ 0 ] ,
                    anio = self.data[ -1 ][ 1 ] ,
                    descripcion = self.data[ -1 ][ 2 ] ,
                    medio = self.data[ -1 ][ 3 ] ,
                    canciones = [ ]
                ) )
            self.session.add ( self.albumes[ -1 ] )

        '''Persiste los objetos
        En este setUp no se cierra la sesión para usar los albumes en las pruebas'''
        self.session.commit ( )

    def tearDown(self) :
        self.session = Session ( )
        busqueda = self.session.query ( Album ).all ( )

        for album in busqueda :
            self.session.delete ( album )

        self.session.commit ( )
        self.session.close ( )

    def test_constructor(self):
        for album, dato in zip(self.albumes, self.data):
            self.assertEqual(album.titulo, dato[0])
            self.assertEqual(album.anio, dato[1])
            self.assertEqual(album.descripcion, dato[2])
            self.assertEqual(album.medio, dato[3])

    def test_agregar_album ( self ) :
        '''Prueba la adición de un álbum'''

        self.data.append ( (self.data_factory.unique.name ( ) , self.data_factory.random_int ( 1800 , 2021 ) ,
                            self.data_factory.text ( ) , random.choice ( self.medios )) )
        resultado = self.coleccion.agregar_album (
            titulo = self.data[ -1 ][ 0 ] ,
            anio = self.data[ -1 ][ 1 ] ,
            descripcion = self.data[ -1 ][ 2 ] ,
            medio = self.data[ -1 ][ 3 ] )
        self.assertEqual ( resultado , True )