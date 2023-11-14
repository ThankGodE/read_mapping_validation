"""
A collection of classes or functions that performs bam processing operations
"""
import pysam

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

        bed_file_content: list[str] = read_csv(self.bed_file, delimiter="\t",)

        for bam_file in self.bam_files:
            BamOperator.__process_bam_file(bam_file, bed_file_content)


    @classmethod
    def __process_bam_file(cls, bam_file: str, bed_file_content: list[str]) -> dict():
        """ process each bam file """

        bam_file_content: object() = pysam.AlignmentFile(bam_file, "rb")

        read_counts = {}

        for line in bed_file_content:
            