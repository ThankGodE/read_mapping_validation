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
    -d    absolute directory path to the Python script to process bam files: process_bam_files.py .
          Default: ${ABSOLUTE_PATH_TO_PROCESS_BAM_FILES_PYTHON_SCRIPT};
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
project_root_directory="$(_get_bash_script_directory)";

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


_check_mandatory_cli_arguments() {

  echo -e "checking mandatory commandline arguments...\n"

  if [ ! -d "${PATH_TO_OUTPUT_DIRECTORY}" ] || [ ! -d "${PATH_TO_BED_FILES}" ] || [ ! -f "${PATH_TO_BAM_FILES}" ] ||
        [ ! -f "${ABSOLUTE_PATH_TO_PROCESS_BAM_FILES_PYTHON_SCRIPT}" ] ; then
         echo -e "\nERROR: Options supplied to -o, -i and -d must be directories that exists,
                  while -d must be python file that exists \n" >&2;
         Help
         exit 1
  fi

}

_remove_existing_matrix_files() {

  echo -e "removing existing files...\n";

  ALL_FORMER_BED_FILES="$(find "$PATH_TO_OUTPUT_DIRECTORY" -type f -name "*.bed" | wc -l)";
  ALL_FORMER_BAM_FILES="$(find "$PATH_TO_OUTPUT_DIRECTORY" -type f -name "*.bam" | wc -l)";

  if [ $REMOVE_PATH == "true" ] && [ -f "${ALL_FORMER_BED_FILES}" ]; then

    rm "$ALL_FORMER_BED_FILES";

  fi

  if [ $REMOVE_PATH == "true" ] && [ -f "${ALL_FORMER_BAM_FILES}" ]; then

    rm "$ALL_FORMER_BAM_FILES";

  fi
}

_process_bam_files() {


  echo -e "processing bam files...\n";

  REQUIREMENTS_FILE="$project_root_directory/mapping_validation_python/requirements.txt"

   python3 -m venv venv && \
   . venv/bin/activate && \
   pip install --upgrade pip && \
   pip install -r $REQUIREMENTS_FILE

  echo "venv/bin/python3 $ABSOLUTE_PATH_TO_PROCESS_BAM_FILES_PYTHON_SCRIPT -o $PATH_TO_OUTPUT_DIRECTORY -i $PATH_TO_BED_FILES \
    -a $PATH_TO_BAM_FILES"

  venv/bin/python3 "${ABSOLUTE_PATH_TO_PROCESS_BAM_FILES_PYTHON_SCRIPT}" -o "${PATH_TO_OUTPUT_DIRECTORY}" -i "${PATH_TO_BED_FILES}" \
  -a "${PATH_TO_BAM_FILES}"


  deactivate

}

_main() {

echo -e "
path to output directory: $PATH_TO_OUTPUT_DIRECTORY
path to bed files: $PATH_TO_BED_FILES
path to bam files: $PATH_TO_BAM_FILES
absolute directory path to the Python script: $ABSOLUTE_PATH_TO_PROCESS_BAM_FILES_PYTHON_SCRIPT
force remove existing output files previously created: $REMOVE_PATH

"

_remove_existing_matrix_files;
_process_bam_files;

}

_main;