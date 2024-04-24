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


## Deployment

Ejecutar servidor

```bash
  python manage.py runserver
```




## Informacion Adicional

Crear una aplicacion con django

```bash
  python manage.py startapp {name_app}
```

## Apps del proyecto

#### Aplicaciones para la funcionalidad del proyecto


| Nombre Apps | Funcionalidad     | Description                |
| :-------- | :------- | :------------------------- |
| `Clases` | `Administrador` | App principal para controlar las clases |
| `Login` | `Inicio de sesion` | Inicio de sesion para acceder al panel |


