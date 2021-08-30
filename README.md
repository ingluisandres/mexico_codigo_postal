### API de los códigos postales de México, con sus estados y municipios.

Primero tienes que crear un archivo .env con la variable MYSQL_ROOT_PASSWORD y asígnale un valor.

Si no tienes los datos, puedes usar el archivo database.db des comentando las líneas 13-16 en el archivo database.py y comentando de la 8 a la 11. Tambien puedes comentar el servicio database en docker-compose.yml.

Asegúrate de tener instalado docker-compose. 

Ejecuta:

```
docker-compose up --build
```

Luego ve al localhost:5000/docs para ver la documentación de la API.
