"""Test computer memory size units of measurement."""

from stuom.memory_size import (
    Bytes,
    GigaBytes,
    KiloBytes,
    MegaBytes,
    PetaBytes,
    TeraBytes,
)


def test_bytes_to_kilobytes_conversion():
    assert KiloBytes.from_memory_size(Bytes(1e3)) == KiloBytes(1)


def test_bytes_to_megabytes_conversion():
    assert MegaBytes.from_memory_size(Bytes(1e6)) == MegaBytes(1)


def test_bytes_to_gigabytes_conversion():
    assert GigaBytes.from_memory_size(Bytes(1e9)) == GigaBytes(1)


def test_bytes_to_terabytes_conversion():
    assert TeraBytes.from_memory_size(Bytes(1e12)) == TeraBytes(1)


def test_bytes_to_petabytes_conversion():
    assert PetaBytes.from_memory_size(Bytes(1e15)) == PetaBytes(1)


def test_string_format_kilobytes():
    assert str(KiloBytes(20)) == "20.0 kB"


def test_string_format_megabytes():
    assert str(MegaBytes(20)) == "20.0 MB"


def test_string_format_gigabytes():
    assert str(GigaBytes(20)) == "20.0 GB"


def test_string_format_terabytes():
    assert str(TeraBytes(20)) == "20.0 TB"


def test_string_format_petabytes():
    assert str(PetaBytes(20)) == "20.0 PB"
