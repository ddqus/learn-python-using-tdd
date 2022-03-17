import os
import threading

from confluent_kafka import Producer

_producer_config = {
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVER"),
}

producer = Producer(_producer_config)


def run(i):
    print(f"thread #{i}")

    for k in range(10):
        producer.poll(0)
        producer.produce("test", f"thread#{i} num#{k}")

        if k % 1000 == 0:
            producer.flush()
    producer.flush()


def test_thread():
    threads = []
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
