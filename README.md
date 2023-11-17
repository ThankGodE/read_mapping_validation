# read_mapping_validation

This script:
1. performs read counts for the regions specified in an input BED file and outputs it in JSON format.
2. extract reads in the regions and convert it into a FASTA file

Required:
- Python >= 3.10
- python-dotenv>=1.0.0
- for additional dependencies, see requirements.txt

## Usage

```
python read_mapping_validation.py --help
```

### Example

```
python read_mapping_validation.py \
    -o /path/to/output_directory -i /path/to/bed/ -a /path/to/bam/ 
```