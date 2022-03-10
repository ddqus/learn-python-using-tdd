import os

from confluent_kafka import Consumer
from confluent_kafka.admin import ClusterMetadata, TopicMetadata

_conf = {
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVER"),
    "group.id": os.getenv("KAFKA_GROUP_ID"),
    'auto.offset.reset': "earliest",
}

_topic = os.getenv("KAFKA_TOPIC")


def test_config():
    assert _conf.get("bootstrap.servers")
    assert _conf.get("group.id")


def test_consumer():
    consumer = Consumer(_conf)
    assert consumer

    cluster_metadata = consumer.list_topics(_topic, timeout=1)  # type: ClusterMetadata
    topic = cluster_metadata.topics.get(_topic)  # type: TopicMetadata
    assert None is topic.error

    consumer.subscribe([_topic])
    msg = consumer.poll(timeout=0.5)
    assert None is msg
