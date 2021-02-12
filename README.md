# Web Cine | Temas 1-4 Ejercicios Propuestos

En este repositorio estaré llevando la documentación del proyecto de temas 1 al 4 del curso de django de inteccsa

# Índice

1. [Como subir este repositorio](#Como-subir-este-repo)
2. [Contraseña Login](#Contraseña-Login)
3. [Link de Post - Blog Notion](#Link-de-Post---Blog-Notion)
4. [Comentarios](#Comentarios)

# Como subir este repositorio

- Creo el repo en github normal si novedad, en blanco.
- Creo el README.md con la estructura de documentacion como puedes ver.
- **Y luego aplico estos comandos:**

  - git init
  - git add .
  - git commit -m "first commit"
  - git branch -M main
  - git remote add origin https://github.com/gustavcaves/examen-tema1-4-django
  - git push -u origin main
- **Luego para seguir actualizando:**

  - git status
  - **git add .**
  - git status
  - **git commit -m "another commit"**
  - git status
  - **git push -u origin main**

# Contraseña Login

admin | 1234

# Link de Post - Blog Notion

[Examen 1 Python Django (notion.so)](https://www.notion.so/Examen-1-Python-Django-6afb294b2a034367b2a7aaa2af6091f0)

# Puntos del Examen:

## Pregunta 1 (1 punto)

1. [X] Crea el proyecto cine y la aplicación sala
2. [X] Configura la base de datos y las opciones locales (idioma, zona horaria)
3. [X] Sincroniza la base de datos.
4. [X] Lanza el servidor interno de django y comprueba que funciona el
   proyecto

## Pregunta 2 (1 punto)

En la aplicación sala :

1. [X] Escribe las dos clases para los modelos: Peliculas y programacionSala
2. [X] Sincroniza la base de datos
3. [X] Introduce varias peliculas y programacionSala desde la API del ORM de
   django

## Pregunta 3 (3 punto)

1. [X] Activa el admin de Django para la aplicación sala
2. [X] Diseña una clase para administrar las salas
3. [X] Relaciona las opciones mediante un inline
4. [X] Configura los fieldsets
5. [X] Haz que se vea bien el plural de programacionSala
6. [X] Mejora la página de listados de salas:
7. [X] Que se vean bien las columnas de datos
8. [X] Opción para buscar
9. [X] Añade list_filter y date_hierarchy
10. [X] Cambia el nombre de la aplicación para que no se vea: Administración
    de Django
11. [ ] Haz que, al entrar en el admin, vaya directamente a la aplicación de
    salas.
12. [ ] Añade en el listado de las encuestas el número total de películas
    exhibidas que ha tenido cada una.

## Pregunta 4 (3 punto)

Diseña las urls para que se pueda acceder a:

1. [ ] Listado general de todas las salas
2. [ ] Detalle de una sala
3. [ ] Resultado de las películas exhibidas en esa sala
4. [X] Hazlo en un fichero urls.py dentro de la aplicación y enlázalo desde
   el urls.py general del proyecto
5. [ ] Escribe las tres vistas para las acciones anteriores.
6. [ ] Escribe las plantillas necesarias. Configura el directorio de templates
   dentro de settings.py

## Pregunta 5 (2 punto)

* [ ] Modifica tus plantillas para que usen un template genérico que contenga el
  estilo del sitio. Utiliza la herencia de plantillas. Haz que todas las páginas
  compartan el encabezado y el pie de página. Pon un color de fondo a las
  páginas y modifica el color de la letra. En el encabezado tendrá que haber una
  imagen almacenada en el proyecto.

# Comentarios

### viernes, 12 de febrero de 2021 23:19

Avanzando punto por punto, he cambiado titulo a administrador, fielsetd search and others. I think this comments aren´t useful, I am tinking only use the commit offered by git, and write every thing in english to practice too.

### jueves, 11 de febrero de 2021 23:16

He realizado algunos puntos, agragado datos por la shell orm api de django y visualizado con el admin. Entre otras cosas como practicar e interiorizar mas los comandos.

### martes, 3 de febrero de 2021 20:05

Creo este formato de documentacion para darle seguimiento al proceso.

### lunes, 1 de febrero de 2021 23:03

Projecto creado y app creada, conexion con postgresql exitosa. Migraciones por defecto realizadas.
