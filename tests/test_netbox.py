import pytest
from netbox.ip_address import IpV4Address


def test_ip_address(valid_ipv4_case):
    value, _ = valid_ipv4_case
    ip = IpV4Address(value)
    assert ip is not None


def test_ip_address_validation(valid_ipv4_case):
    value, expected_private = valid_ipv4_case
    ip = IpV4Address(value)
    assert ip is not None
    assert ip.mask == 32
    assert ip.is_private == expected_private


def test_ip_address_rejection(invalid_ipv4_value):
    with pytest.raises(ValueError):
        IpV4Address(invalid_ipv4_value)
