// main.nf
include { GTFINSERT } from '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/sortInsert/gffInsert/nextflow/gtfinsert.nf'


// params.combined_gtf =
// params.tracking_file = 
// params.reference_gtf = 
// params.overlapClassCodes = ['k', 'm', 'n', 'j', 'e']
// params.novelClassCodes = ['r', 'u', 'i', 'y', 'p']

workflow {
    // Define input channels
    combined_gtf_ch = Channel.fromPath('/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/null.combined.gtf')
    tracking_file_ch = Channel.fromPath('/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/null.tracking')
    reference_gtf_ch = Channel.fromPath('/Users/dxu/Documents/axolotlOmics/AmexT_v47-AmexG_v6.0-DD.gtf')

    // Call the GTFINSERT subworkflow
    GTFINSERT(
        combined_gtf_ch.map { [ [:], it ] },
        tracking_file_ch.map { [ [:], it ] },
        reference_gtf_ch.map { [ [:], it ] }
    )

    // Collect and emit the final output if needed
    final_output = GTFINSERT.out.final_gtf
    //final_output.view { "Final GTF file: ${it}" }
}

