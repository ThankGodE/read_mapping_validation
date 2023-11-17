#!/bin/bash

#********************************************************************
#
# process_bam_files.sh
# ${PROJECT_ROOT_REPOSITORY}/mapping_validation_bash/process_bam_files.sh
#
# PURPOSE
# ^^^^^^
#
# Script to process bam files
#
#
#
# $Source: ${PROJECT_ROOT_REPOSITORY}/mapping_validation_bash/process_bam_files.sh
#*********************************************************************
# this is a strict mode for shell. it ensures that all commands exits with 0 and that all variables are set
set -e
set -u
#set -x for debugging


########################################################################################################################
# Help                                                                                                                 #
########################################################################################################################
Help() {

# Display Help
echo -e "Script to process bam files
Syntax: $0 [-o|-i|-p|-s|-c|-h]
options
    -o    path to output directory
    -i    path to bed files
    -a    path to bam files
    -d    absolute directory path to the Python script to process banm files: process_bam_files.py .
          Default: ${ABSOLUTE_PATH_TO_PYTHON_PREDICT_CANCER_TYPES_SCRIPT};
    -f    force remove existing output files previously created. e.g. true or false. Default=false
    -h    Display Help";

}


########################################################################################################################
########################################################################################################################
# Main program                                                                                                         #
########################################################################################################################
########################################################################################################################
# Process the input options. Add the options as needed                                                                 #
########################################################################################################################

# Get the options
_get_bash_script_directory() {

  ABS_DIR_PATH_CURRENT_RUNNING_SCRIPT="$(dirname "$(realpath "$0")")";
  PARENT_DIR_ALL_SCRIPTS="$(dirname "$ABS_DIR_PATH_CURRENT_RUNNING_SCRIPT")";

  echo "$PARENT_DIR_ALL_SCRIPTS";

}
project_root_directory="$(dirname "$(_get_bash_script_directory)")";


PATH_TO_BED_FILES="";
PATH_TO_OUTPUT_DIRECTORY="";
PATH_TO_BAM_FILES="";
REMOVE_PATH="false";
ABSOLUTE_PATH_TO_PROCESS_BAM_FILES_PYTHON_SCRIPT="$project_root_directory""/mapping_validation_python/src/main/process_bam_files.py";


while getopts i:o:d:a:f:h flag # the colon after any alphabet shows that an input argument is required.
do
    case "${flag}" in

    i) PATH_TO_BED_FILES=${OPTARG};;
    o) PATH_TO_OUTPUT_DIRECTORY=${OPTARG};;
    d) ABSOLUTE_PATH_TO_PROCESS_BAM_FILES_PYTHON_SCRIPT=${OPTARG};;
    a) PATH_TO_BAM_FILES=${OPTARG};;
    f) REMOVE_PATH="true";;
    h) Help
        exit;; # display Help
    \?) echo "Error: Invalid option  -${OPTARG}";
    exit;; # incorrect option

    esac
done
