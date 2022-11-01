# Kafka PoC - Tweets Streaming to MongoDB

Kafka stack based on Stephane Maarek’s project [kafka-stack-docker-compose](https://github.com/simplesteph/kafka-stack-docker-compose)

El siguiente ejercicio tiene como objetivo introducir al alumno en los siguientes tópicos

1) Docker. Continuando nuestro primer acercamiento a infraestructura y contrainers, la idea es poder seguir utilizando tecnologías cloud native que nos permitan trabajar de forma ágil y consistente.
2) Introducción a Kafka, componentes básicos y casos de uso.
3) Como los producer y consumers interactuan con Kafka
4) Implementar una solución que tomando datos desde la API de Twitter, los mismos se stremean en tiempo real a Kafka desde el producer, y los consumers tomen esos datos y los almacenen en MongoDB

Requerimientos:
- Docker
- Docker Compose
- Python 3.7
- pip (Gestor de paquetes de python)
- Cuenta de desarrollador de Twitter, para mallor información referirse al siguiente artículo [Twitter Dev Account](https://dev.to/sumedhpatkar/beginners-guide-how-to-apply-for-a-twitter-developer-account-1kh7)
- Cliente MongoDB (e.g. Studio3T)
- Datos de Conexión MongoDB `mongodb://localhost:27017` No posee usuario / No posee Password


## Instalación y ejecución

1) Clonar el repositorio
2) Acceder al directorio `cd kafka_demo`
3) ejecutar `pip install -r requirements.txt`
4) Crear un volumen para MongoDB utilizando el siguiente comando `docker volume create data-mongodb`
5) Ejectue el stack `docker-compose -f zk-single-kafka-single_mongo.yml up`
6) Debemos crear un topic, ejecutar el comando `python3.7 create_topic.py` *(Nota: Tu comando python puede diferir, revisar el binario)*
7) Editar el archivo `producer.py` y completar con los datos token y secrets otorgados por Twitter.
   - access_token 
   - access_token_secret
   - consumer_key
   - consumer_secret 
8) Abrir una nueva consola y ejecutar el comando `python3.7 producer.py` 
9) Abrir una consola o tab y ejecutar el consumer mediante el siguiente comando `python3.7 consumer.py`
10) Abrir el cliente de MongoDB y acceder a la Base Twitter y a la collection Data para realizar consultas.
