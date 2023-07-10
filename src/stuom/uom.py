"""Simple statically-typed unit of measurements with order conversions."""

from abc import abstractmethod
from typing import TypeAlias, TypeVar

SiT = TypeVar("SiT", bound="HasSiOrder")
IntT: TypeAlias = int | float


# SI unit types
class HasSiOrder(float):
    """Represents a unit of measurement type that has an SI order at the type level."""

    @staticmethod
    @abstractmethod
    def order() -> float:
        raise NotImplementedError()

    def convert_si(self, to_cls: type[SiT]) -> SiT:
        return _convert_si(self, to_cls)

    @classmethod
    def from_si(cls: type[SiT], other: "HasSiOrder") -> SiT:
        return other.convert_si(cls)

    def __mul__(self: SiT, value: IntT) -> SiT:
        self_type = type(self)
        return self_type(float.__mul__(self, value))

    def __add__(self: SiT, value: IntT) -> SiT:
        self_type = type(self)
        return self_type(float.__add__(self, value))

    def __sub__(self: SiT, value: IntT) -> SiT:
        self_type = type(self)
        return self_type(float.__sub__(self, value))

    def __truediv__(self: SiT, value: IntT) -> SiT:
        self_type = type(self)
        return self_type(float.__truediv__(self, value))

    def __floordiv__(self: SiT, value: IntT) -> SiT:
        self_type = type(self)
        return self_type(float.__floordiv__(self, value))


def _convert_si(from_value: HasSiOrder, to_cls: type[SiT]) -> SiT:
    return to_cls(from_value * 10 ** (to_cls.order() - from_value.order()))
