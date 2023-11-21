## Summarizing RelocaTE2 Results

**Directories:**
- `annotation_data`: Contains genomic features (`annotation_data/chrom_nums.csv` is used to change chrom names).
- `data_from_lit`: Holds parental insertion information.
- `relocate_summary_results`: RelocaTE2 results for each RIL (files were renamed).
- `scripts`: Includes a series of scripts used to transform RelocaTE2 input.

## Scripts

### `scripts/make_concat_table.py`

- Reads in all RIL RelocaTE2 results and creates one long table with selected columns.
- Chromosome names are changed, and a `Chr_Start` column is created (joining the `Chr` and `Start` columns).
  - This column contains all possible insertion sites in the sequenced RILs.

### `scripts/00_modify_parental_data.py`

- Modifies parental Ping and Pong data.
  - Reads in `parental_pings.csv` and `parental_pongs.csv`, subsets columns, and creats `Chrom_Start` column
- Outputs new file (ex. `parent_ping_loc.tsv`), and this will be used when finding Ping locations in RIL populations.


### `scripts/03_make_summary_table.py`

- A goal is to create a summary file that has all possible locations (`Chrom_Start`), origin of insertion (de novo or which parent it came from),
  type of insertion, and a presence/abscence table (1/0 for P/A).
- Reads in processed data from scripts above, makes dictionaries (`lines : locations`), and compares locations between lines
