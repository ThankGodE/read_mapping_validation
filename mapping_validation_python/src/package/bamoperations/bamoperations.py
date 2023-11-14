"""
A collection of classes or functions that performs bam processing operations
"""


class BamOperator:
    """Performs bam processing operations"""

    bam_files_directory = None
    bed_files_directory = None
    output_directory = None

    def __init__(self, bam_files: list, bed_files: list,
                 output_directory: str) -> None:
        """
        Constructor

        Parameters
        ----------
        bam_files :list
           Path to bam files
        bed_files:list
           Path to bwa meth bam file
        output_directory:str
           Path to output directory
        """

        self.bam_files = bam_files
        self.bed_files = bed_files
        self.output_directory = output_directory

    def process_bam_files(self) -> None:
        """process bam files """

        for bam in self.bam_files:



    @classmethod
    def __process_bam_file(cls, ) -> dict():
        """ process each bam file """

        for line in