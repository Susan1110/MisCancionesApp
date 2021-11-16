import unittest

from faker import Faker

from src.logica.coleccion import Coleccion
from src.modelo.cancion import Cancion
from src.modelo.declarative_base import Session
from fake_providers import CancionTituloProvider, CancionMinutosProvider, CancionSegundosProvider, CancionCompositorProvider

class CancionTestCaseFake(unittest.TestCase):
    def setUp ( self ) :
        self.logica = Coleccion()
        self.session = Session ( )
        self.data_factory = Faker ( )

        # Generación de datos con libreria Faker
        self.data_factory.add_provider(CancionTituloProvider)
        self.data_factory.add_provider(CancionMinutosProvider)
        self.data_factory.add_provider(CancionSegundosProvider)
        self.data_factory.add_provider(CancionCompositorProvider)

        self.dataC=[]
        self.canciones=[]
        for i in range ( 0 , 2 ) :
            self.dataC.append(
                (
                    self.data_factory.cancionTitulo(),
                    self.data_factory.cancionMinutos(),
                    self.data_factory.cancionSegundos(),
                    self.data_factory.cancionCompositor()
                )
            )
            self.canciones.append(
                Cancion(
                    titulo=self.dataC[-1][0],
                    minutos=self.dataC[-1][1],
                    segundos=self.dataC[-1][2],
                    compositor=self.dataC[-1][3]
                )
            )
            self.session.add ( self.canciones[ -1 ] )

        '''
            Persiste los objetos
            En este setUp no se cierra la sesión para usar
            los albumes en las pruebas
        '''
        self.session.commit ( )
        #self.session.close()

    def tearDown ( self ) :
        self.session = Session ( )

        busqueda_cancion = self.session.query(Cancion).all()
        for cancion in busqueda_cancion:
            self.session.delete(cancion)

        self.session.commit()
        self.session.close()

    def test_constructor ( self ) :
        for cancion , dato in zip ( self.canciones , self.dataC ) :
            self.assertEqual ( cancion.titulo , dato[ 0 ] )
            self.assertEqual ( cancion.minutos , dato[ 1 ] )
            self.assertEqual ( cancion.segundos , dato[ 2 ] )
            self.assertEqual ( cancion.compositor , dato[ 3 ] )

    def test_agregar_cancion ( self ) :
        cancionTitulo=self.data_factory.unique.cancionTitulo ( )
        cancionMinutos=self.data_factory.cancionMinutos ( )
        cancionSegundos=self.data_factory.cancionSegundos ( )
        cancionCompositor=self.data_factory.cancionCompositor()

        resultado=self.logica.agregar_cancion(cancionTitulo,cancionMinutos,cancionSegundos,cancionCompositor)

        self.assertEqual ( resultado , True )