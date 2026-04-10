import ipaddress


class IPv4Address:
    def __init__(self, address: str | ipaddress.IPv4Address) -> None:
        self.address = address

    @property
    def address(self) -> ipaddress.IPv4Address:
        return self._address

    @address.setter
    def address(self, value: str | ipaddress.IPv4Address) -> None:
        if isinstance(value, str):
            try:
                value = ipaddress.IPv4Address(value)
            except ipaddress.AddressValueError as exc:
                raise ValueError("address must be a valid IPv4 address") from exc
        if not isinstance(value, ipaddress.IPv4Address):
            raise TypeError("address must be str or ipaddress.IPv4Address")
        self._address = value

    @property
    def is_private(self) -> bool:
        return self.address.is_private

    @property
    def is_global(self) -> bool:
        return self.address.is_global

    def __str__(self) -> str:
        return str(self.address)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.address!s})"
