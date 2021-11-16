import unittest

from faker import Faker

from src.logica.coleccion import Coleccion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import Session
from fake_providers import InterpreteNombreProvider, InterpreteCuriosidadesProvider

class InterpreteTestCaseFake(unittest.TestCase):
    def setUp ( self ) :
        self.logica = Coleccion()
        self.session = Session ( )
        self.data_factory = Faker ( )

        # Generación de datos con libreria Faker
        self.data_factory.add_provider(InterpreteNombreProvider)
        self.data_factory.add_provider(InterpreteCuriosidadesProvider)

        self.dataI=[]
        self.interpretes=[]
        for i in range ( 0 , 2 ) :
            self.dataI.append(
                (
                    self.data_factory.interpreteNombre(),
                    self.data_factory.interpreteCuriosidades(),
                )
            )
            self.interpretes.append(
                Interprete(
                    nombre=self.dataI[-1][0],
                    texto_curiosidades=self.dataI[-1][1]
                )
            )
            self.session.add ( self.interpretes[ -1 ] )

        '''
            Persiste los objetos
            En este setUp no se cierra la sesión para usar
            los albumes en las pruebas
        '''
        self.session.commit ( )
        #self.session.close()

    def tearDown ( self ) :
        self.session = Session ( )

        busqueda_interprete = self.session.query(Interprete).all()
        for interprete in busqueda_interprete:
            self.session.delete(interprete)

        self.session.commit()
        self.session.close()

    def test_constructor ( self ) :
        for interprete , dato in zip ( self.interpretes , self.dataI ) :
            self.assertEqual ( interprete.nombre , dato[ 0 ] )
            self.assertEqual ( interprete.texto_curiosidades , dato[ 1 ] )

    def test_agregar_interprete ( self ) :
        interpreteNombre=self.data_factory.unique.interpreteNombre ( )
        interpreteCuriosidades=self.data_factory.interpreteCuriosidades ( )

        resultado=self.logica.agregar_interprete(interpreteNombre,interpreteCuriosidades)

        self.assertEqual ( resultado , True )