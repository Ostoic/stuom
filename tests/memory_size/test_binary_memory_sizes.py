"""Test computer memory size units of measurement following the IEC binary convention."""

import pytest
from stuom.memory_size import Bytes, GibiBytes, KibiBytes, MebiBytes, PebiBytes, TebiBytes


def test_bytes_to_kibibytes_conversion():
    assert KibiBytes.from_memory_size(Bytes(2**10)) == pytest.approx(KibiBytes(1))

def test_bytes_to_mebibytes_conversion():
    assert MebiBytes.from_memory_size(Bytes(2**20)) == pytest.approx(MebiBytes(1))

def test_bytes_to_gibibytes_conversion():
    assert GibiBytes.from_memory_size(Bytes(2**30)) == pytest.approx(GibiBytes(1))

def test_bytes_to_tebibytes_conversion():
    assert TebiBytes.from_memory_size(Bytes(2**40)) == pytest.approx(TebiBytes(1))

def test_bytes_to_pebibytes_conversion():
    assert PebiBytes.from_memory_size(Bytes(2**50)) == pytest.approx(PebiBytes(1))

