#!/usr/bin/python3
import csv
import pandas as pd


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

# Create dictionary (RIL : [mPingLocations, ...], ...)
ril_to_relocate = create_dict(path_to_ril_data)
del ril_to_relocate['Undetermined_S0']  # Remove 'Undetermined_S0' entry if needed


# Create dictionary (PARENT : [PingLocations, ...], ...)
# Locations found from previous paper
parental_to_ping = create_dict(path_to_parental_ping)

# Create dictionary (PARENT : [RelocateInsertions, ...], ...)
parental_to_relocate = create_dict(path_to_parental_relocate)


               ########## Finding Shared Ping locations (from literature) in RIL Relocate results ##########

# Convert values to sets for both parental pings and RILs
parental_ping_locations_set = set()
for locations in parental_to_ping.values():
    parental_ping_locations_set.update(locations)

ril_locations_set = set()
for locations in ril_to_relocate.values():
    ril_locations_set.update(locations)

# Find common locations between parental pings and RILs
common_locations = parental_ping_locations_set & ril_locations_set

# Count the total number of common locations
total_common_locations = len(common_locations)

print(f'Total number of parental pings shared in RIL locations: {total_common_locations}')


               ########## Finding Shared Ping locations (from literature) in Parental (EG4 and A123) Relocate results ##########

# Convert values to sets for both parental pings and parental relocate results
parental_ping_locations_set = set()
for locations in parental_to_ping.values():
    parental_ping_locations_set.update(locations)

parental_relocate_locations_set = set()
for locations in parental_to_relocate.values():
    parental_relocate_locations_set.update(locations)

# Find common locations between parental pings and parental relocate results
common_locations_parental_ping_relocate = parental_ping_locations_set & parental_relocate_locations_set


# Count the total number of common locations
total_common_locations_parental_ping_relocate = len(common_locations_parental_ping_relocate)

print(f'Total number of parental pings shared with parental relocate results: {total_common_locations_parental_ping_relocate}')


len(parental_relocate_locations_set)
len(parental_ping_locations_set)




               ########## Sumamry So Far ##########

# Looks like there are no shared Pings in the parental or RIL relocate results)
# Might be because specific coordinate calls are off?? 






               ########## Creating Binary DataFrame ##########

# Creating a list of all RIL mPing locations
ril_relocate_list = []
for ril in ril_to_relocate:
    for loc in ril_to_relocate[ril]:
        if loc not in ril_relocate_list:
            ril_relocate_list.append(loc)

# Creating a binary dictionary where each 
binary_dict = {'RIL': list(ril_to_relocate.keys())}
for loc in ril_relocate_list:
    binary_dict[loc] = [1 if loc in ril_to_relocate[ril] else 0 for ril in ril_to_relocate]


# Create binary data frame 
binary_df = pd.DataFrame(binary_dict)
print(binary_df)

# Transpose the data frame
binary_df_T = binary_df.T

# Write to file
binary_df_T.to_csv("../results/ril_relocate_binary_table.tsv", sep='\t', index=False)





               ########## Testing / Brainstorming ##########





# Creating Series of all possible RIL mPing loc (will be used as first column)
ril_chrom_start_series = pd.Series(ril_relocate_list, name = 'Chr_Start')


## Newest idea. Want to do this but instead of parental_to_ping or parental_to_pong we make another dict parent_to_all_loc (every mPing, Ping, or Pong location)
## For the Type column we will do something similar but with parental_to_ping and parental_to_pong 
origin_list = []
for i in range(0, len(ril_relocate_list)):
    for line in parental_to_relocate:
        if origin_list[i] in parental_to_relocate[line]:
            origin_list.append(line)
        else:
            origin_list.append("de novo")





insertion_type_list = []
for i in range(0, len(ril_loc_list)):
    for line in parental_to_ping:
        if ril_loc_list[i] in parental_to_ping[line]:
            ping_origin_list.append("Ping")
        elif ril_loc_list [i] in parental_to_pong:
            ping_origin_list.append("Pong")
#        



# Create series that has parental origin information (if a site is parental)
# Label RIL mPing as Ping if location is in parental_to_ping
ril_ping

# Use dictionary of Series to create a dataframe
df = pd.DataFrame({'Chr_Start' : ril_chrom_start_series})


### TESTING ## 

mpinglocations = dict()

for RIL in ril_to_relocate:
    for loc in ril_to_relocate[RIL]:
        if loc not in mpinglocations:
            mpinglocations[loc] = {}
        mpinglocations[loc][RIL] = 1


mpinglocations

# Getting Ping loci in RIL mPing calls (mPing calls with same location are probably Ping)
rilToParentPing = {}
for parent in parental_to_ping:
    for parent_loc in parental_to_ping[parent]:
        for ril in ril_to_relocate:
            for ril_loc in ril_to_relocate[ril]:
                if ril not in rilToParentPing:
                    rilToParentPing[ril]  = {}
                for ril_loc in ril_to_relocate[ril]:
                    if ril_loc in parental_to_ping.values():
                        rilToParentPing[ril] = {}
                        rilToParentPing[ril].append([parent][ril_loc])


rilToParentPing


rilToParentPing = {}
for parent in parental_to_ping:
    for parent_loc in parental_to_ping[parent]:
        if parent loc in:

        for ril in ril_to_relocate:
            if ril not in rilToParentPing:
                rilToParentPing[ril] = {}
                for ril_loc in ril_to_relocate[ril]:
                    if ril_loc in parental_to_ping.values():
                         rilToParentPing[ril].append([parent][ril_loc])




rilToParentPing = {}
for ril in ril_to_relocate:
    if ril not in rilToParentPing:
        rilToParentPing[ril] = {}
    for ril_loc in ril_to_relocate[ril]:
        if ril_loc in parental_to_ping:
            rilToParentPing[ril][parent] = [loc]  # append loc to the nested parental dictionary

# Want something like this:
#rilToParentPing = {'B_11' : {'A123' : ['Chr1_345', 'Chr2_12345'], EG4 : [Chr5_12354, Chr6_12354]}, 'B_12' : {'A123' : [Chr3_235, Chr5_1345], 'EG4' : ['Chr5_345', 'Chr7_434']}}

            for ril_loc in ril_to_relocate[ril]:


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
