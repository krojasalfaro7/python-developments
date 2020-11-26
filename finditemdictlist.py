"""
Search and return the element of a dictionary list by key and item
"""


def finditemdictlist(key="key", value="value", dictlist=[]):
    """

    :param key: item key
    :param value: item value
    :param dictlist: dictionary list
    :return: None or found item
    """
    elem = None
    for item in dictlist:
        if item[key] == value:
            elem = item
            break
    return elem
