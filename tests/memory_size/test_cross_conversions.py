"""Test computer memory size units of measurement."""

import pytest
from stuom import (
    GigaBytes,
    KibiBytes,
    KiloBytes,
    MegaBytes,
    PetaBytes,
    TeraBytes,
)


def test_bytes_to_kilobytes_conversion():
    assert KiloBytes.from_memory_size(KibiBytes(1)) == pytest.approx(KiloBytes(1.024))


def test_bytes_to_megabytes_conversion():
    assert MegaBytes.from_memory_size(KibiBytes(1)) == pytest.approx(
        MegaBytes(1.024e-3)
    )


def test_bytes_to_gigabytes_conversion():
    assert GigaBytes.from_memory_size(KibiBytes(1)) == pytest.approx(
        GigaBytes(1.024e-6)
    )


def test_bytes_to_terabytes_conversion():
    assert TeraBytes.from_memory_size(KibiBytes(1)) == pytest.approx(
        TeraBytes(1.024e-9)
    )


def test_bytes_to_petabytes_conversion():
    assert PetaBytes.from_memory_size(KibiBytes(1)) == pytest.approx(
        PetaBytes(1.024e-12)
    )
