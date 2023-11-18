""" test to test the methods and classes used by annotation_evaluations.py script

how to run in commandline (USAGE) - all commandline options are in conftest.py. Just run the below command:

source read_mapping_validation/mapping_validation_python/venv/bin/activate
pytest -s -k "test_" -q test_process_bam_files.py

or

source read_mapping_validation/mapping_validation_python/venv/bin/activate
pytest -s -vv test_process_bam_files.py

"""
import filecmp
import logging
import os
import sys

import pytest

# Futures local application libraries, source package
from .addscriptdir2path import add_package2env_var

# re-define system path to include modules, packages,
# and libraries in environment variable
add_package2env_var()

from package.bamoperations.bamoperations import BamOperator
from package.enums.delimiter_enums import Delimiters
from package.fileoperations.filewriters import FileWriter
from package.datastructureoperations.listoperations.listhandlers import (get_first_element, get_second_element,
                                                                         get_third_element)
from package.fileoperations.filehandlers import globally_get_all_files, read_csv

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


class TestDelimiters:
    """ test the delimiters enums """

    def test_delimiters(self):
        """test the variables or attributes in the delimiters enums"""

        expected_tab = "\t"
        expected_hyphen = "-"
        expected_fasta_identifier = ">"
        expected_new_liner = "\n"

        actual_tab = Delimiters.TAB_SEPERATOR
        actual_hyphen = Delimiters.HYPHEN
        actual_fasta_identifier = Delimiters.FASTA_IDENTIFIER
        actual_new_liner = Delimiters.NEW_LINER

        assert actual_tab == expected_tab
        assert actual_hyphen == expected_hyphen
        assert actual_fasta_identifier == expected_fasta_identifier
        assert actual_new_liner == expected_new_liner

        assert actual_tab != expected_hyphen
        assert actual_hyphen != expected_fasta_identifier
        assert actual_new_liner != expected_fasta_identifier


class TestFileWriter:
    """test the file writer methods and compare output contents"""

    def test_write_json_positive(self):
        """ test the JSON file writing method for positive tests"""

        expected = os.path.join(dir_basename_of_run_script, "test_data/output/read_counts0.json")

        path_to_json_out = os.path.join(dir_basename_of_run_script, "test_data/output/write_test_actual.json")
        data = {"chrM-5000-6500": 2174}

        file_writer = FileWriter(path_to_json_out, "w")
        file_writer.write_json(data)

        comparative_result = filecmp.cmp(expected, path_to_json_out, shallow=False)

        assert comparative_result is True

    def test_write_json_negative(self):
        """ test the JSON file writing method for negative tests"""

        expected = os.path.join(dir_basename_of_run_script, "test_data/output/read_counts0.json")

        path_to_json_out = os.path.join(dir_basename_of_run_script, "test_data/output/write_test_actual.json")
        data = {"chrM-5000-7500": 2174}

        file_writer = FileWriter(path_to_json_out, "w")
        file_writer.write_json(data)

        comparative_result = filecmp.cmp(expected, path_to_json_out, shallow=False)

        assert comparative_result is False

    def test_write_fasta_positive(self):
        """ test the fasta file writing method for positive tests"""

        expected = os.path.join(dir_basename_of_run_script, "test_data/output/write_test_expected.fasta")

        path_to_fasta_out = os.path.join(dir_basename_of_run_script, "test_data/output/write_test_actual.fasta")

        with open(expected, "r") as file:

            all_fasta_file_content = [line.strip() for line in file.readlines()]

        all_fasta_file_content_data = Delimiters.NEW_LINER.join(all_fasta_file_content)

        file_writer = FileWriter(path_to_fasta_out, "w")
        file_writer.write_str(all_fasta_file_content_data)

        comparative_result = filecmp.cmp(expected, path_to_fasta_out, shallow=False)

        assert comparative_result is True

    def test_write_fasta_negative(self):
        """ test the fasta file writing method for negative tests"""

        expected = os.path.join(dir_basename_of_run_script, "test_data/output/write_test_expected.fasta")

        path_to_fasta_out = os.path.join(dir_basename_of_run_script, "test_data/output/write_test_actual.fasta")

        data = ">header\nASDAASDF"

        file_writer = FileWriter(path_to_fasta_out, "w")
        file_writer.write_str(data)

        comparative_result = filecmp.cmp(expected, path_to_fasta_out, shallow=False)

        assert comparative_result is False

def test_read_csv(test_path2bed: str, test_bed_extension: str, capsys: str) -> None:
    """ test the read csv function """

    bed_file = get_first_element(globally_get_all_files(test_path2bed, test_bed_extension))
    bed_file_content = read_csv(bed_file, Delimiters.TAB_SEPERATOR)

    out, err = capsys.readouterr()

    first_bed_row = bed_file_content[0]

    assert err == ""
    assert out == ""

    assert len(first_bed_row) > 0
    assert first_bed_row[0] == "chrM"
    assert first_bed_row[1] == "5000"
    assert first_bed_row[2] == "6500"

    assert first_bed_row[0] != "chrA"
    assert first_bed_row[1] != "5001"
    assert first_bed_row[2] != "6400"


def test_globally_get_all_files(test_path2bed: str, test_bed_extension: str) -> None:
    """ test the globally_get_all_files function in file handlers """

    expected = os.path.join(dir_basename_of_run_script, "test_data/input/regions.bed")

    actual = globally_get_all_files(test_path2bed, test_bed_extension)

    assert len(actual) > 0
    assert expected in actual
    assert get_first_element(actual) == expected


def test_get_first_element() -> None:
    "Test get_first_element in module listhandlers.py"

    contents = ["A", "B", "C"]

    expected = "A"

    actual = get_first_element(contents)

    assert actual == expected
    assert actual != "B"
    assert actual != "C"


def test_get_second_element() -> None:
    "Test get_second_element in module listhandlers.py"

    contents = ["A", "B", "C"]

    expected = "B"

    actual = get_second_element(contents)

    assert actual == expected
    assert actual != "A"
    assert actual != "C"


def test_get_third_element() -> None:
    "Test get_third_element in module listhandlers.py"

    contents = ["A", "B", "C"]

    expected = "C"

    actual = get_third_element(contents)

    assert actual == expected
    assert actual != "A"
    assert actual != "B"







