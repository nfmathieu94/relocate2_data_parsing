import csv

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
ril_to_loc = create_dict(path_to_ril_data)
del ril_to_loc['Undetermined_S0']  # Remove 'Undetermined_S0' entry if needed

# Create dictionary (PARENT : [PingLocations, ...], ...)
# Locations found from previous paper
parental_to_ping = create_dict(path_to_parental_ping)

# Create dictionary (PARENT : [RelocateInsertions, ...], ...)
parental_to_relocate = create_dict(path_to_parental_relocate)

# Flatten the lists of locations for parental pings, RILs, and parental relocate results
parental_ping_locations = [location for locations in parental_to_ping.values() for location in locations]
ril_locations = [location for locations in ril_to_loc.values() for location in locations]
parental_relocate_locations = [location for locations in parental_to_relocate.values() for location in locations]

# Convert values to sets for both parental pings, RILs, and parental relocate results
parental_ping_locations_set = set(parental_ping_locations)
ril_locations_set = set(ril_locations)
parental_relocate_locations_set = set(parental_relocate_locations)

# Find common locations between parental pings and RILs
common_locations_ril = parental_ping_locations_set & ril_locations_set
total_common_locations_ril = len(common_locations_ril)
print(f'Total number of parental pings shared in RIL locations: {total_common_locations_ril}')

# Find common locations between parental pings and parental relocate results
common_locations_parental_ping_relocate = parental_ping_locations_set & parental_relocate_locations_set
total_common_locations_parental_ping_relocate = len(common_locations_parental_ping_relocate)
print(f'Total number of parental pings shared with parental relocate results: {total_common_locations_parental_ping_relocate}')

