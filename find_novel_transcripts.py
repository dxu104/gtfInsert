def find_novel_transcripts(combined_gtf_path, reference_gtf_path, output_gtf_path):
    # Define the novel transcript class codes
    novel_class_codes = {'j'} 
    # Read the combined GTF file
    with open(combined_gtf_path, 'r') as file:
        combined_gtf_lines = file.readlines()

    # Process the combined GTF lines
    novel_transcript_lines = []
    target_class_code = False
    for line in combined_gtf_lines:
        fields = line.strip().split('\t')
        if len(fields) < 9:
            continue

        # Check for transcript lines with novel class codes
        if fields[2] == "transcript" and 'class_code "' in fields[8]:
            
            class_code = fields[8].split('class_code "')[1][0]
            target_class_code = class_code in novel_class_codes
            # If current transcript is novel, keep the transcript and subsequent exon lines
            if target_class_code:
               novel_transcript_lines.append(line)

        



        elif target_class_code:
            novel_transcript_lines.append(line)      
                
                


    # Read the reference GTF file and append the novel transcript lines
    with open(reference_gtf_path, 'r') as ref_file:
        reference_gtf_lines = ref_file.readlines()

    # Append the novel transcript lines to the new output file
    with open(output_gtf_path, 'w') as output_file:
        output_file.writelines(reference_gtf_lines + novel_transcript_lines)

    return len(novel_transcript_lines)



# Define file paths
combined_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/null.combined.gtf'  
# Path to the combined GTF file
reference_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/AmexT_v47.chr.unscaffolded.CherryGFP.gtf' 
# Path to the reference GTF file
output_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/Class_Code_j.gtf'  # Path to save the updated GTF file

# Process the files
novel_lines_count = find_novel_transcripts(combined_gtf_path, reference_gtf_path, output_gtf_path)
print(f"Number of novel transcript lines processed: {novel_lines_count}")

