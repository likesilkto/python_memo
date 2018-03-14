#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

byte = b'\xff\xee'
u8 = np.asarray( [255, 238], dtype=np.uint8 )

frombyte = np.asarray( bytearray(byte), dtype=np.uint8 )
fromu8 = bytes( u8.tolist() )

print(byte)
print(fromu8)

print(u8)
print(frombyte)

