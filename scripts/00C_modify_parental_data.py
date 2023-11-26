# This script creates lists of ping insertions, and checks if known ping locations (from lit) are showing up in relocate results


import pandas as pd

# Read DataFrames
A123_relocate = pd.read_csv("../data_from_lit/A123_relocate_results.tsv", sep="\t")
EG4_relocate = pd.read_csv("../data_from_lit/EG4_relocate_results.tsv", sep="\t")
A123_ping = pd.read_csv("../data_from_lit/A123_ping.tsv", sep='\t', header=None)
EG4_ping = pd.read_csv("../data_from_lit/EG4_ping.tsv", sep='\t', header=None)

# Convert columns to lists
A123_relocate_list = A123_relocate["Chr_Start"].tolist()
EG4_relocate_list = EG4_relocate["Chr_Start"].tolist()
A123_ping_list = A123_ping[0].tolist()
EG4_ping_list = EG4_ping[0].tolist()

# Find common elements
A123_relocate_pings = [loc for loc in A123_relocate_list if loc in A123_ping_list]
EG4_relocate_pings = [loc for loc in EG4_relocate_list if loc in EG4_ping_list]

# Print the lists
print("Common locations in A123_relocate and A123_ping:", A123_relocate_pings)
print("Common locations in EG4_relocate and EG4_ping:", EG4_relocate_pings)


# Known Ping locations are not showing up in relocate results
