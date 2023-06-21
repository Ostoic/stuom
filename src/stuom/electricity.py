from stuom.uom import HasSiOrder


class ElectricPotential(HasSiOrder):
    """A unit of measurement representing electric potential."""


class Kilovolts(ElectricPotential):
    def __str__(self) -> str:
        return super().__str__() + "kV"

    @staticmethod
    def order() -> int:
        return -3


class Volts(ElectricPotential):
    def __str__(self) -> str:
        return super().__str__() + "V"

    @staticmethod
    def order() -> int:
        return 0


class Millivolts(ElectricPotential):
    def __str__(self) -> str:
        return super().__str__() + "mV"

    @staticmethod
    def order() -> int:
        return 3


class Power(HasSiOrder):
    pass


class Watts(Power):
    def __str__(self) -> str:
        return super().__str__() + "W"

    @staticmethod
    def order() -> int:
        return 0

    @staticmethod
    def from_current_and_potential(current: "Current", potential: ElectricPotential) -> "Watts":
        return Watts(Amps.from_si(current) * Volts.from_si(potential))


class Deciwatts(Power):
    def __str__(self) -> str:
        return super().__str__() + "dW"

    @staticmethod
    def order() -> int:
        return 1


class Milliwatts(Power):
    def __str__(self) -> str:
        return super().__str__() + "mW"

    @staticmethod
    def order() -> int:
        return 3


class Current(HasSiOrder):
    """A unit of measurement representing electric current."""


class Amps(Current):
    def __str__(self) -> str:
        return super().__str__() + "A"

    @staticmethod
    def order() -> int:
        return 0


class Milliamps(Current):
    def __str__(self) -> str:
        return super().__str__() + "mA"

    @staticmethod
    def order() -> int:
        return 3


class Microamps(Current):
    def __str__(self) -> str:
        return super().__str__() + "uA"

    @staticmethod
    def order() -> int:
        return 6
