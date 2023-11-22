# Read mapping counts and fasta extraction

This script does the following:
1. performs read counts for the regions specified in an input BED file and outputs it in JSON format.
2. extract reads in the regions and convert it into a FASTA file

Required:
- Python >= 3.10
- python-dotenv>=1.0.0
- for additional dependencies, see requirements.txt

# Usage

# RUN PIPELINE

The below step outlines how to run this NextFlow pipeline

## 1. Set up the environment

```
git clone https://github.com/ThankGodE/read_mapping_validation.git
```
```
cd read_mapping_validation
```
```
pwd
```

## 2. edit only one line in the NextFlow ```process_bam_file.config``` file by replacing the path variable string of ```env.PROJECT_CODE_BASE_SRC_DIR``` with the absolute path ```(i.e. the output of pwd)``` of pwd from above

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

# RUN TEST CASES

The below steps outline how to run test cases for the Python script in this pipeline:

### Install NextFlow

See pypi documentation: https://pypi.org/project/nextflow/

```
pip install nextflow
```

### 1. set up testing environment - install Python virtual environment and test dependencies

No need to git clone and ```cd read_mapping_validation``` if you've previously done this and already in ```read_mapping_validation``` directory 
```
git clone https://github.com/ThankGodE/read_mapping_validation.git
```
```
cd read_mapping_validation
```
```
CURRENT_WORKING_DIRECTORY=$(echo $PWD)
```
```
REQUIREMENTS_FILE=$CURRENT_WORKING_DIRECTORY"/mapping_validation_python/requirements.txt" 
```

Install Python virtual environment with one of the below methods:

Does not require sudo privileges
```
python3.10 -m venv --without-pip venv && source venv/bin/activate && curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install -r $REQUIREMENTS_FILE
```

Requires sudo privileges
```
sudo apt install python3.10-venv && \
    python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r $REQUIREMENTS_FILE
```


### 2. run test cases for the Python script

```
source venv/bin/activate
```
```
cd mapping_validation_python/test/
```

### Examples unit test for each method in Python script

```
pytest -s -vv -k "test_" -q test_functions/test_process_bam_files.py::TestBamOperator::test_process_bam_files
```
```
pytest -s -vv -k "test_" -q test_functions/test_process_bam_files.py::test_get_second_element
```


### Example integration tests for the whole Python application

```
pytest -s -vv -k "test_" -q test_functions/test_process_bam_files.py
```

### Deactivate the Python virtual environment when testing is completed
```
deactivate
```