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

## 2. replace the path ```env.PROJECT_CODE_BASE_SRC_DIR``` in NextFlow config file with the absolute path ```(i.e. the output of pwd)``` of pwd from above

```
vim mapping_validation_nextflow/process_bam_file.config
```

If the absolute path for the input and output directories changes, please edit the process_bam_file.config file accordingly to reflect these new paths. 

## 3. then run NextFlow 

## Run the Python script and Bash Script using NextFlow (PREFERRED METHOD). Entry point of the pipeline:

### Example

```
nextflow run mapping_validation_nextflow/process_bam_file.nf -c mapping_validation_nextflow/process_bam_file.config -with-singularity
```

## 4. Run test cases

### run test cases for the Python script

```
source mapping_validation_python/venv/bin/activate

cd mapping_validation_python/test/
```

### Examples unit test for each method in Python script

```
pytest -s -vv -k "test_" -q test_functions/test_process_bam_files.py::TestBamOperator::test_process_bam_files

pytest -s -vv -k "test_" -q test_functions/test_process_bam_files.py::test_get_second_element
```


### Example integration tests for the whole Python application

```
pytest -s -vv -k "test_" -q test_functions/test_process_bam_files.py
```
