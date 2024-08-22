# pythools v3.0

## Variables de entorno

Las variables de entorno se cargan desde el archivo `.env`, se puede tomar como base el example.env

`cp example.env .env`

Se puede usar variables dentro del archivo yml, con la estructura `${api}`

## set de pruebas

### qué es?

un set de pruebas es un archivo yml que contiene un listado de request a ejecutar que tienen contexto y relación entre si.

Por ejemplo, `POST ${api}/users` crea un usuario y devuelve su id, luego con ese id se hace una request a `GET ${api}/user/101` para verificar que se creo correctamente. Además usando otra id que no exista, deberia retornar otra respuesta.

```yml
requests:
  - name: create user
    request: POST ${api}/users
    json: '{"name":"Jhon Doe", "user":"jhdoe"}'
    response:
      status: 201
      json:
        id: 101
  - name: get user informacion by id
    request: GET ${api}/user/101
    response:
      status: 200
      json:
        name: Jhon Doe
        user: jhdoue
        'address.city': Dosquebradas
  - name: return not found when user id not exists
      request: GET ${api}/user/9999
      response:
        status: 404
        json:
          message: user with id 9999 not found
```


### Restricciones

Por ahora cada peticion require poner informacion manualmente si esta cambia. En una futura version una request como `GET ${api}/users/$#{userId}`.

resolvera `${api}`desde las environments y `$#{userId}` solicitara interaccion con el usuario.
