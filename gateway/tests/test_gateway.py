"""
This module tests the gateway.

test_version:
    tests if the current version is the correct one.
"""
from gateway import __version__


def test_version():
    """Tests if the current version is the correct one."""
    assert __version__ == '0.1.0'
