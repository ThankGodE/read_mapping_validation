# Read mapping counts and fasta extraction

This script does the following:
1. performs read counts for the regions specified in an input BED file and outputs it in JSON format.
2. extract reads in the regions and convert it into a FASTA file

Required:
- Python >= 3.10
- python-dotenv>=1.0.0
- for additional dependencies, see requirements.txt

# Usage

## 1. Set up the environment

```
git clone https://github.com/ThankGodE/read_mapping_validation.git
cd read_mapping_validation
```

## 2. then run any of the commands below. NextFlow is preferred


## 3. Run the Python script and Bash Script using NextFlow (PREFERRED)


```
nextflow run process_bam_file.nf -c process_bam_file.config
```

### Example

```
nextflow run mapping_validation_nextflow/process_bam_file.nf -c mapping_validation_nextflow/process_bam_file.config 
```


## 4. Run the Python script using Bash (OPTIONAL)

```
mapping_validation_bash/process_bam_files.sh -h
```

### Example

```
mapping_validation_bash/process_bam_files.sh \
    -o example_data/output/ -i example_data/input/ -a example_data/input/ 
```

## 5. Run the Python script directly (OPTIONAL)

```
source mapping_validation_python/venv/bin/activate

python3 mapping_validation_python/src/main/process_bam_files.py --help

deactivate
```

### Example

```
source mapping_validation_python/venv/bin/activate

python3 read_mapping_validation.py \
    -o example_data/output/ -i example_data/input/ -a example_data/input/

deactivate
```


## Run test cases

```
source mapping_validation_python/venv/bin/activate

cd mapping_validation_python/test/test_functions/
```

### Example unit test per for each method

```
pytest -s -k "test_" -q test_process_bam_files.py::TestBamOperator::test_process_bam_files
```


### Example integration tests for the whole application

```
pytest -s -k "test_" -q test_process_bam_files.py
```