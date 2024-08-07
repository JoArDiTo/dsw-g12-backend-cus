# Entregable SISVITA3 - grupo 12

## Descripción:
Tratamos el desarrollo del backend de los casos de uso proporcionados en el diagrama para el avance del proyecto de curso *DESARROLLO DE SISTEMAS WEB*.

## Detalles:
- Uso del framework Flask, extendido con Marshmallow
- Uso del gestor de base de datos Postgresql
- Uso de render para desplegar proyecto

## Instalación:
- Descargamos el repositorio como .ZIP o con el siguiente comando:
```bash
git clone git@github.com:JoArDiTo-DEV/dsw-g12-backend-cus.git
```

- Una vez instalado, nos dirigimos a la carpeta del proyecto importado
```bash
cd g12-sisvita3-backend-cus/
```

- Abrimos en nuestro editor de codigo e instalamos el entorno virtual por la terminal:
```bash
virtualenv venv
```

- En caso de no tener la librería *virtualenv*, instalamos con el siguiente comando:
```bash
pip install virtualenv
```

- Continuando con la instalación, activamos el entorno virtual:

### Para sistemas WINDOWS:
```cmd
venv\Scripts\activate
```

### Para sistemas LINUX:
```bash
source venv/bin/activate
```

- Con esto, instalamos los requerimientos del proyecto:
```bash
pip install -r requirements.txt
```

- Creamos un archivo .env para realizar la configuración de la base de datos, en el archivo debe ir lo siguiente:
```.env
USER = <nombre-del-usuario-de-la-base-de-datos>
PASSWORD = <contraseña-de-la-base-de-datos>
DATABASE = <nombre-de-la-base-de-datos>
HOST = <host-de-la-base-de-datos>
SERVER = postgresql

EMAIL = <correo-gmail-para-permitir-el-envío-de-correos>
PASSWORD_EMAIL = <contraseña-de-aplicación-del-correo>
```

- Corremos el programa
```bash
python app.py
```

## Observacion:
Para obtener una contraseña de aplicación, se hace lo siguiente:
- Tenemos que ir a la configuración de la cuenta gmail que vamos a usar.

![Configurar-envío-de-correo](/imagenes-para-configurar-correo/paso-1.png)

- Luego, vamos a la opción de seguridad

![Configurar-envío-de-correo](/imagenes-para-configurar-correo/paso-2.png)

- Y seleccionamos la opción para realizar la verificación en dos pasos.

![Configurar-envío-de-correo](/imagenes-para-configurar-correo/paso-3.png)

- Una vez configurada, buscamos *Contraseñas de aplicación* e ingresamos

![Configurar-envío-de-correo](/imagenes-para-configurar-correo/paso-4.png)

- Creamos el nombre de la aplicación

![Configurar-envío-de-correo](/imagenes-para-configurar-correo/paso-5.png)

- Finalmente, nos entrega la contraseña para ingresarlo en nuestras variables de entorno *.env*

![Configurar-envío-de-correo](/imagenes-para-configurar-correo/paso-6.png)






