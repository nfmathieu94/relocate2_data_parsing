#!/usr/bin/python3
import pandas as pd

path_to_parental_ping = "../data_from_lit/parental_pings.csv"

parental_ping_df = pd.read_csv(path_to_parental_ping)

parental_ping_df["Chr_Start"] = parental_ping_df["Chromosome"].astype(str) + '_' + parental_ping_df["Start"].astype(str)

parental_subset_df = parental_ping_df[["Chr_Start", "Parent"]]

parental_subset_df.to_csv("../data_from_lit/parent_ping_loc.tsv", sep = '\t', header=True, index=False)

