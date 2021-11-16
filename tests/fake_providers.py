import random
from datetime import datetime
from datetime import timedelta
from src.modelo.album import Medio
from faker import Faker
from faker.providers import BaseProvider

class AlbumTituloProvider(BaseProvider):
    def albumTitulo(self):
        albumesTitulo = ['Latin Jazz Compilation', 'Bandas sonoras famosas', 'The Dark Side of the Moon', 'The Bodyguard', 'Rumours', 'Saturday Night Fever', 'El fantasma de la ópera', 'Come on Over']
        return random.choice(albumesTitulo)

class AlbumAnioProvider(BaseProvider):
    def albumAnio(self):
        anio = [2018, 2019, 2020, 2021]
        return random.choice(anio)

class AlbumDescripcionProvider(BaseProvider):
    def albumDescripcion(self):
        descripcion = ["Album original", "Compilación"]
        return random.choice(descripcion)

class AlbumMedioProvider(BaseProvider):
    def albumMedio(self):
        self.medios = [ Medio.CD , Medio.CASETE , Medio.DISCO ]
        return random.choice(self.medios)

class AlbumFechaProvider(BaseProvider):
    def AlbumFecha(self):
        new_date = datetime(2019, 2, 28, 00, 00, 00, 00000)
        fecha = [new_date, new_date + timedelta(days=-1), new_date + timedelta(days=-2)]
        return random.choice(fecha)

class CancionTituloProvider(BaseProvider):
    def cancionTitulo(self):
        cancionTitulo = ['Corazon', 'Desesperado', 'La niña de mis ojos', 'Melodía', 'Razones']
        return random.choice(cancionTitulo)

class CancionMinutosProvider(BaseProvider):
    def cancionMinutos(self):
        minutos = [1, 2, 3, 4]
        return random.choice(minutos)

class CancionSegundosProvider(BaseProvider):
    def cancionSegundos(self):
        segundos = [15, 26, 35, 46]
        return random.choice(segundos)

class CancionCompositorProvider(BaseProvider):
    def cancionCompositor(self):
        compositor = ['Enanitos Verdes', 'Grupo 5', 'RBD', 'Yiruma']
        return random.choice(compositor)

class InterpreteNombreProvider(BaseProvider):
    def interpreteNombre(self):
        nombre = ['Marco Hernández', 'George Lucas', 'Esteban Díaz', 'Rosa Olivares']
        return random.choice(nombre)

class InterpreteCuriosidadesProvider(BaseProvider):
    def interpreteCuriosidades(self):
        curiosidades = ['Hermano de', 'Médico', 'Astronauta', 'Emisión de']
        return random.choice(curiosidades)

