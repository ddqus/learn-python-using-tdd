example_response_type = dict(
    name=str,
    header=dict,
    childs=list,
)

example_header_type = dict(
    token=str,
)

example_response = {
    "name": "n1",
    "header": {
        "token": "t1",
    },
    "childs": [],
}


def validate(response_type: dict, response: dict):
    for key, value in response_type.items():
        if key not in response:
            raise ValueError(f"key not in response - {key}")

        assert isinstance(response[key], value)


def test_response_type():
    sut = validate
    sut(example_response_type, example_response)
    sut(example_header_type, example_response["header"])
