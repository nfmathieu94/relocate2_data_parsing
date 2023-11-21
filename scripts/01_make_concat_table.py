#!/usr/bin/python
import pandas as pd
import os
import glob

#Paths to ril and parental insertion calls  
path_to_ril_files = "../relocate_summary_results/"
path_to_parental_files = "../data_from_lit"

# Creating file lists for rils and parents
ril_file_list = glob.glob(path_to_ril_files + "*")
parental_file_list = glob.glob(path_to_parental_files + "*")

# Columns that we are interested in grabbing
columns_to_grab = [0, 2, 3, 4, 6]

# Initialize empty df list to store concatenated data
ril_df_list = []

# Make for loop to read in data
for file in ril_file_list:
    # create df for each ril file
    ril_df = pd.read_csv(file, sep='\t', header=None)
    # Subsetting for columns of interested
    ril_selected_columns = ril_df.iloc[:, columns_to_grab]
    # Appending subsetted ril df to a list
    ril_df_list.append(ril_selected_columns)

# Concatenate the list of dfs into one dataframe
ril_concatenated_df = pd.concat(ril_df_list, ignore_index=True)

# Changing chromosome names to "Chr#"
# read in file that has replacement text
replace_file = "../annotation_data/chrom_nums.csv"
replace_df = pd.read_csv(replace_file)
replace_df['chr'] = 'Chr' + replace_df['chr'].astype(str)
replacement_dict = dict(zip(replace_df['acc'], replace_df['chr']))

# Create function to do the replacement
def replace_text(input_text, replacement_dict):
    for key, value in replacement_dict.items():
        input_text = input_text.replace(key, value)
    return input_text

# Use function to do the replacement
ril_concatenated_df[0] = ril_concatenated_df[0].apply(lambda x: replace_text(x, replacement_dict))

# Concatenating the first and third row so that we have Chr_Start

ril_concatenated_df[0] = ril_concatenated_df[0].astype(str) + '_' + ril_concatenated_df[3].astype(str)

# Might want to write the combined dataframe to a file 

ril_concatenated_df.to_csv("../results/ril_concatenated_relocate_results.tsv", sep='\t', header=False)


# Drop the original row (not working at the moment)
ril_concatenated_df = ril_concatenated_df.drop(3, axis=1)
# Reset index
ril_concatenated_df = ril_concatenated_df.reset_index(drop=True)

# Rename Columns
ril_concatenated_df.columns = ["Chr_Start", "Line", "Start", "End", "Strand"]

# Subset Columns
locAndLine_df = ril_concatenated_df[["Chr_Start", "Line"]]
locAndLine_df.to_csv("../results/insertion_and_rils.tsv", sep='\t', header=True, index=False)
#Future work for this script
# - Remove hard coded paths and get paths from user from command line

