import re

testdata = (
    '"TYPE=UWSGI [pid: 20|app: -|req: -/-] 10.0.1.208 (-) {42 vars in 568 bytes} [Mon Apr 11 05:01:58 2022] GET /api/v1 - => generated 88 bytes in 14 msecs (HTTP/1.1 200) 2 head',
    '"TYPE=UWSGI [pid: 20|app: -|req: -/-] 10.0.1.208 (-) {42 vars in 568 bytes} [Mon Apr 11 05:01:58 2022] POST /api/v1 - => generated 88 bytes in 14 msecs (HTTP/1.1 200) 2 head',
)


def test_pattern():
    assert re.match(r"^.*GET.*HTTP/1.1 200.*$", testdata[0])
    assert not re.match(r"^.*GET.*HTTP/1.1 200.*$", testdata[1])

    assert not re.match(r"^.*POST.*HTTP/1.1 200.*$", testdata[0])
    assert re.match(r"^.*POST.*HTTP/1.1 200.*$", testdata[1])

    assert re.match(r"^.*(GET|POST).*HTTP/1.1 200.*$", testdata[0])
    assert re.match(r"^.*(GET|POST).*HTTP/1.1 200.*$", testdata[1])
