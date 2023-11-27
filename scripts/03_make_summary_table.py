#!/usr/bin/python3
import csv
import pandas as pd
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
del rilToLoc['Undetermined_S0'] # delete Undetermined dictionary entry


# Create Dictionary parentalToPing (parent : Chrom_Start (ping))
path_to_parental_ping = '../data_from_lit/parent_ping_loc.tsv'
parentalToPing = create_dict(path_to_parental_ping)


# Create Dictionary parentalToPong (parent : Chrom_Start (pong))
# Will fill this in later after prepping pong input data 


# Create Dictionary parentToAllLoc that has every mPing, Ping, and Pong location
# This will be used to create the origin column in the summary table
path_to_parental_relocate = '../data_from_lit/all_parental_insertions.tsv'
partentalToRelocaTE = create_dict(path_to_parental_relocate)


# Determining how many parental insertions are in RILs

# Create list that has all locations from parents (just locations no parental details)
# The list contains no repeats 
parent_relocate_list = []
for parent in partentalToRelocaTE:
    for loc in partentalToRelocaTE[parent]:
        if loc not in parent_relocate_list:
            parent_relocate_list.append(loc)


parent_relocate_list
len(rilToLoc.values())
rilToLoc


n = 0
for RIL in rilToLoc:
    for loc in rilToLoc[RIL]:
        if loc in parent_relocate_list:
            n += 1

print(n)


# Creating binary dataframe (p/a)
# creating list of all ril mPing locations
ril_loc_list = []
for ril in rilToLoc:
    for loc in rilToLoc[ril]:
        if loc not in ril_loc_list:
            ril_loc_list.append(loc)

# Creating Series of all possible RIL mPing loc (will be used as first column)
ril_chrom_start_series = pd.Series(ril_loc_list, name = 'Chr_Start')


## Newest idea. Want to do this but instead of parentalToPing or parentalToPong we make another dict parentToAllLoc (every mPing, Ping, or Pong location)
## For the Type column we will do something similar but with parentalToPing and parentalToPong 
origin_list = []
for i in range(0, len(ril_loc_list)):
    for line in parentAllLoc:
        if origin_list[i] in parentAllLoc[line]:
            origin_list.append(line)
        else:
            origin_list.append("de novo")





insertion_type_list = []
for i in range(0, len(ril_loc_list)):
    for line in parentalToPing:
        if ril_loc_list[i] in parentalToPing[line]:
            ping_origin_list.append("Ping")
        elif ril_loc_list [i] in parentalToPong:
            ping_origin_list.append("Pong")
#        



# Create series that has parental origin information (if a site is parental)
# Label RIL mPing as Ping if location is in parentalToPing
ril_ping

# Use dictionary of Series to create a dataframe
df = pd.DataFrame({'Chr_Start' : ril_chrom_start_series})


### TESTING ## 

mpinglocations = dict()

for RIL in rilToLoc:
    for loc in rilToLoc[RIL]:
        if loc not in mpinglocations:
            mpinglocations[loc] = {}
        mpinglocations[loc][RIL] = 1


mpinglocations

# Getting Ping loci in RIL mPing calls (mPing calls with same location are probably Ping)
rilToParentPing = {}
for parent in parentalToPing:
    for parent_loc in parentalToPing[parent]:
        for ril in rilToLoc:
            for ril_loc in rilToLoc[ril]:
                if ril not in rilToParentPing:
                    rilToParentPing[ril]  = {}
                for ril_loc in rilToLoc[ril]:
                    if ril_loc in parentalToPing.values():
                        rilToParentPing[ril] = {}
                        rilToParentPing[ril].append([parent][ril_loc])


rilToParentPing


rilToParentPing = {}
for parent in parentalToPing:
    for parent_loc in parentalToPing[parent]:
        if parent loc in:

        for ril in rilToLoc:
            if ril not in rilToParentPing:
                rilToParentPing[ril] = {}
                for ril_loc in rilToLoc[ril]:
                    if ril_loc in parentalToPing.values():
                         rilToParentPing[ril].append([parent][ril_loc])




rilToParentPing = {}
for ril in rilToLoc:
    if ril not in rilToParentPing:
        rilToParentPing[ril] = {}
    for ril_loc in rilToLoc[ril]:
        if ril_loc in parentalToPing:
            rilToParentPing[ril][parent] = [loc]  # append loc to the nested parental dictionary

# Want something like this:
#rilToParentPing = {'B_11' : {'A123' : ['Chr1_345', 'Chr2_12345'], EG4 : [Chr5_12354, Chr6_12354]}, 'B_12' : {'A123' : [Chr3_235, Chr5_1345], 'EG4' : ['Chr5_345', 'Chr7_434']}}

            for ril_loc in rilToLoc[ril]:


RILnames = sorted(listOfRILs.keys())
print("\t".join(RILnames))
for loc in mpinglocations:
    row = []
    for RIL in RILnames:
        if RIL in mpinglocations[loc]:
            row.append("1")
        else:
            row.append("0")
            print("\t".join(row))
