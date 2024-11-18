import re
import os

def create_journal_file(title, content, index, description, output_dir='_posts'):
    # Extract the core title (everything after the dash)
    core_title = title.split('-')[-1].strip() if '-' in title else title
    
    # Clean the core title
    clean_title = core_title.lower().replace(' ', '-')
    clean_title = re.sub(r'[^a-z0-9-]', '', clean_title)
    
    # Format the index with leading zero
    formatted_index = f"{index:02d}"
    
    # Create filename with date and index
    filename = f"2024-01-{formatted_index}-{clean_title}.md"
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Create the full file path
    filepath = os.path.join(output_dir, filename)
    
    # Create file content with Jekyll front matter
    file_content = f"""---
layout: post
title: "{title}"
excerpt: "{description}"
---

{content}
"""
    
    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_content)

def split_journals(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content by journal entries (## headers)
    journals = re.split(r'(?=## Journal|## Jurnal)', content)
    
    # Process each journal entry
    for index, journal in enumerate(journals, 1):
        if journal.strip() and ('Journal' in journal or 'Jurnal' in journal):
            # Extract title and content
            title_match = re.match(r'##\s+(.*?)\n', journal)
            if title_match:
                title = title_match.group(1).strip()
                # Look for description
                desc_match = re.search(r'\[desc:\s*(.*?)\]', journal)
                description = desc_match.group(1).strip() if desc_match else "No description available"
                # Remove the description from the content
                content = re.sub(r'\[desc:\s*(.*?)\]\n?', '', journal[len(title_match.group(0)):])
                create_journal_file(title, content, index, description)

# Run the script
split_journals('the_lost_memories.md')
