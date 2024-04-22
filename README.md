# PortalEdu
portal educativo para aulas vituales con django

## Ejecutar local

Clonar el repositorio 
```bash
  git clone https://github.com/Adrian-Aguilera/PortalEdu.git
```

Go to the project directory

```bash
  cd /PortalEdu
```


## Instalacion

Para poder instalar el proyecto, crearemos un .venv para instalar las dependencias

```bash
  python3 -m venv .venv
  .venv\Scripts\activate
```
una vez instalado y corriendo la terminal del .venv, instalar las dependencias corriendo

```bash
  pip install -r requirements.txt
```

Ejecutar servidor

```bash
  python manage.py runserver
```


Crear una aplicacion con dajngo 

```bash
  python manage.py startapp {name_app}
```
