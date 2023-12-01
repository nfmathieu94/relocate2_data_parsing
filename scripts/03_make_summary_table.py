#!/usr/bin/python3
import csv
import pandas as pd
from pandas.io.sql import com


# Function to read in file and create dictionary

def create_dict(path_to_file):
    line_to_loc = {}
    with open(path_to_file, 'r') as file:
        file_reader = csv.reader(file, delimiter='\t')
        next(file_reader)
        for line in file_reader:
            line_to_loc.setdefault(line[1], []).append(line[0])
    return line_to_loc

# File paths
path_to_ril_data = '../results/insertion_and_rils.tsv'
path_to_parental_ping = '../data_from_lit/parent_ping_loc.tsv'
path_to_parental_relocate = '../data_from_lit/all_parental_insertions.tsv'
path_to_old_parental = '../parental_old_relocate_calls/a123_eg4_relocate.tsv'


# Create dictionary (RIL : [mPingLocations, ...], ...)
ril_to_relocate = create_dict(path_to_ril_data)
del ril_to_relocate['Undetermined_S0']  # Remove 'Undetermined_S0' entry if needed



# Create dictionary (PARENT : [PingLocations, ...], ...)
# Locations found from previous paper
parental_to_ping = create_dict(path_to_parental_ping)

# Create dictionary (PARENT : [RelocateInsertions, ...], ...)
parental_to_relocate = create_dict(path_to_parental_relocate)

# Dictionary with relocate results ran by Jason
oldParent_to_relocate = create_dict(path_to_old_parental)


print(len(ril_to_relocate.values()))
print(len(parental_to_ping.values()))
print(len(parental_to_relocate.values()))
print(len(oldParent_to_relocate.values()))

# Count 
n = 0
for ril in ril_to_relocate:
    for loc in ril_to_relocate[ril]:
        n += 1

print(n)

     ### Comparing RIL and Parental Insertions ###

# Count Shared Values 
n = 0
for line in oldParent_to_relocate:
    for loc in oldParent_to_relocate[line]:
        for ril in ril_to_relocate:
            if loc in ril_to_relocate[ril]:
                n += 1

print(n)

# Function to create a list of unique locations from dictionary
def get_uniq_loc_list(dictionary):
    loc_list = []
    for key in dictionary:
        for value in dictionary[key]:
            if value not in loc_list:
                loc_list.append(value)
    return loc_list

# Function to create a list of all locations from dictionary
def get_all_loc_list(dictionary):
    loc_list = []
    for key in dictionary:
        for value in dictionary[key]:
                loc_list.append(value)
    return loc_list



# Create lists with unique locations 
uniq_ril_relocate_list = get_uniq_loc_list(ril_to_relocate)
uniq_parent_relocate_list = get_uniq_loc_list(parental_to_relocate)
uniq_parental_ping_list = get_uniq_loc_list(parental_to_ping)
uniq_parental_relocate_list = get_uniq_loc_list(oldParent_to_relocate)

len(uniq_ril_relocate_list)


# Create lists with all locations 
ril_relocate_list = get_all_loc_list(ril_to_relocate)

parent_relocate_list = get_all_loc_list(parental_to_relocate)
parental_ping_list = get_all_loc_list(parental_to_ping)
old_parental_relocate_list = get_all_loc_list(oldParent_to_relocate)

len(ril_relocate_list)

# Creating a list of all RIL mPing locations
#uniq_ril_relocate_list = []
#for ril in ril_to_relocate:
#    for loc in ril_to_relocate[ril]:
#        if loc not in uniq_ril_relocate_list: # Change line if we want total locations
#            uniq_ril_relocate_list.append(loc)

# Creating list with all unique parental relocate locations  
#parent_relocate_list = []
#for parent in parental_to_relocate:
#    for loc in parental_to_relocate[parent]:
#        if loc not in parent_relocate_list: # Change line if we want total locations
#            parent_relocate_list.append(loc)

# Creating list with all unique ping locations. Use this later for different dataframe to find ping locations
#uniq_parental_ping_list = []
#for parent in parental_to_ping:
#    for loc in parental_to_ping[parent]:
#        if loc not in uniq_parental_ping_list:
#            uniq_parental_ping_list.append(loc)


# Creating combined dictionary parental and ril relocate locations 
combined_LineToLoc = {**ril_to_relocate, **parental_to_relocate}


# Create list that has all Parental and RIL locations
rilAndParent_relocate_list = uniq_ril_relocate_list + parent_relocate_list


BinaryCombined_relocate_dict = {}

for loc in rilAndParent_relocate_list:
    for line in combined_LineToLoc:
        if loc in combined_LineToLoc[line]:
            if line not in BinaryCombined_relocate_dict:
                BinaryCombined_relocate_dict[line] = {}
            BinaryCombined_relocate_dict[line][loc] = 1
        else:
            if line not in BinaryCombined_relocate_dict:
                BinaryCombined_relocate_dict[line] = {}
            BinaryCombined_relocate_dict[line][loc] = 0



combined_relocate_binary_df = pd.DataFrame(BinaryCombined_relocate_dict)








