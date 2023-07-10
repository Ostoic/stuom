"""Functions for parsing `Duration`s from strings."""

from stuom.duration import (
    Duration,
    Hours,
    HundredNanoseconds,
    Microseconds,
    Milliseconds,
    Minutes,
    Nanoseconds,
    Seconds,
)


def find_minimal_si(d: Duration) -> Duration:
    """Parse the duration and use the `Duration` subclass that represents the duration in the
    lowest number of digits.

    Args:
        d (Duration): The duration to parse

    Returns:
        str: The
    """
    duration_us = d.convert_duration(Microseconds)
    duration_ms = d.convert_duration(Milliseconds)
    if duration_ms >= Milliseconds(1000):
        return d.convert_duration(Seconds)

    if duration_us >= Microseconds(1000):
        return d.convert_duration(Milliseconds)

    else:
        return duration_us


def parse_minimal_si(d: Duration) -> str:
    """Parse the minimal duration subclass.

    Args:
        d (Duration): The duration to process.

    Returns:
        str: The minimal subclass as a string.
    """
    return str(find_minimal_si(d))


def parse_duration(ts_str: str) -> Duration:
    """Parse a `Duration` from a string."""
    if len(ts_str) <= 1:
        raise ValueError(f"Invalid timestamp string: {ts_str}")

    ts_str = ts_str.lower()
    if "hr" in ts_str:
        return Hours(ts_str.replace("hrs", "").replace("hr", ""))

    if "min" in ts_str:
        return Minutes(ts_str.replace("mins", "").replace("min", ""))

    elif "ms" in ts_str:
        return Milliseconds(ts_str.replace("ms", ""))

    elif "us" in ts_str or "μs" in ts_str:
        return Microseconds(ts_str.replace("us", "").replace("μs", ""))

    elif "hns" in ts_str:
        return HundredNanoseconds(ts_str.replace("hns", ""))

    elif "ns" in ts_str:
        return Nanoseconds(ts_str.replace("ns", ""))

    # Note: Order is important since we want to run through all of the above cases before reaching
    # "s" otherwise this would match first.
    elif "s" in ts_str:
        return Seconds(ts_str.replace("s", ""))

    raise ValueError("No timestamp type specified!")
