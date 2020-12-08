# File name: finditemdictlist.py
# Author: Kevin Rojas
# email: krojas.alfaro7@gmail.com
# Python Version: 3.8
# Funcion que encuentra y devuelve el elemento de una lista de diccionarios por llave y valor

def finditemdictlist(key="key", value="value", dictlist=[]):
    """
    Search and return the element of a dictionary list by key and item
    
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
