"""Units of measurement for working with lengths."""
from typing import TypeVar

from stuom.uom import HasSiOrder

LengthT = TypeVar("LengthT", bound="Length")


class Length(HasSiOrder):
    """A general-purpose SI-based length."""

    def convert_length(self, to_cls: type[LengthT]) -> LengthT:
        return self.convert_si(to_cls)

    @classmethod
    def from_length(cls: type[LengthT], other: "Length") -> LengthT:
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
