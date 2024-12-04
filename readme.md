# Proyecto RestApi

**Descripción:** Este es un proyecto de ejemplo que demuestra cómo aplicar RestApi, debes instalar flask

## Puedes utilizar estos comandos en Postman para probar

curl -X GET http://127.0.0.1:5000/tasks
curl -X POST -H "Content-Type: application/json" -d '{"title": "Estudiar Flask"}' http://127.0.0.1:5000/tasks
curl -X PUT -H "Content-Type: application/json" -d '{"done": true}' http://127.0.0.1:5000/tasks/1
curl -X DELETE http://127.0.0.1:5000/tasks/1
