"""
A collection of classes or functions that evaluates proteins from nodes using keyword,
pathway comments, function comments, and catalytic activity comments
"""

__name__ = "__main__"

import argparse
import os

import pysam as pysam

from package.fileoperations.filehandlers import globally_get_all_files, read_csv


class CliInputArgumentGetter:
    """Wrapper for argparse that returns an object of the class for ease of use"""

    @classmethod
    def get_cli_input_arguments(cls, args=None) -> argparse.Namespace:
        """gets input arguments from the commandline interface """

        parser = argparse.ArgumentParser(prog="process_bam_files.py", usage="""process_bam_files.py -h""",
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter, description=("""
                    This script:
                        1. performs read counts for the regions specified in an input BED file 
                            and outputs it in JSON format.
                        2. extract reads in the regions and convert it into a FASTA file
                    
                    Required:
                        - Python >= 3.10
                        - python-dotenv>=1.0.0
                        - for additional dependencies, see requirements.txt

                """), )
        parser.add_argument("-o", "--path2out", help="absolute directory path to processed output files ",
                            required=True, )
        parser.add_argument("-i", "--path2bed", help="absolute directory path to bed files ", required=True, )
        parser.add_argument("-a", "--path2bam", help="absolute directory path to bam files ", required=True, )
        parser.add_argument("-e", "--bam_extension", help="bam file extension", default="bam")
        parser.add_argument("-b", "--bed_extension", help="bed file extension", default="bed")

        return parser.parse_args(args)

    @classmethod
    def check_input_arguments(cls, cli_input_arguments: argparse.Namespace) -> None:
        """ check or verify input arguments """

        if not os.path.exists(cli_input_arguments.path2bam):
            raise FileNotFoundError("bam file director {} does not exist!".format(cli_input_arguments.path2bam))

        if not os.path.exists(cli_input_arguments.path2out):
            raise FileNotFoundError("output directory {} does not exist!".format(cli_input_arguments.path2out))

        if not os.path.exists(cli_input_arguments.path2bed):
            raise FileNotFoundError("genome fasta file {} does not exist!".format(cli_input_arguments.path2beds))

        CliInputArgumentGetter.__check_bam_bed_files(cli_input_arguments)

    @classmethod
    def __check_bam_bed_files(cls, cli_input_arguments: argparse.Namespace) -> None:
        """ check if bam files """

        bam_files: list = globally_get_all_files(cli_input_arguments.path2bam, cli_input_arguments.bam_extension)
        bed_files: list = globally_get_all_files(cli_input_arguments.path2bed, cli_input_arguments.bed_extension)

        if not len(bam_files) or not len(bed_files):
            raise FileNotFoundError(
                "{} and {} does not contain files ending with file extensions {} and/or {} respectively!".format(
                    cli_input_arguments.path2bam, cli_input_arguments.path2bed,
                    cli_input_arguments.bam_extension, cli_input_arguments.bed_extension))

        CliInputArgumentGetter.__iterate_through_bam_bed_files(bam_files, bed_files)

    @classmethod
    def __iterate_through_bam_bed_files(cls, bam_files: list, bed_files: list) -> None:
        """ iterate through bam and bed files to process each bam and bed files individually """

        [CliInputArgumentGetter.__check_bam_file(bam_file, "bam file") for bam_file in bam_files]
        [CliInputArgumentGetter.__check_bed_file(bam_file, "bed file") for bam_file in bed_files]

    @classmethod
    def __check_bam_file(cls, bam_file: str, file_type: str) -> None:
        """ check or verify input arguments """

        if not os.path.exists(bam_file):
            raise FileNotFoundError("{} {} does not exist!".format(file_type, bam_file))

        try:

            pysam.AlignmentFile(bam_file, "rb")

        except ValueError:
            raise ValueError("the bam file {} does not contain any alignment data".format(bam_file))

    @classmethod
    def __check_bed_file(cls, bed_file: str, file_type: str) -> None:
        """ check or verify input arguments """

        if not os.path.exists(bed_file):
            raise FileNotFoundError("{} {} does not exist!".format(file_type, bed_file))

        try:

            read_csv(bed_file, "\t")

        except ValueError:
            raise ValueError("the {} {} does not contain any data".format(file_type, bed_file))