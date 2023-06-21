"""Contains units of measurement for working with electricity units such as power."""
from stuom.uom import HasSiOrder


class ElectricPotential(HasSiOrder):
    """A unit of measurement representing electric potential."""


class Kilovolts(ElectricPotential):
    """kV."""
    def __str__(self) -> str:
        return super().__str__() + "kV"

    @staticmethod
    def order() -> int:
        return -3


class Volts(ElectricPotential):
    """V."""
    def __str__(self) -> str:
        return super().__str__() + "V"

    @staticmethod
    def order() -> int:
        return 0


class Millivolts(ElectricPotential):
    """mV."""
    def __str__(self) -> str:
        return super().__str__() + "mV"

    @staticmethod
    def order() -> int:
        return 3


class Power(HasSiOrder):
    """The amount of energy transferred per unit time."""
    pass


class Watts(Power):
    """W."""
    def __str__(self) -> str:
        return super().__str__() + "W"

    @staticmethod
    def order() -> int:
        return 0

    @staticmethod
    def from_current_and_potential(current: "Current", potential: ElectricPotential) -> "Watts":
        return Watts(Amps.from_si(current) * Volts.from_si(potential))


class Deciwatts(Power):
    """dW."""
    def __str__(self) -> str:
        return super().__str__() + "dW"

    @staticmethod
    def order() -> int:
        return 1


class Milliwatts(Power):
    """mW."""
    def __str__(self) -> str:
        return super().__str__() + "mW"

    @staticmethod
    def order() -> int:
        return 3


class Current(HasSiOrder):
    """A unit of measurement representing electric current."""


class Amps(Current):
    """A."""
    def __str__(self) -> str:
        return super().__str__() + "A"

    @staticmethod
    def order() -> int:
        return 0


class Milliamps(Current):
    """mA."""
    def __str__(self) -> str:
        return super().__str__() + "mA"

    @staticmethod
    def order() -> int:
        return 3


class Microamps(Current):
    """uA."""
    def __str__(self) -> str:
        return super().__str__() + "uA"

    @staticmethod
    def order() -> int:
        return 6
