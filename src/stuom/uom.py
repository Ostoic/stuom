"""Simple statically-typed unit of measurements with order conversions."""

import math
from abc import abstractmethod
from typing import Self, TypeVar

DurationT = TypeVar("DurationT", bound="Duration")
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


class Duration(HasSiOrder):
    """Represents a duration and is functionally equivalent to its base."""

    def convert_duration(self, to_cls: type[DurationT]) -> DurationT:
        return _convert_si(self, to_cls)

    @classmethod
    def from_duration(cls, other: "Duration"):
        return other.convert_duration(cls)


class Hours(Duration):
    """hrs."""

    def __str__(self) -> str:
        return super().__str__() + "hrs"

    @staticmethod
    def order() -> float:
        return -math.log(3600, 10)


class Minutes(Duration):
    """mins."""

    def __str__(self) -> str:
        return super().__str__() + "mins"

    @staticmethod
    def order() -> float:
        return -(math.log(6, 10) + 1)


# Seconds-based SI units
class Seconds(Duration):
    """s."""

    def __str__(self) -> str:
        return super().__str__() + "s"

    @staticmethod
    def order() -> float:
        return 0


class Milliseconds(Duration):
    """ms."""

    def __str__(self) -> str:
        return super().__str__() + "ms"

    @staticmethod
    def order() -> float:
        return 3


class Microseconds(Duration):
    """us."""

    def __str__(self) -> str:
        return super().__str__() + "us"

    @staticmethod
    def order() -> float:
        return 6


class HundredNanoseconds(Duration):
    """hns."""

    def __str__(self) -> str:
        return super().__str__() + "hns"

    @staticmethod
    def order() -> float:
        return 7


class Nanoseconds(Duration):
    def __str__(self) -> str:
        return super().__str__() + "ns"

    @staticmethod
    def order() -> float:
        return 9


def _convert_si(from_value: HasSiOrder, to_cls: type[SiT]) -> SiT:
    return to_cls(from_value * 10 ** (to_cls.order() - from_value.order()))


LengthT = TypeVar("LengthT", bound="Length")


class Length(HasSiOrder):
    """A general-purpose SI-based length."""

    def convert_length(self, to_cls: type[LengthT]) -> LengthT:
        return _convert_si(self, to_cls)

    @classmethod
    def from_length(cls, other: "Length") -> Self:
        return other.convert_length(cls)


class Meters(Length):  # noqa: D101
    """m."""

    def __str__(self) -> str:  # noqa: D105
        return super().__str__() + "m"

    @staticmethod
    def order() -> int:
        return 0


class Centimeters(Length):
    """cm."""

    def __str__(self) -> str:
        return super().__str__() + "cm"

    @staticmethod
    def order() -> int:
        return 2


class Milimeters(Length):
    """mm."""

    def __str__(self) -> str:
        return super().__str__() + "mm"

    @staticmethod
    def order() -> int:
        return 3


class Micrometers(Length):
    """um."""

    def __str__(self) -> str:
        return super().__str__() + "um"

    @staticmethod
    def order() -> int:
        return 6


class Nanometers(Length):
    """nm."""

    def __str__(self) -> str:
        return super().__str__() + "nm"

    @staticmethod
    def order() -> int:
        return 9


class Angstroms(Length):
    """lambda."""

    @staticmethod
    def order() -> int:
        return 10


class ReciprocalLength(HasSiOrder):
    """1 / `Length`."""

    # def reciprocate(self) -> HasSiOrder:
    #     return Length()


class ReciprocalMeters(ReciprocalLength):
    """m^-1."""

    @staticmethod
    def order() -> int:
        return 0

    def to_meters(self) -> Meters:
        return Meters(1 / self)


class ReciprocalCentimeters(ReciprocalLength):
    """cm^-1."""

    @staticmethod
    def order() -> int:
        return 2


class ReciprocalMilimeters(ReciprocalLength):
    """mm^-1."""

    @staticmethod
    def order() -> int:
        return 3


class ReciprocalMicrometers(ReciprocalLength):
    """um^-1."""

    @staticmethod
    def order() -> int:
        return 6
