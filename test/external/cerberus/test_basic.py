from cerberus import Validator

dto_schema = dict(
    img=dict(
        type='string',
        empty=False,
    ),
    name=dict(
        type='string',
    ),
)


def test_empty_doc_is_success():
    document = {}
    assert Validator(dto_schema).validate(document)


def test_unknown_field_make_fail():
    document = {
        "k": "i1",
    }
    v = Validator()
    assert not v.validate(document, dto_schema)
    assert str(v.errors) == "{'k': ['unknown field']}"


def test_allow_unknown():
    document = {
        "k": "i1",
    }
    v = Validator()
    v.allow_unknown = True
    assert v.validate(document, dto_schema)


def test_empty_not_allowed():
    document = {
        "img": "",
    }
    v = Validator()
    assert not v.validate(document, dto_schema)
    assert str(v.errors) == "{'img': ['empty values not allowed']}"


def test_empty_allowed():
    document = {
        "img": "x",
        "name": "",
    }
    v = Validator()
    assert v.validate(document, dto_schema)


def test_root_list():
    schema = dict()
    document = [1, 2, 3]
    v = Validator(schema)
    assert v.validate(document)
