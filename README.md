# simetraTest
Тестовое задание для "Simetra"

Для запуска программы используйте (в корневом файле каталога):
-  docker-compose up -d --build

Для запуска процесса парсинга (если необходимо):
- docker build -t simetra .
- docker run --network=host -d --name simetraApi -p 8000:8000 simetra

#######################################################################################

Внимание! При первом запуске необходимо создать таблицу в postgreSQL внутри контейнера docker:
1) psql -d <база> -U <пользователь> -p <порт>
2) CREATE TABLE vehicle_control
   (
     id BIGINT NOT NULL PRIMARY KEY,
     longlati POINT NOT NULL,
     speed INTEGER NOT NULL,
     gps_time TIMESTAMP NOT NULL,
     vehicle_id BIGINT NOT NULL PRIMERY KEY
   ) PARTITION BY RANGE (vehicle_id);

Для перезапуска парсера вызовете команду:
-  docker-compose up -d --build parser

Теперь вы готовы к запуску!

#######################################################################################

.env-файлы должны распологаться в корневых директориях API и parser 
Содержание файлов:
PG_IP=db
PGUSER=<имя_пользователя>
PGPASSWORD=<пароль>
DATABASE=<имя_базы_данных>
TIMEZONE=Europe/Moscow

#######################################################################################


