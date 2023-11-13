"""
This script:
    1. performs read counts for the regions specified in an input BED file and outputs it in JSON format.
    2. extract reads in the regions and convert it into a FASTA file

Required:
    - Pandas
    - Python >= 3.10
    - python-dotenv>=1.0.0

"""


# Futures local application libraries, source package
from addscriptdir2path import add_package2env_var
from package.commandlineoperations.commandline_input_argument_getter import CliInputArgumentGetter
from package.profiling.profiling import begin_profiling, end_profiling, ProfileLogger

# re-define system path to include modules, packages
# and libraries in environment variable
add_package2env_var()

# profiling begins
profiling_starting = begin_profiling("")


###################################################
# main function                               #####
###################################################


def main() -> None:
    """main function to run commandline arguments and call other functions to run."""

    args_cli_values = CliInputArgumentGetter.get_cli_input_arguments()

    CliInputArgumentGetter.check_input_arguments(args_cli_values)

    path2output_dir = args_cli_values.path2out
    path2bamfile = args_cli_values.path2bam
    path2fasta = args_cli_values.path2fasta
    #
    # path_to_bismark_bam_files = args_cli_values.path2bismark_bam
    # path_to_bwa_bam_files = args_cli_values.path2bwa_meth_bam
    # path_to_genome_fasta = args_cli_values.path2genome
    # alignment_file_extension = args_cli_values.file_extension
    #
    # bam_operator: BamOperator = BamOperator(path_to_bismark_bam_files, path_to_bwa_bam_files, path_to_genome_fasta)
    #
    # bam_operator.process_bam_files(alignment_file_extension)


###################################################################################
# run __main__ ####################################################################
###################################################################################
if __name__ == "__main__":
    main()

time_end = end_profiling()
ProfileLogger(profiling_starting, time_end).log_profiling()
