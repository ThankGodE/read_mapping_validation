#!/usr/bin/env nextflow

params.output_directory = "$params.path_to_output_directory"
params.absolute_path_project_root_dir = "$params.absolute_path_to_project_root_dir_source"
params.path_to_bed_files = "$params.path_to_bed_files"
params.path_to_bam_files = "$params.path_to_bam_files"

/*
make directory for DMRs split chunk files
*/
process_out = file("$params.output_directory/process_out/")


process PROCESS_BAM_FILES() {

    publishDir params.output_directory, mode:'copy'
    input:
    path output_directory

    output:
    val "process_bam_files_completed"

    script:
    """
    $params.absolute_path_project_root_dir/mapping_validation_python/src/main/process_bam_file.py \
    -o $output_directory -i $params.path_to_bed_files -a $params.path_to_bam_files
    """

}


workflow() {

    process_bam_ch = PROCESS_BAM_FILES(params.output_directory)

}

