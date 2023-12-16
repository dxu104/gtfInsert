# import os

# def find_overlap_transcript(combined_gtf_path):
#     novel_class_codes = ['k', 'm', 'n', 'j', 'e']
    
#     # Generate output path from the input path by adding a suffix
#     base_name = os.path.basename(combined_gtf_path)
#     directory = os.path.dirname(combined_gtf_path)
#     output_gtf_path = os.path.join(directory, os.path.splitext(base_name)[0] + '_ready_insert_transcript.gtf')

#     with open(combined_gtf_path, 'r') as file:
#         combined_gtf_lines = file.readlines()

#     novel_transcript_lines = []
#     i = 0
#     while i < len(combined_gtf_lines):
#         line = combined_gtf_lines[i]
#         fields = line.strip().split('\t')
        
#         if len(fields) < 9:
#             i += 1
#             continue

#         if fields[2] == "transcript" and 'class_code "' in fields[8]:
#             class_code = fields[8].split('class_code "')[1][0]
#             if class_code in novel_class_codes:
#                 novel_transcript_lines.append(line)
#                 i += 1
#                 while i < len(combined_gtf_lines) and 'exon' in combined_gtf_lines[i].split('\t')[2]:
#                     novel_transcript_lines.append(combined_gtf_lines[i])
#                     i += 1
#                 continue
#         i += 1

#     with open(output_gtf_path, 'w') as output_file:
#         output_file.writelines(novel_transcript_lines)

#     return  output_gtf_path

# # Define the input file path
# combined_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/null.combined.gtf' 

# # Process the file
# output_gtf_path = find_overlap_transcript(combined_gtf_path)


# # Define file paths
 

import os

def find_overlap_transcript(combined_gtf_path, output_gtf_path):
   # novel_class_codes = {'r', 'u', 'i', 'y', 'p'}
    novel_class_codes = {'k', 'm', 'n', 'j', 'e'}
    novel_transcript_lines =0 
    with open(combined_gtf_path, 'r') as file:
        combined_gtf_lines = file.readlines()

    novel_transcript_lines = []
    i = 0
    while i < len(combined_gtf_lines):
        line = combined_gtf_lines[i]
        fields = line.strip().split('\t')
        
        if len(fields) < 9:
            i += 1
            continue

        # Check if it is a new transcript line
        if fields[2] == "transcript" and 'class_code "' in fields[8]:
            class_code = fields[8].split('class_code "')[1][0]

            if class_code in novel_class_codes:
                  # Add the current transcript line
                novel_transcript_lines.append(line)
                i += 1

                 # Add all subsequent exon lines
                while i < len(combined_gtf_lines) and 'exon' in combined_gtf_lines[i].split('\t')[2]:
                    novel_transcript_lines.append(combined_gtf_lines[i])
                    i += 1
                continue

        i += 1

    # Save new(aka potential overlap) transcript lines to a new GTF file
    with open(output_gtf_path, 'w') as output_file:
        output_file.writelines(novel_transcript_lines)

    return len(novel_transcript_lines)

# Define file paths
combined_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/null.combined.gtf'  
output_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/readyInsert.gtf'  

# Process the file
novel_lines_count = find_overlap_transcript(combined_gtf_path, output_gtf_path)
print(f"Processed {novel_lines_count} novel transcript lines. Output saved to {output_gtf_path}")