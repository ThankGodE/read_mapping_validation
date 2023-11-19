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
pwd
```

## 3. replace the path ```env.PROJECT_CODE_BASE_SRC_DIR``` in NextFlow config file with the absolute path ```(i.e. the output of pwd)``` of pwd from above

```
vim mapping_validation_nextflow/process_bam_file.config
```

If the absolute path for the input and output directories changes, please edit the process_bam_file.config file accordingly to reflect these new paths. 

## 2. then run any of the commands below. NextFlow is preferred


## A. Run the Python script and Bash Script using NextFlow (PREFERRED METHOD). Entry point of the pipeline:

### Example

```
nextflow run mapping_validation_nextflow/process_bam_file.nf -c mapping_validation_nextflow/process_bam_file.config -with-singularity
```


## B. Run the Python script using Bash (sub-module - OPTIONAL)

```
mapping_validation_bash/process_bam_files.sh -h
```

### Example

```
mapping_validation_bash/process_bam_files.sh \
    -o example_data/output/ -i example_data/input/ -a example_data/input/ 
```

## C. Run the Python script directly (sub-module - OPTIONAL)

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


## 3. Run test cases

```
source mapping_validation_python/venv/bin/activate

cd mapping_validation_python/test/
```

### Examples unit test per for each method

```
pytest -s -vv -k "test_" -q test_functions/test_process_bam_files.py::TestBamOperator::test_process_bam_files

pytest -s -vv -k "test_" -q test_functions/test_process_bam_files.py::test_get_second_element
```


### Example integration tests for the whole application

```
pytest -s -vv -k "test_" -q test_functions/test_process_bam_files.py
```