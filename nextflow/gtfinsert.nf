include { FIND_OVERLAP_TRANSCRIPT } from '../nextflow/find_overlap_transcript.nf'
include { PARSE_GTF_TO_DICT } from '../nextflow/parse_gtf_to_dict_by_cmp_ref.nf'
include { EXTRACT_KEY_VALUE } from '../nextflow/extract_key_value_pairs.nf'
include { CHECK_UNIQUE_KEYS } from '../nextflow/check_key_unique.nf'
include { UPDATE_KEYS } from '../nextflow/update_keys_with_tracking_key_value_pair.nf'
include { PARSE_GTF_TO_DICT_BY_GENEID } from '../nextflow/parse_gtf_to_dict_by_geneID.nf'
include { INSERT_BY_START_POSITION } from '../nextflow/insert_by_start_position.nf'
include { JSON_TO_GTF} from '../nextflow/parse_json_gtf.nf'
include { FIND_NOVEL_TRANSCRIPTS } from '../nextflow/find_novel_transcripts.nf'

workflow GTFINSERT {
    take:
    combined_gtf   //channel: [ val(meta), [ path ] ]
    tracking_file  //channel: [ val(meta), [ path ] ]
    reference_gtf //channel: [ val(meta), [ path ] ]

    main:
    // Step 1: Find overlapping transcripts
    FIND_OVERLAP_TRANSCRIPT(combined_gtf)

    // Step 2: Parse GTF to dict by cmp_ref
    PARSE_GTF_TO_DICT (FIND_OVERLAP_TRANSCRIPT.out.select_transcript_insert_based_on_gffcompare_class_code)

    // Step 3: Extract key-value pairs
    EXTRACT_KEY_VALUE(tracking_file)

    // Step 4: (Optional) Check if keys are unique
    CHECK_UNIQUE_KEYS(EXTRACT_KEY_VALUE.out.key_value_json)

    // Step 5: Update keys with tracking key-value pair
    UPDATE_KEYS (EXTRACT_KEY_VALUE.out.key_value_json, PARSE_GTF_TO_DICT.out.parsed_gtf_json_by_cmp_ref)

    // Process Reference GTF
    // Step 6: Parse GTF to dict by gene ID
    PARSE_GTF_TO_DICT_BY_GENEID(reference_gtf)

    // Insertion and Sorting
    // Step 7: Insert by start position
    INSERT_BY_START_POSITION(UPDATE_KEYS.out.update_keys_with_tracking_key_value_pair, PARSE_GTF_TO_DICT_BY_GENEID.out.parsed_gtf_json_by_geneID)

    // Finalization
    // Step 8: Parse JSON GTF
    JSON_TO_GTF(INSERT_BY_START_POSITION.out.final_annotation_json)

    // Handling Novel Transcripts
    // Step 9: Find novel transcripts
    FIND_NOVEL_TRANSCRIPTS(JSON_TO_GTF.out.final_annotation,reference_gtf)

    emit:
    final_gtf = FIND_NOVEL_TRANSCRIPTS.out.final_annotation_gtf  //select_transcript_append_based_on_gffcompare_class_code_to_generate_final_gtf
     
    
    

}
