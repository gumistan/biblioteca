# Biblioteca UFPS

## 1. Título y descripción

Sistema para llevar los préstamos de una biblioteca universitaria, hecho con Django. Reemplaza los cuadernos de la bibliotecaria: guarda libros, autores, categorías, copias físicas, estudiantes y préstamos, y ofrece un panel de administración para manejarlos sin conocimientos técnicos.

Actividad de Programación Web, UFPS.

---

## 2. Tecnologías

| Componente | Versión |
|---|---|
| Python | 3.12.6 |
| Django | 6.1.2 |
| Base de datos | SQLite (la que trae Django por defecto, archivo `db.sqlite3`) |

---

## 6. Panel de administración

Cada personalización responde a una necesidad de la bibliotecaria:

| Personalización | Necesidad que resuelve |
|---|---|
| `search_fields` en estudiantes (código y nombre) | Encontrar a un estudiante escribiendo cualquiera de los dos datos |
| Columna "¿Devuelto?" (✔/✘) en préstamos | Ver de un vistazo qué préstamos siguen pendientes, sin interpretar fechas vacías |
| `list_filter` por fechas en préstamos | Acotar la lista por fecha de préstamo y de devolución |
| `autocomplete_fields` en préstamos (copia y estudiante) | Registrar un préstamo buscando por título o código, en vez de un desplegable largo |
| `__str__` de la copia: "Título - código" | No confundir copias de libros distintos, ni copias del mismo libro entre sí |
| `CopiaInline` dentro del libro | Agregar y ver las copias de un libro en la misma página |
| `readonly_fields = ("fecha_prestamo",)` | Que la fecha que se pone sola al crear el préstamo no se edite por error |
| Acción "Marcar préstamos como devueltos" | Devolver varios préstamos de una vez; solo afecta a los que aún no tienen fecha de devolución |
| `list_select_related` en préstamos, copias y libros | Evitar consultas repetidas al mostrar las listas (ver sección 8) |
| Columna de autores en la lista de libros | Ver quién escribió cada libro sin abrirlo |

`list_display`, `search_fields` y `list_filter` están configurados en los modelos Libro, Copia y Préstamo, y todos los modelos tienen un `__str__` legible.

---