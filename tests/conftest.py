import pytest


VALID_IPV4_CASES = [
    ("192.168.1.1", True),
    ("8.8.8.8", False),
]

INVALID_IPV4_VALUES = [
    "256.256.256.256",
    "192.168.1.256",
    "10.0.0.256",
]


@pytest.fixture(
    params=VALID_IPV4_CASES,
    ids=[value for value, _ in VALID_IPV4_CASES],
)
def valid_ipv4_case(request):
    return request.param


@pytest.fixture(
    params=INVALID_IPV4_VALUES,
    ids=INVALID_IPV4_VALUES,
)
def invalid_ipv4_value(request):
    return request.param
