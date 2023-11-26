#!/usr/bin/python3
import csv

## Add a function to create dictionary to reduce redundant code ##

def create_dict(path_to_file):
    lineToLoc = {}
    with open(path_to_file, 'r') as file:
        file_reader = csv.reader(file, delimiter='\t')
        next(file_reader)
        for line in file_reader:
            if line[1] in lineToLoc:
                lineToLoc[line[1]].append(line[0])
            else:
                lineToLoc[line[1]] = [line[0]]
    return lineToLoc




# Create Dictionary rilToLoc (ril : Chrom_Start)
path_to_ril_data = '../results/insertion_and_rils.tsv'
rilToLoc = create_dict(path_to_ril_data)

# Create Dictionary parentalToPing (parent : Chrom_Start (ping))
path_to_parental_ping = '../data_from_lit/parent_ping_loc.tsv'
parentalToPing = create_dict(path_to_parental_ping)

# Create Dictionary parentalToPong (parent : Chrom_Start (pong))
mpinglocations = dict()

for RIL in rilToLoc:
    for loc in rilToLoc[RIL]:
        if loc not in mpinglocations:
            mpinglocations[loc] = {}
        mpinglocations[loc][RIL] = 1

RILnames = sorted(listOfRILs.keys()
print("\t".join(RILnames))
for loc in mpinglocations:
    row = []
    for RIL in RILnames:
        if RIL in mpinglocations[loc]:
            row.append("1")
        else:
            row.append("0")
            print("\t".join(row))
