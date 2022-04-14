"""This is to test the lib module"""

from usb_flasher import lib

def test_join():
    """
    GIVEN a list of strings
    RETURN the string conatenated
    """
    expected = 'abcd'
    actual = lib.join(['a','b','c','d'])
    assert (expected == actual)
