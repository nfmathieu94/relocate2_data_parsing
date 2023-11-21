# Summarizing RelocaTE2 Results

** directories **
'annotation_data' - for genomic features ('annotation_data/chrom_nums.csv' used to change chrom names)
'data_from_lit' - has parental insertion information
'relocate_summary_results' - Relocate2 results for each RIL (files were renamed)
'scripts' - series of scripts used to transform relocate input


## Scripts
'scripts/make_concat_table.py'
- Reads in all RIL relocate2 results and creates one long table with selected columns
- Chromosome names are changed and 'Chr_Start' column is made (join Chr and Start column)
    * This column has all possible insertion sites in the sequenced RILs


