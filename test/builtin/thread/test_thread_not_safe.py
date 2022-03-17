import threading

n = 0


def foo():
    global n
    for _ in range(500000):
        n += 1


def test_thread_not_safe():
    global n
    threads = []
    for i in range(10):
        t = threading.Thread(target=foo)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    assert n != 500000 * 10
