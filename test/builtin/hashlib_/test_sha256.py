import hashlib

import pytest


def test_hash_need_encoding():
    with pytest.raises(TypeError) as exc_info:
        hashlib.sha256("xx")

    assert str(exc_info.value) == "Strings must be encoded before hashing"


def test_hash_return_HASH():
    sut = hashlib.sha256("xx".encode("utf-8"))
    assert str(type(sut)) == "<class '_hashlib.HASH'>"


def test_hash_hexdigest_return_str():
    sut = hashlib.sha256("xx".encode("utf-8")).hexdigest()
    assert isinstance(sut, str)
    assert sut == "5dde896887f6754c9b15bfe3a441ae4806df2fde94001311e08bf110622e0bbe"
