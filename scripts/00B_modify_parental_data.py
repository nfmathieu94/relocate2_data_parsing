import pandas as pd

# Function to split a string based on separator and position
def split_on_seq(strng, sep, pos):
    strng = strng.split(sep)
    return sep.join(strng[:pos]), sep.join(strng[pos:])

# Function to replace text in a given string based on a dictionary
def replace_text(input_text, replacement_dict):
    for key, value in replacement_dict.items():
        input_text = input_text.replace(key, value)
    return input_text

# Function to process DataFrame
def process_dataframe(df, replacement_dict):
    # Apply split_on_seq function to the first column and create new "Chr" and "Start" columns
    df[['Chr', 'Start']] = df['RIL_Start'].apply(lambda x: pd.Series(split_on_seq(x, '_', 2)))

    # Apply replace_text function to the "Chr" colum
    df['Chr'] = df['Chr'].apply(lambda x: replace_text(x, replacement_dict))

    # Drop the original column
    df.drop('RIL_Start', axis=1, inplace=True)

    # Create a new column "Chr_Start"
    df["Chr_Start"] = df["Chr"].astype(str) + '_' + df["Start"].astype(str)

# Read in data
A123_df = pd.read_csv("../data_from_lit/creating_parental_tables/A123-0_mPing.csv")
EG4_df = pd.read_csv("../data_from_lit/creating_parental_tables/EG4-1_mPing.csv")

# Read in file that has replacement text
replace_file = "../annotation_data/chrom_nums.csv"
replace_df = pd.read_csv(replace_file)
replace_df['chr'] = 'Chr' + replace_df['chr'].astype(str)
replacement_dict = dict(zip(replace_df['acc'], replace_df['chr']))

# Process DataFrames
process_dataframe(A123_df, replacement_dict)
process_dataframe(EG4_df, replacement_dict)

# Create subsets with only "Chr_Start" column
A123_subset = A123_df[["Chr_Start"]].copy()
EG4_subset = EG4_df[["Chr_Start"]].copy()

# Add column with line information
A123_subset["line"] = "A123"
EG4_subset["line"] = "EG4"

# Print subsets
print(A123_subset)
print(EG4_subset)


# Concatenate the DataFrames
concatenated_df = pd.concat([A123_subset, EG4_subset])

# Reset the index if needed
concatenated_df.reset_index(drop=True, inplace=True)

A123_subset.to_csv("../data_from_lit/A123_relocate_results.tsv", sep = '\t', index=False)
EG4_subset.to_csv("../data_from_lit/EG4_relocate_results.tsv", sep = '\t', index=False)
concatenated_df.to_csv("../data_from_lit/all_parental_relocate_results.tsv", sep = '\t', index=False)



