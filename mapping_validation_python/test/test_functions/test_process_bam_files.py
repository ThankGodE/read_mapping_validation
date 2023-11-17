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
import sys

import pytest

# Futures local application libraries, source package
from addscriptdir2path import add_package2env_var

# re-define system path to include modules, packages,
# and libraries in environment variable
add_package2env_var()

from package.bamoperations.bamoperations import BamOperator
from package.datastructureoperations.listoperations.listhandlers import get_first_element
from package.fileoperations.filehandlers import globally_get_all_files


# ThankGod's packages ###

#################################################################################
# get base directory of run script ##############################################
#################################################################################

dir_basename_of_run_script = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(pytestconfig.getoption("path2out"))
sys.exit()


#################################################################################
# pytest config options #########################################################
#################################################################################

@pytest.fixture()
def test_path2out(pytestconfig):
    """path2out  pytest config options """
    logging.info("path to out set to: ", pytestconfig.getoption("path2out"))
    return os.path.join(dir_basename_of_run_script, pytestconfig.option.path2out)


@pytest.fixture()
def test_path2bed(pytestconfig):
    """ absolute directory path to bed files pytest config options"""
    logging.info("path to bed set to: ", pytestconfig.getoption("path2bed"))
    return os.path.join(dir_basename_of_run_script, pytestconfig.option.path2bed)


@pytest.fixture()
def test_path2bam(pytestconfig) -> str:
    """ path to bam files pytest config options"""
    logging.info("path to bam set to: ", pytestconfig.getoption("path2bam"))
    return os.path.join(dir_basename_of_run_script, pytestconfig.option.path2bam)


@pytest.fixture()
def test_bam_extension(pytestconfig) -> str:
    """bam_extension pytest config options"""
    logging.info("bam extension set to: ", pytestconfig.getoption("bam_extension"))
    return os.path.join(dir_basename_of_run_script, pytestconfig.option.bam_extension)


@pytest.fixture()
def test_bed_extension(pytestconfig) -> str:
    """bed_extension pytest config options"""
    logging.info("bed extension set to: ", pytestconfig.getoption("bed_extension"))
    return pytestconfig.option.bed_extension


#################################################################################
# run unit tests: functions #####################################################
#################################################################################


class TestBamOperator:
    """ test the method process_bam_files in class BamOperator """

    def test_process_bam_files(self, test_path2out: str, test_path2bed: str, test_path2bam: str,
                               test_bam_extension: str, test_bed_extension: str, capsys: str) -> None:
        """ test the method process_bam_files """

        all_bam_files: list = globally_get_all_files(test_path2bam, test_bam_extension)
        bed_file: str = get_first_element(globally_get_all_files(test_path2bed, test_bed_extension))

        bam_operator: BamOperator = BamOperator(all_bam_files, bed_file, test_path2out)

        bam_operator.process_bam_files()

        out, err = capsys.readouterr()

        assert err == ""
        assert out == ""




