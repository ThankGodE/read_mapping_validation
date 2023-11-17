""" test to test the methods and classes used by annotation_evaluations.py script

how to run in commandline (USAGE) - all commandline options are in conftest.py. Just run the below command:

source read_mapping_validation/mapping_validation_python/venv/bin/activate
pytest -s -k "test_" -q test_process_bam_files.py

or

source read_mapping_validation/mapping_validation_python/venv/bin/activate
pytest -s -vv test_process_bam_files.py

"""

import pytest

# Futures local application libraries, source package
from .addscriptdir2path import add_package2env_var


# re-define system path to include modules, packages,
# and libraries in environment variable

add_package2env_var()


# ThankGod's packages ###
from fileoperations.filehandlers import globally_get_all_files
