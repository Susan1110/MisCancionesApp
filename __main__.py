from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.album import Album, Medio
from src.modelo.declarative_base import Session, engine, Base
from src.logica.coleccion import Coleccion


def anadir_album (titulo , anio , descripcion , medio) :
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )
   coleccion = Coleccion ( )

   if coleccion.agregar_album ( titulo , anio , descripcion , medio ) :
      print ( f"Se añadio el titulo: {titulo}" )
   else :
      print ( f"El título: {titulo}, ya existe" )
   session.close()

def editar_album (album_id,titulo , anio , descripcion , medio) :
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )
   coleccion = Coleccion ( )

   if coleccion.editar_album ( album_id , titulo , anio , descripcion , medio ) :
      print ( f"Se modifico el album con id: {album_id}" )
   else :
      print ( f"El nuevo título '{titulo}' para el album con id: {album_id}, ya existe" )
   session.close()



def mostrar_album (album_id) :
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )
   coleccion = Coleccion ( )

   album=coleccion.dar_album_por_id(album_id)
   # print(album)
   print ( f"=======================================" )
   print ( f"Id Album    : {album[ 'id' ]}" )
   print ( f"Título Album: {album[ 'titulo' ]}" )
   print ( f"Año         : {album[ 'anio' ]}" )
   print ( f"Descripción : {album[ 'descripcion' ]}" )
   print ( f"Medio       : {album[ 'medio' ]}" )
   print ( f"=======================================" )
   session.close()

def Anadir_registros():
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )

   # crear interpretes
   interprete1 = Interprete ( nombre = "Samuel Torres" , texto_curiosidades = "Es colombiano y vive en NY" )
   interprete2 = Interprete ( nombre = "Aldo Gavilan" , texto_curiosidades = "Canto a Cuba" )
   interprete3 = Interprete ( nombre = "Buena Vista Social club" )
   interprete4 = Interprete ( nombre = "Arturo Sandoval" , texto_curiosidades = "No sabia quien era" )
   session.add ( interprete1 )
   session.add ( interprete2 )
   session.add ( interprete3 )
   session.add ( interprete4 )
   session.commit ( )

   # Crear albumes
   album1 = Album ( titulo = "Latin Jazz Compilation" , anio = 2021 , descripcion = "Album original" , medio = Medio.DISCO )
   album2 = Album ( titulo = "Bandas sonoras famosas" , anio = 2021 , descripcion = "Compilacion" , medio = Medio.DISCO )
   session.add ( album1 )
   session.add ( album2 )

   # Crear canciones
   cancion1 = Cancion ( titulo = "Ajiaco" , minutos = 3 , segundos = 1 , compositor = "Samuel Torres" )
   cancion2 = Cancion ( titulo = "Forced Displacement" , minutos = 3 , segundos = 12 , compositor = "Desconocido" )
   cancion3 = Cancion ( titulo = "Alegria" , minutos = 4 , segundos = 27 , compositor = "AU" )
   session.add ( cancion1 )
   session.add ( cancion2 )
   session.add ( cancion3 )

   # Relacionar albumes con canciones
   album1.canciones = [ cancion1 , cancion2 ]
   album2.canciones = [ cancion1 , cancion3 ]

   # Relacionar canciones con interpretes
   cancion1.interpretes = [ interprete1 ]
   cancion2.interpretes = [ interprete2 ]
   cancion3.interpretes = [ interprete3 , interprete4 ]
   session.commit ( )

   session.commit ( )
   session.close ( )

if __name__ == '__main__':
   Anadir_registros ( )

   anadir_album ( "Arde del cielo" , 2008 , "Album rock" , Medio.CD )
   anadir_album ( "Similares" , 2015 , "Romantico" , Medio.CD )
   anadir_album ( "Otherside" , 1999 , "Rock alternativo" , Medio.CD )
   anadir_album ( "All the Little Lights" , 2012 , "Folk, Pop, Cantautor, Rock, Acoustic" , Medio.CD )

   editar_album (2, "Similares",2020, "Romantico",Medio.CD)
   editar_album ( 1 , "River flows in you ",2010 , "Romantico" , Medio.CD)

   for i in [ 1 , 2 , 3, 4] :
      mostrar_album ( i )

   i = 1
   while i <= 4:
      mostrar_album(i)
      i=i+1

