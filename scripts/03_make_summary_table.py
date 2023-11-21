#!/usr/bin/python3
import csv
from re import I

# Create Dictionary rilToLoc
rilToLoc = {}
with open('../results/insertion_and_rils.tsv', 'r') as file:
    ril_result_reader = csv.reader(file, delimiter='\t')
    next(ril_result_reader)
    for line in ril_result_reader:
        if line[1] in rilToLoc:
            rilToLoc[line[1]].append([line[0]])
        else:
            rilToLoc[line[1]] = [line[0]]

# Create Dictionary parentalToPing
parentToPing = {}
with open('../data_from_lit/parent_ping_loc.tsv', 'r') as file:
    parental_ping_reader = csv.reader(file, delimiter='\t')
    next(parental_ping_reader)
    for line in parental_ping_reader:
        print(line)
        if line[1] in parentToPing:
            parentToPing[line[1]].append([line[0]])
        else:
            parentToPing[line[1]] = [line[0]]




rilToLoc = {}

keys = [] #RIL names : list[Unknown]
values = [] #mPing locations : list[Unknown]
for file in file_list:
    table = pd.read_csv(file)
    name = os.path.basename(file) : str
    keys.append(name)
    value = (table['RIL_Start']) : Unknown
    values.append(value)

