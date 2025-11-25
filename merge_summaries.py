import re

def parse_extracted_summaries(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    entries = []
    # Split by "### FILE:"
    parts = content.split('### FILE:')[1:] # Skip the first empty part
    
    for part in parts:
        lines = part.strip().split('\n')
        filename = lines[0].strip()
        
        # Extract Abstract
        abstract = ""
        conclusion = ""
        
        if '--- ABSTRACT ---' in part:
            abstract_part = part.split('--- ABSTRACT ---')[1]
            if '--- CONCLUSION ---' in abstract_part:
                abstract = abstract_part.split('--- CONCLUSION ---')[0].strip()
            else:
                abstract = abstract_part.strip()
        
        if '--- CONCLUSION ---' in part:
            conclusion = part.split('--- CONCLUSION ---')[1].strip()
            
        entries.append({
            'filename': filename,
            'abstract': abstract,
            'conclusion': conclusion
        })
    return entries

def parse_markdown_consolidated(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by "## [Number]."
    # We use a regex lookahead to keep the delimiter or just split and reconstruct
    # The file starts with a header, then ## 1., ## 2., etc.
    
    header = content.split('## 1. ')[0]
    rest = '## 1. ' + content.split('## 1. ')[1]
    
    # Split by "\n## " to find sections
    sections = re.split(r'\n## (\d+)\. ', rest)
    # sections[0] is empty or the first "## 1. " part if split consumed it?
    # re.split with capturing group returns [pre, group1, post, group2, post...]
    # Since rest starts with "## 1. ", the first split might be empty string if we matched start
    
    # Actually, let's just split by "\n## " and check if it starts with a number
    parts = re.split(r'\n## ', rest)
    
    parsed_sections = []
    # The first part is "1. Title..." (because we constructed rest that way)
    # But wait, rest = "## 1. Title..."
    # split by "\n## " will give: ["## 1. Title..."] if no newlines before it?
    # No, rest starts with "## 1. ".
    # If I split by "\n## ", the first chunk is the whole thing if there are no other "\n## ".
    # But there are.
    
    # Let's use a simpler approach. Iterate line by line.
    lines = content.split('\n')
    output_lines = []
    
    current_section_idx = 0
    
    # We need to match the extracted entries (list) with the markdown sections.
    # We assume they are in order 1 to 52.
    
    return content

def merge_content(md_path, txt_path, output_path):
    extracted = parse_extracted_summaries(txt_path)
    
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    current_article_index = -1
    
    # We need to detect when we are inside an article block to insert the summary/conclusion
    # The structure is:
    # ## N. Title
    # **Referencia:** ...
    # [INSERT HERE]
    # * **Detalles...**
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for new article header
        match = re.match(r'^## (\d+)\. ', line)
        if match:
            current_article_index = int(match.group(1)) - 1 # 0-based index
            new_lines.append(line)
            i += 1
            continue
            
        # Check for Reference line
        if "**Referencia:**" in line and current_article_index >= 0 and current_article_index < len(extracted):
            new_lines.append(line)
            
            # Prepare content to insert
            entry = extracted[current_article_index]
            
            # Clean up abstract/conclusion to be markdown friendly (remove excessive newlines)
            abstract_text = entry['abstract'].replace('\n', ' ').replace('  ', ' ').strip()
            # Truncate if too long? User said "amplies", so keep it but maybe clean it.
            # Let's keep it as a block but clean up weird spacing.
            
            conclusion_text = entry['conclusion'].replace('\n', ' ').replace('  ', ' ').strip()
            
            if abstract_text:
                new_lines.append(f"\n**Resumen:** {abstract_text[:1500]}...\n") # Limit slightly to avoid huge blocks if OCR failed
            else:
                new_lines.append("\n**Resumen:** No disponible en la extracción automática.\n")

            if conclusion_text:
                new_lines.append(f"\n**Conclusión:** {conclusion_text[:1500]}...\n")
            else:
                new_lines.append("\n**Conclusión:** No disponible en la extracción automática.\n")
                
            i += 1
            continue
            
        new_lines.append(line)
        i += 1
        
    # Add the comparison section at the end if not present (or append to it)
    # The user asked to "add at the end which authors can be compared".
    # The current file already has a comparison section. I should enhance it.
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    merge_content(
        '/home/ssg/Documentos/ANH951_H2_storage/h2-storage/02_research/lectura_articulos/Consolidado_Articulos_Completo.md',
        '/home/ssg/Documentos/ANH951_H2_storage/h2-storage/extracted_summaries.txt',
        '/home/ssg/Documentos/ANH951_H2_storage/h2-storage/02_research/lectura_articulos/Consolidado_Final_Completo.md'
    )
