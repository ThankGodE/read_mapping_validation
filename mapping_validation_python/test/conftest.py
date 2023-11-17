# content of conftest.py
""" commandline options are for script: test_process_bam_files.py

Required:
    - Pytest >= 7.0.1

"""


def pytest_addoption(parser):
    """appends commandline argument to pytest.
    Help == stringinputs to pass to test functions."""

    parser.addoption(
        "--path2out",
        action="store",
        default="test_data/output/",
        help="""absolute path to processed output files""",
    )
    parser.addoption(
        "--path2bed",
        action="store",
        default="test_data/input/",
        help="absolute directory path to bed files ",
    )
    parser.addoption(
        "--path2bam",
        action="store",
        default="test_data/input/",
        help="absolute directory path to bam files ",
    )
    parser.addoption(
        "--bam_extension",
        action="store",
        default="bam",
        help="bam file extension",
    )
    parser.addoption(
        "--bed_extension",
        action="store",
        default="bed",
        help="bed file extension",
    )