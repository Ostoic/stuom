"""Test unit of measurement types."""
import math

from stuom import (
    Angstroms,
    Deciwatts,
    Hours,
    HundredNanoseconds,
    Kilovolts,
    Meters,
    Microamps,
    Microseconds,
    Milimeters,
    Milliseconds,
    Minutes,
    Nanoseconds,
    ReciprocalCentimeters,
    ReciprocalMeters,
    Seconds,
    Watts,
)


def test_duration_uom():
    assert math.isclose(Minutes.from_duration(Hours(2)), Minutes(60 * 2))
    assert math.isclose(Hours(2).convert_duration(Minutes), Minutes(60 * 2))
    assert math.isclose(Minutes.from_duration(Seconds(10)), Minutes(1 / 6))
    assert math.isclose(Seconds.from_duration(Minutes(10)), 10 * 60)
    assert math.isclose(Milliseconds.from_duration(Minutes(10)), 10 * 60 * 1000)
    assert math.isclose(Microseconds.from_duration(Minutes(10)), 10 * 60 * 1000 * 1000)
    assert math.isclose(Nanoseconds.from_duration(Minutes(10)), 10 * 60 * 1000 * 1000 * 1000)
    assert math.isclose(HundredNanoseconds.from_duration(Minutes(10)), 10 * 60 * 1000 * 1000 * 10)


def test_length_uom():
    assert math.isclose(Meters(0.005), Milimeters(5).convert_length(Meters))
    assert math.isclose(Meters(1), Meters.from_length(Milimeters(1000)))
    assert math.isclose(Meters(2), Meters.from_length(Angstroms.from_length(Meters(2))))
    assert math.isclose(Meters(2).convert_si(Angstroms), Angstroms(2e10))
    assert math.isclose(Angstroms(2e10).convert_si(Meters), Meters(2))

    assert math.isclose(
        ReciprocalMeters(10e-2).convert_si(ReciprocalCentimeters).convert_si(ReciprocalMeters),
        ReciprocalMeters(10e-2),
    )

    assert math.isclose(
        ReciprocalMeters(1).convert_si(ReciprocalCentimeters),
        ReciprocalCentimeters(100),
    )

    assert math.isclose(ReciprocalMeters(10e-2).to_meters(), Meters(1 / 10e-2))


def test_electricity_uom():
    power = Watts.from_current_and_potential(Microamps(225), Kilovolts(20))
    assert power == Watts(4.5)
    assert Deciwatts.from_si(power) == 45

