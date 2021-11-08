"""
This module tests the gateway.

test_version:
    tests if the current version is the correct one.
"""

from gateway import receive


def test_connection():
    """Tests connection."""
    assert receive.connection == "200"
