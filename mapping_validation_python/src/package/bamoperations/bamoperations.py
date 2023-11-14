"""
A collection of classes or functions that performs bam processing operations
"""
import sys

import pysam

# import pysam

from package.datastructureoperations.listoperations.listhandlers import (get_first_element, get_second_element,
                                                                         get_third_element)
from package.enums.delimiter_enums import Delimiters
from package.fileoperations.filehandlers import read_csv


class BamOperator:
    """Performs bam processing operations"""

    bam_files_directory = None
    bed_file = None
    output_directory = None

    def __init__(self, bam_files: list, bed_file: str,
                 output_directory: str) -> None:
        """
        Constructor

        Parameters
        ----------
        bam_files :list
           Path to bam files

        bed_file:str
           Path to bwa meth bam file
        output_directory:str
           Path to output directory
        """

        self.bam_files = bam_files
        self.bed_file = bed_file
        self.output_directory = output_directory

    def process_bam_files(self) -> None:
        """process bam files """

        bed_file_content: list[str] = read_csv(self.bed_file, delimiter=Delimiters.TAB_SEPERATOR,)

        for bam_file in self.bam_files:
            BamOperator.__process_bam_file(bam_file, bed_file_content)

    @classmethod
    def __process_bam_file(cls, bam_file: str, bed_file_content: list[str]) -> dict:
        """ process each bam file """

        with pysam.AlignmentFile(bam_file, "rb") as bam_file_content:

            read_interval_counts = {}

            for line in bed_file_content:
                chromosome, start, end = get_first_element(line), get_second_element(line), get_third_element(line)
                start, end = int(start), int(end)

                reads: list = []

                for read in bam_file_content:

                    if read.is_mapped:

                        if read.reference_name == chromosome and read.reference_start >= start and \
                                read.reference_end <= end:
                            reads.append(read)
                            print(len(read.query_sequence), read.query_alignment_length,
                                  len(read.get_reference_sequence()))

                read_interval_counts[(chromosome, start, end)] = len(reads)

                sys.exit()



