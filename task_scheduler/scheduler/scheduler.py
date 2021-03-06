from abc import ABCMeta, abstractmethod
from typing import List, Optional, Dict, Any

from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaConsumer

from json import dumps,loads

import pika
import requests
import time


class TaskScheduler(metaclass=ABCMeta):
    @abstractmethod
    def schedule_task(self) -> None:
        pass
    
    # @abstractmethod
    # def get_manufacturer(manufacturer_id: Optional[int]) -> List[Manufacturer]:
    #     pass

    # @abstractmethod
    # def get_interface(interface_id: Optional[int]) -> List[L3Interface]:
    #     pass

class TaskSchedulerKafka(TaskScheduler):

    
    def __init__(self) -> None:
        self._producer =  'localhost:9092'    
    
    def test_schedule_task(self) -> None:

        admin_client = KafkaAdminClient(
            bootstrap_servers='localhost:9093' 
        )

        topic_list = []
        topic_list.append(NewTopic(name="testtopic", num_partitions=1, replication_factor=1))
        admin_client.create_topics(new_topics=topic_list, validate_only=False)



        producer = KafkaProducer(bootstrap_servers='localhost:9093',
                                value_serializer=lambda x: 
                                dumps(x).encode('utf-8'))


        for e in range(5):
            data = {'number' : e}
            producer.send('testtopic', value=data)
            print("sent")
            time.sleep(2)

        consumer = KafkaConsumer(
            'topic_test',
            bootstrap_servers=['localhost:9093'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group-id',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
        for msg in consumer:
            print (msg)        


class TaskSchedulerRabbitmq(TaskScheduler):

    def send_test_msg(self) -> None:
        credentials = pika.PlainCredentials('guest', 'guest')
        params = pika.ConnectionParameters('pydevice_rabbitmq_1', '5672', '/', credentials)
        connection = pika.BlockingConnection(params)   
        channel = connection.channel()      
        channel.queue_declare(queue='queue_test')
        channel.basic_publish(exchange='',
                            routing_key='queue_test',
                            body='Hello World!')
        print(" [x] Sent 'Hello World!'")

        connection.close()

    


    def recv_test_msg(self) -> None:
    
        def callback(ch, method, properties, body):
            print("callback")
            print(" [x] Received %r" % body)        
        
        
        credentials = pika.PlainCredentials('guest', 'guest')
        params = pika.ConnectionParameters('pydevice_rabbitmq_1', '5672', '/', credentials)
        connection = pika.BlockingConnection(params)   
        channel = connection.channel()      
        channel.queue_declare(queue='queue_test')

        channel.basic_consume(queue='queue_test',
                            auto_ack=True,
                            on_message_callback=callback)        
        channel.start_consuming()


    def schedule_task(self) -> None:
        pass
        


def get_task_scheduler() -> TaskScheduler:
    return TaskSchedulerRabbitmq()


   