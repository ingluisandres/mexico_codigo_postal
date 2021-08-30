# API de los códigos postales de México, con sus estados y municipios.

## Sin docker-compose

Si no tienes los datos, puedes usar el archivo database.db descomentando las líneas 13-16 en el archivo database.py y comentando de la 8 a la 11. 

Ejecuta:

```
python -m venv .venv3.8
. venv3.8/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Luego ve a 127.0.0.1:8000/docs para ver la documentación de la API.

Ingresa la siguientes credenciales para estar autenticado. username: andy031197@gmail.com, password: somepassword
