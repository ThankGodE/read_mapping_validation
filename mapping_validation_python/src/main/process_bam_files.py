"""
This script:
    1. performs read counts for the regions specified in an input BED file and outputs it in JSON format.
    2. extract reads in the regions and convert it into a FASTA file

Required:
    - Python >= 3.10
    - python-dotenv>=1.0.0
    - for additional dependencies, see requirements.txt

"""

# Futures local application libraries, source package
from addscriptdir2path import add_package2env_var

# re-define system path to include modules, packages
# and libraries in environment variable
add_package2env_var()

from package.bamoperations.bamoperations import BamOperator
from package.commandlineoperations.commandline_input_argument_getter import CliInputArgumentGetter
from package.datastructureoperations.listoperations.listhandlers import get_first_element
from package.fileoperations.filehandlers import globally_get_all_files
from package.profiling.profiling import begin_profiling, end_profiling, ProfileLogger


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
    path2bam_files = args_cli_values.path2bam
    path2bed = args_cli_values.path2bed
    bed_file_extension = args_cli_values.bed_extension
    bam_file_extension = args_cli_values.bam_extension

    try:

        all_bam_files: list = globally_get_all_files(path2bam_files, bam_file_extension)
        bed_file: str = get_first_element(globally_get_all_files(path2bed, bed_file_extension))

        bam_operator: BamOperator = BamOperator(all_bam_files, bed_file, path2output_dir)

        bam_operator.process_bam_files()

    except (ValueError, TypeError, FileNotFoundError) as e:

        if isinstance(e, ValueError):
            raise ValueError(e)

        if isinstance(e, TypeError):
            raise TypeError(e)

        if isinstance(e, FileNotFoundError):
            raise FileNotFoundError(e)


###################################################################################
# run __main__ ####################################################################
###################################################################################
if __name__ == "__main__":
    main()

time_end = end_profiling()
ProfileLogger(profiling_starting, time_end).log_profiling()
