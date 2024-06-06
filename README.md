# Entregable SISVITA3 - grupo 12

## Descripción:
Tratamos el desarrollo del backend de los casos de uso proporcionados en el diagrama para el avance del proyecto de curso *DESARROLLO DE SISTEMAS WEB*.

## Detalles:
- Uso del framework Flask, extendido con Marshmallow
- Uso del gestor de base de datos Postgresql
- Uso de render para desplegar proyecto

## Instalación:
- Descargamos el repositorio como .ZIP o con el siguiente enlace SSH:
```bash
git clone git@github.com:JoArDiTo-DEV/dsw-g12-backend-cus.git
```

- Nos dirigimos a la carpeta del proyecto importado
```bash
cd g12-sisvita3-backend-cus/
```

- Una vez instalado, abrimos en nuestro editor de codigo e instalamos el entorno virtual:
```bash
virtualenv venv
```

- En caso de no tener la librería, instalamos con:
```bash
pip install virtualenv
```

- Ahora, activamos el entorno virtual:

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

- Configuramos la base de datos a utilizar (crear un archivo .env)

- Corremos el programa
```bash
python app.py
```


