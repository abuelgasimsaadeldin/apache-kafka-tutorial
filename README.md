# Apache Kafka tutorial

Apache Kafka is a distributed publish-subscribe messaging system developed by LinkedIn and written in Scala and Java.

## Windows Installation Guide:

1) Install Java SDK (required Java 8+).
2) Download and Install Apache Kafka Binaries from the following [link](https://kafka.apache.org/downloads).
3) Extract the folder and move it to local disk C Drive.
4) Create 'zookeeper' and 'kafka-logs' folders for storing zookeeper data and kafka logs.
5) Modify ```dataDir=/tmp/zookeeper``` in config.properties to ```dataDir=C:/kafka/zookeeper```.
6) Modify ```log.dirs=/tmp/kafka-logs``` in config/server.properties to ```log.dirs=C:/kafka/kafka-logs```.

<br />

## Producing and Consuming Messages Using Kafka
### Start Zookeeper Server:
```
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper-properties
```

### Start Kafka Server:
```
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

### Create Topic in Kafka Broker:
```
.\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --topic cities
```

### Create Kafka Producer:
```
.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic cities
```

### Create Kafka Consumer:
```
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic cities --from-beginning
```
<br />

## Kafka with Python
In order to use Kafka with Python you need to first install kafka-python, to do so use following command:
```
pip install kafka-python
```

### Send String Data to Kafka Server:
To send a string data to the Kafka Server using Python run the following script:
```
python producer.py
```

### Send SensorIOT Data to Kafka Server:
To send a continuous dummy real-time IOT sensors data into Kafka run the following script:
```
python producer-sensor
```

