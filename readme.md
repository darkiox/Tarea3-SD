## Generar map | reduce en python

Desarrollado por [Darkiox](https://github.com/darkiox) y [JavierGv1](https://github.com/JavierGv1).

## Video

[![Video](https://img.youtube.com/vi/y7Hw4lUdbAA/maxresdefault.jpg)](https://youtu.be/y7Hw4lUdbAA)

## Diagrama

![Diagrama](https://i.imgur.com/ktC8lKX.png)

## Qué hacer antes de correr contenedor

	python3 wikipedia.py

## Cómo correr el contenedor

Para poder levantar el contenedor:

	docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop

## Cómo entrar al contenedor

	docker exec -it hadoop bash
	
## Qué hacer antes de levantar código

Crear la carpeta input:

     hdfs dfs -mkdir -p input	

Pasamos el input al hdfs;

	`cd examples`
	`hdfs dfs -put Carpeta1/* input`
	`hdfs dfs -put Carpeta2/* input`

## Cómo ejecutar código

	 mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output /user/hduser/output -mapper ./mapper.py -reducer ./reducer.py

## Obtener datos desde Hadoop a Host

	`cd /home/hduser`
	`hdfs dfs -get /user/hduser/output/part-00000 Output.txt`
	`exit`
	`cd examples`
	`docker cp CONTAINERID:/home/hduser/Output.txt Output.txt`
	
## Ejecutar buscador

 	`python3 Browser.py`


