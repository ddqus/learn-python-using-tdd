import json
import logging
import os
import time
import uuid
from multiprocessing import Process

from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic, ClusterMetadata
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=getattr(logging, os.getenv('LOGLEVEL', '').upper(), 'INFO'),
    format='[%(asctime)s] %(levelname)s:%(name)s:%(message)s',
)

_conf = {
    # "logger": logging,
    "process": {
        "producer_count": 2,
        "consumer_count": 2,
    },
    "kafka": {
        "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVER"),
        "group.id": os.getenv("KAFKA_GROUP_ID"),
        # 'auto.offset.reset': "earliest",
    },
    "producer": {
        "msg_count": 2000000,
    },
    "output": {
        "file": "output.txt",
    },
}

_topic = os.getenv("KAFKA_TOPIC")


def run():
    producers = []
    consumers = []

    logging.info("topic: {}".format(_topic))
    _create_topic(_topic)

    for i in range(_conf["process"]["consumer_count"]):
        logging.info("start consumer process: {}".format(i))
        # p = ConsumerProcess(_conf)
        p = Process(
            daemon=True,
            target=_consumer,
            args=(_conf, _topic),
        )
        p.start()
        consumers.append(p)

    for i in range(_conf["process"]["producer_count"]):
        logging.info("start producer process: {}".format(i))
        p = Process(
            daemon=True,
            target=_producer,
            args=(_conf, _topic),
        )
        p.start()
        producers.append(p)

    for producer in producers:
        producer.join()

    for consumer in consumers:
        consumer.join()


def _create_topic(topic):
    admin = AdminClient(_conf["kafka"])

    exist_topics = admin.list_topics()  # type: ClusterMetadata

    if topic in exist_topics.topics:
        return

    topics = [NewTopic(topic, num_partitions=10, replication_factor=1)]
    fs = admin.create_topics(topics)  # type: dict

    for topic, f in fs.items():
        f.result()
        logging.info("topic created: {}".format(topic))


def _producer(conf, topic):
    logging.info("producer process: pid:{}".format(os.getpid()))

    producer = Producer(conf["kafka"])

    for i in range(conf["producer"]["msg_count"]):
        msg = json.dumps({
            "created": str(time.time()),
            "id": str(uuid.uuid4()),
        })
        # logging.info("produce topic({}) msg #{}:({}...)".format(topic, i, msg[0:70]))
        producer.poll(0)
        producer.produce(topic, msg.encode("UTF-8"))
        producer.flush()
        # sleep(random.random())


def _consumer(conf, topic):
    logging.info("consumer process: pid:{}".format(os.getpid()))

    consumer = Consumer(conf["kafka"])
    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(0.5)
        if msg is None:
            continue

        if msg.error():
            logging.error("error: {}".format(msg.error()))

        jsonobj = json.loads(msg.value())

        diff = time.time() - float(jsonobj["created"])
        output = {
            "diff": diff,
            "created": jsonobj["created"],
        }
        line = json.dumps(output)

        logging.info("msg: {}".format(line))

        # with open(conf["output"]["file"], "a") as f:
        #     f.write(msg.value())
        #     f.write("\n")

    logging.info("consumer end")


if __name__ == "__main__":
    run()
