from google.cloud import pubsub
from time import sleep
import random
import datetime
import csv
import json


def read_file(filename):
    file_1 = open(filename,'r')
    lines = file_1.readlines() 
    return lines


def publish(lines):
    publisher = pubsub.PublisherClient()
    project = "samhitha-data228-project"
    topic = "my-dataflow-topic1"
    topic_path = publisher.topic_path(project, topic)

    for item in lines:
        print(f"Publishing {bytes(item, 'utf-8')} to {topic_path} at {datetime.datetime.now()}...")
        publisher.publish(topic_path, bytes(item, "utf-8"))
        sleep(0.15)


if __name__ == "__main__":
    filename = '/home/ganesha/GCS_PYTHON/vaccinations-stream.csv'
    dict_object = read_file(filename)
    publish(dict_object)

