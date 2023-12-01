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


# Creating sets that will be used to compare insertion sites (will probably make function for this later)

# Create set of Ping locations from Literature
#parental_ping_locations_set = set()
#for locations in parental_to_ping.values():
#    parental_ping_locations_set.update(locations)

# Create set of RIL insertions identified from Relocate
#ril_locations_set = set()
#for locations in ril_to_relocate.values():
#    ril_locations_set.update(locations)

# Create set of Parental insertions identified from Relocate 
#parental_relocate_locations_set = set()
#for locations in parental_to_relocate.values():
#    parental_relocate_locations_set.update(locations)


               ########## Finding Shared Ping locations (from literature) in RIL Relocate results ##########


# Find common locations between parental pings and RILs
#common_locations = parental_ping_locations_set & ril_locations_set

# Count the total number of common locations
#total_common_locations = len(common_locations)

#print(f'Total number of parental pings shared in RIL locations: {total_common_locations}')


               ########## Finding Shared Ping locations (from literature) in Parental (EG4 and A123) Relocate results ##########


# Find common locations between parental pings and parental relocate results
#common_locations_parental_ping_relocate = parental_ping_locations_set & parental_relocate_locations_set


# Count the total number of common locations
#total_common_locations_parental_ping_relocate = len(common_locations_parental_ping_relocate)

#print(f'Total number of parental pings shared with parental relocate results: {total_common_locations_parental_ping_relocate}')





               ########## Finding Shared relocate locations between Parental (EG4 and A123) and RILs ##########


# Find common locations between parental and RIL relocate results
#common_locations_relocate_parent_ril = parental_relocate_locations_set & ril_locations_set

# Count the total number of common locations
#total_common_locations_relocate_parent_ril = len(common_locations_relocate_parent_ril)

#print(f'Total number of parental relocate insertions shared with RIL relocate insertions: {total_common_locations_relocate_parent_ril}')




               ########## Sumamry So Far ##########

# Looks like there are no shared pings in the parental relocate results and 15 ping locations in the RIL relocate results
# Might be because specific coordinate calls are off?? 



# Comparing values between parents and RILs 

n = 0
for line in oldParent_to_relocate:
    for loc in oldParent_to_relocate[line]:
        for ril in ril_to_relocate:
            if loc in ril_to_relocate[ril]:
                n += 1


# Creating a binary dictionary where each 
#binary_ril_dict = {'RIL': list(ril_to_relocate.keys())}




               ########## Creating Binary DataFrame ##########

# Creating a list of all RIL mPing locations
ril_relocate_list = []
for ril in ril_to_relocate:
    for loc in ril_to_relocate[ril]:
        if loc not in ril_relocate_list: # Change line if we want total locations
            ril_relocate_list.append(loc)

# Creating list with all unique parental relocate locations  
parent_relocate_list = []
for parent in parental_to_relocate:
    for loc in parental_to_relocate[parent]:
        if loc not in parent_relocate_list: # Change line if we want total locations
            parent_relocate_list.append(loc)

# Creating list with all unique ping locations. Use this later for different dataframe to find ping locations
parental_ping_list = []
for parent in parental_to_ping:
    for loc in parental_to_ping[parent]:
        if loc not in parental_ping_list:
            parental_ping_list.append(loc)


# Creating combined dictionary parental and ril relocate locations 
combined_LineToLoc = {**ril_to_relocate, **parental_to_relocate}


# Create list that has all Parental and RIL locations
rilAndParent_relocate_list = ril_relocate_list + parent_relocate_list


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



# Create binary data frame 

#binary_df = pd.DataFrame(binary_dict)
#print(binary_df)

combined_relocate_binary_df = pd.DataFrame(BinaryCombined_relocate_dict)

combined_relocate_binary_df = combined_relocate_binary_df.T

combined_relocate_binary_df

# Transpose the data frame
#binary_df = binary_df.T

# Write to file with just RIL locations 
binary_df.to_csv("../results/ril_relocate_binary_table.tsv", sep='\t')



# Adding "Origin" column that gives information on whether the insertion came from a parent or is de novo 
binary_df['Origin'] = 'de novo'

# Iterate through the DataFrame and update "Origin" column
for loc in binary_df.index:
    for parent, locations in parental_to_relocate.items():
        if loc in locations:
            binary_df.at[loc, 'Origin'] = parent


binary_df.to_csv("../results/binary_df_with_origin.tsv", sep='\t')









               ########## Testing / Brainstorming ##########



# Checking insertion counts 
binary_df['B_11'].value_counts()[1]


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
