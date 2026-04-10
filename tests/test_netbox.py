import pytest

from kata.netbox import IPv4Address


def test_ip_address(valid_ipv4_case):
    value, _ = valid_ipv4_case
    ip = IPv4Address(value)
    assert ip is not None


def test_ip_address_validation(valid_ipv4_case):
    value, expected_private = valid_ipv4_case
    ip = IPv4Address(value)
    assert ip is not None
    assert ip.is_private == expected_private


def test_ip_address_rejection(invalid_ipv4_value):
    with pytest.raises(ValueError):
        IPv4Address(invalid_ipv4_value)


def test_explore_ip_address(valid_ipv4_case):
    value, _ = valid_ipv4_case
    ip = IPv4Address(value)
    assert str(ip) == value
    assert repr(ip) == f"IPv4Address({value})"
