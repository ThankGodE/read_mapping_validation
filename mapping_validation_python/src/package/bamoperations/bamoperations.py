"""
A collection of classes or functions that performs bam processing operations
"""

import os.path
import pysam

from package.datastructureoperations.listoperations.listhandlers import (get_first_element, get_second_element,
                                                                         get_third_element)
from package.enums.delimiter_enums import Delimiters
from package.fileoperations.filehandlers import read_csv
from package.fileoperations.filewriters import FileWriter


class BamOperator:
    """Performs bam processing operations"""

    bam_files_directory = None
    bed_file = None
    output_directory = None

    def __init__(self, bam_files: list, bed_file: str, output_directory: str) -> None:
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

        bed_file_content: list[str] = read_csv(self.bed_file, delimiter=Delimiters.TAB_SEPERATOR)

        for count, bam_file in enumerate(self.bam_files):

            output_read_counts_sequences: tuple = BamOperator.__process_bam_file(bam_file, bed_file_content)

            output_read_counts: dict = get_first_element(output_read_counts_sequences)

            fasta_sequences: str = BamOperator.__generate_fasta(get_second_element(output_read_counts_sequences))

            BamOperator.__write_to_out(output_read_counts, fasta_sequences,
                                       BamOperator.__prepare_json_filenames(count, self.output_directory),
                                       BamOperator.__prepare_fasta_filenames(count, self.output_directory))

    @classmethod
    def __prepare_json_filenames(cls, count: int, output_directory) -> str:
        """ prepare json filenames """

        __file_basename_json: str = str(count).join(["read_counts", ".json"])

        json_output_file: str = os.path.join(output_directory, __file_basename_json)

        return json_output_file

    @classmethod
    def __prepare_fasta_filenames(cls, count: int, output_directory) -> str:
        """ prepare fasta filenames """

        __file_basename_fasta: str = str(count).join(["fasta_sequence", ".fasta"])

        fasta_output_file: str = os.path.join(output_directory, __file_basename_fasta)

        return fasta_output_file

    @classmethod
    def __write_to_out(cls, output_read_counts: dict, fasta_sequences: str,
                       json_output_file: str, fasta_output_file: str) -> None:
        """Writes the output to the output file. """

        file_writer_json: FileWriter = FileWriter(json_output_file, "w")

        file_writer_json.write_json(output_read_counts)

        file_writer_fasta: FileWriter = FileWriter(fasta_output_file, "w")

        file_writer_fasta.write_str(fasta_sequences)

    @classmethod
    def __generate_fasta(cls, read_ids_sequences: list) -> str:
        """ Generate fasta file from read_ids_sequences """

        fasta_sequences: list = [
            Delimiters.FASTA_IDENTIFIER + Delimiters.NEW_LINER.join([read_query_id, read_sequence])
            for element in read_ids_sequences
            for read_query_id, read_sequence in
            element.items()
        ]

        return Delimiters.NEW_LINER.join(fasta_sequences)

    @classmethod
    def __process_bam_file(cls, bam_file: str, bed_file_content: list[str]) -> tuple:
        """ process each bam file """

        with pysam.AlignmentFile(bam_file, "rb") as bam_file_content:
            return BamOperator.__process_bed_file_content(bed_file_content, bam_file_content)

    @classmethod
    def __process_bed_file_content(cls, bed_file_content: list, bam_file_content: object()) -> tuple:
        """ process bed file content """

        read_interval_counts = {}
        read_sequences = []

        for line in bed_file_content:
            chromosome, start, end = get_first_element(line), get_second_element(line), get_third_element(line)
            start, end = int(start), int(end)

            read_names_sequence_pairs: dict = BamOperator.__process_bed_line(line, bam_file_content)

            read_counts_key: str = Delimiters.HYPHEN.join([chromosome, str(start), str(end)])

            read_interval_counts[read_counts_key] = len(list(read_names_sequence_pairs.keys()))

            read_sequences.append(read_names_sequence_pairs)

        return read_interval_counts, read_sequences

    @classmethod
    def __process_bed_line(cls, line: str, bam_file_content: object()) -> dict:
        """ process bed file """

        chromosome, start, end = get_first_element(line), get_second_element(line), get_third_element(line)
        start, end = int(start), int(end)

        reads: dict = {}

        for read in bam_file_content:

            if read.is_mapped and read.reference_name == chromosome:
                if BamOperator.__is_interval(read, start, end):
                    reads[read.query_name] = read.query_sequence

        return reads

    @classmethod
    def __is_interval(cls, read: object(), bed_start: int, bed_end: int) -> bool:
        """ check if read is within interval """

        return read.reference_start >= bed_start and read.reference_end <= bed_end


