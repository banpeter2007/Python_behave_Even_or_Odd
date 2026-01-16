"""
Szám ellenőrző modul - páros/páratlan ellenőrzés

TODO: Implementáld a check_number függvényt!
"""


def check_number(number):
    """
    Ellenőrzi, hogy a szám páros vagy páratlan.
    
    Args:
        number (int): Az ellenőrizendő szám
        
    Returns:
        str: "even" ha páros, "odd" ha páratlan
    """
    # TODO: Implementáld a logikát!
    # Használd a modulo operátort (%)
    # Ha number % 2 == 0, akkor páros → "even"
    # Egyébként páratlan → "odd"
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
