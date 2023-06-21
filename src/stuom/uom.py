"""Simple statically-typed unit of measurements with order conversions."""

from abc import abstractmethod
from typing import Self, TypeVar

SiT = TypeVar("SiT", bound="HasSiOrder")


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
    def from_si(cls, other: "HasSiOrder") -> Self:
        return other.convert_si(cls)


def _convert_si(from_value: HasSiOrder, to_cls: type[SiT]) -> SiT:
    return to_cls(from_value * 10 ** (to_cls.order() - from_value.order()))
