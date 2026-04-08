import ipaddress


class IpV4Address:
    def __init__(self, address: str | ipaddress.IPv4Address):
        """
        by referencing the setter, we can ensure that the
        validation logic is applied when initializing the
        object
        """
        self.address = address

    @property
    def address(self) -> ipaddress.IPv4Address:
        return self._address

    @address.setter
    def address(self, value: str | ipaddress.IPv4Address):
        # if it is a string, try to convert it to an IPv4Address
        if isinstance(value, str):
            try:
                value = ipaddress.IPv4Address(value)
            except ipaddress.AddressValueError as exc:
                raise ValueError("Address must be a valid IPv4 address!") from exc
        if not isinstance(value, ipaddress.IPv4Address):
            raise ValueError("Address must be an IPv4 address!")
        self._address = value

    @property
    def is_private(self) -> bool:
        return self.address.is_private

    @property
    def mask(self) -> int:
        return self.address.max_prefixlen

    @property
    def is_global(self) -> bool:
        return self.address.is_global
