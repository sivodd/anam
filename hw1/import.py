#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
f = open("airports.txt")
for row in csv.reader(f):
    print(row[1])