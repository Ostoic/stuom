"""Test unit of measurement parsing."""

import pytest
from stuom.parse import find_minimal_si, parse_duration, parse_minimal_si
from stuom.uom import (
    Hours,
    HundredNanoseconds,
    Microseconds,
    Milliseconds,
    Minutes,
    Nanoseconds,
    Seconds,
)


def test_parse_minimal_si():
    assert type(find_minimal_si(Milliseconds(0.05))) == Microseconds
    assert type(find_minimal_si(Milliseconds(5000))) == Seconds
    assert type(find_minimal_si(Milliseconds(5))) == Milliseconds
    assert parse_minimal_si(Milliseconds(0.05)) == "50.0us"
    assert parse_minimal_si(Milliseconds(5000)) == "5.0s"
    assert parse_minimal_si(Seconds(0.01)) == "10.0ms"


def test_parse():
    assert parse_duration("10hrs") == Hours(10)
    assert parse_duration("10mins") == Minutes(10)
    assert parse_duration("10s") == Seconds(10)
    assert parse_duration("10ms") == Milliseconds(10)
    assert parse_duration("10us") == Microseconds(10)
    assert parse_duration("10hns") == HundredNanoseconds(10)
    assert parse_duration("10ns") == Nanoseconds(10)

    with pytest.raises(ValueError):
        parse_duration("10x")

    with pytest.raises(ValueError):
        parse_duration("1")
