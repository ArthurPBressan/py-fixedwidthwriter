# coding: utf-8

from fixedwidthwriter import FixedWidthWriter

cols = [
    ('ID', 5),
    ('NAME', 40),
    ('BALANCE', 6, {'direction': '>', 'decimal_spaces': 2}),
]

objs = [
    {'ID': 0, 'NAME': 'Jack', 'BALANCE': 100.50},
    {'ID': 1, 'NAME': 'Mary', 'BALANCE': 100}
]

with open('file.txt', 'wb') as fixed_file:
    fww = FixedWidthWriter(fixed_file, cols)
    fww.writerows(objs)