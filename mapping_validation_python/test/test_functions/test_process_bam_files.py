""" test to test the methods and classes used by annotation_evaluations.py script

how to run in commandline (USAGE) - all commandline options are in conftest.py. Just run the below command:

source read_mapping_validation/mapping_validation_python/venv/bin/activate
pytest -s -k "test_" -q test_process_bam_files.py

or

source read_mapping_validation/mapping_validation_python/venv/bin/activate
pytest -s -vv test_process_bam_files.py

"""
import logging
import os

import pytest

# Futures local application libraries, source package
from addscriptdir2path import add_package2env_var


# re-define system path to include modules, packages,
# and libraries in environment variable

add_package2env_var()


# ThankGod's packages ###





#################################################################################
# get base directory of run script ##############################################
#################################################################################

dir_basename_of_run_script = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#################################################################################
# pytest config options #########################################################
#################################################################################


@pytest.fixture()
def test_path2out(pytestconfig):
    """path2out  pytest config options """
    logging.info("path2out set to: ", pytestconfig.getoption("path2out"))
    return os.path.join(dir_basename_of_run_script, pytestconfig.option.path2out)


@pytest.fixture()
def test_path2bed(pytestconfig):
    """ absolute directory path to bed files pytest config options"""
    logging.info("path2props_matrix set to: ", pytestconfig.getoption("path2bed"))
    return os.path.join(
        dir_basename_of_run_script, pytestconfig.option.path2bed
    )


@pytest.fixture()
def test_path2bam(pytestconfig) -> str:
    """ path to bam files pytest config options"""
    logging.info("path2bam set to: ", pytestconfig.getoption("path2bam"))
    return os.path.join(
        dir_basename_of_run_script, pytestconfig.option.path2bam
    )


@pytest.fixture()
def test_bam_extension(pytestconfig) -> str:
    """bam_extension pytest config options"""
    logging.info("bam_extension set to: ", pytestconfig.getoption("bam_extension"))
    return os.path.join(dir_basename_of_run_script, pytestconfig.option.bam_extension)


@pytest.fixture()
def test_bed_extension(pytestconfig) -> str:
    """bed_extension pytest config options"""
    logging.info("bed_extension set to: ", pytestconfig.getoption("bed_extension"))
    return pytestconfig.option.bed_extension

#################################################################################
# run unit tests: functions #####################################################
#################################################################################


