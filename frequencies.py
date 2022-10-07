"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items: 
        key = str(item)
        if(key in frequencies.keys()):
            frequencies[key] = frequencies[key] + 1
        else:
            frequencies[key] = 1
    print(frequencies)
    return frequencies

