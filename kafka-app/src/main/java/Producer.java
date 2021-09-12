import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

public class Producer {
    public Producer(){
        // basic configurations needed to connect kafka client to the kafka server
        // object that will be storing the key value pair
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        ProducerRecord producerRecord = new ProducerRecord("farm", "name", "Hello from the Java Producer");

        KafkaProducer kafkaProducer = new KafkaProducer(properties);

        kafkaProducer.send(producerRecord);
        kafkaProducer.close();
    }
}
