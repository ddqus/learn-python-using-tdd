def sut(bootstrap_servers, **kwargs):
    return {
        "bootstrap.servers": bootstrap_servers,
        "request.timeout.ms": kwargs.get("request_timeout_ms", 2000),
        "delivery.timeout.ms": kwargs.get("delivery_timeout_ms", 2500),
    }


def test_custom_options():
    expected = {
        "bootstrap.servers": "bootstrap_servers",
        "request.timeout.ms": 1000,
        "delivery.timeout.ms": 1500,
    }
    assert sut("bootstrap_servers",
               request_timeout_ms=1000,
               delivery_timeout_ms=1500,
               ) == expected
