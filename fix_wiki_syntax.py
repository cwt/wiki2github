#!/usr/bin/env python3
"""
Script to fix incompatible Wiki syntax in GitHub Wiki files
"""

import re
import os

def convert_wiki_table_to_markdown(table_content):
    """
    Convert wiki table format to markdown table format
    """
    lines = table_content.split('\n')
    result_lines = []
    
    headers = []
    rows = []
    
    # Process table lines to extract headers and rows
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        if line.strip().startswith('{|'):  # Start of table
            i += 1
            continue
        elif line.strip() == '|}':  # End of table
            break
        elif line.strip() == '|-':  # Row separator
            i += 1
            continue
        elif line.lstrip().startswith('!'):  # Header line
            # Handle headers - split by !! or process line by line
            header_line = line.lstrip()[1:]  # Remove leading '!'
            
            # Extract individual headers. In wiki syntax, each ! starts a new cell
            # Look for subsequent ! lines that continue the same header row
            headers = []
            j = i
            while j < len(lines):
                check_line = lines[j].rstrip()
                if check_line.lstrip().startswith('!'):
                    content = check_line.lstrip()[1:]  # Remove leading '!'
                    # Check if this line contains multiple headers separated by !!
                    if '!!' in content:
                        headers.extend([h.strip() for h in content.split('!!')])
                        break  # All headers are on this line
                    else:
                        headers.append(content.strip())
                elif check_line.strip() in ['|-', '|}']:
                    break  # End of header row
                else:
                    # For multiline header content, append to the last header
                    if headers:
                        headers[-1] += " " + check_line.strip()
                j += 1
            i = j
            continue
        elif line.lstrip().startswith('|') and not line.strip() == '|-':  # Data row
            # Process data cells - each | starts a new cell in wiki syntax
            # But we need to handle cells that span multiple lines
            row = []
            j = i
            while j < len(lines):
                check_line = lines[j].rstrip()
                if check_line.strip() == '|-':  # Next row separator
                    break
                elif check_line.strip() == '|}':  # End of table
                    break
                elif check_line.lstrip().startswith('|'):  # Data cell
                    content = check_line.lstrip()[1:]  # Remove leading '|'
                    # Check if this line contains multiple cells separated by ||
                    if '||' in content:
                        cells = [cell.strip() for cell in content.split('||')]
                        row.extend(cells)
                    else:
                        # This is a single cell - either add it or append to last cell if continuing
                        if row:
                            # Check if this is continuation of previous cell
                            # In most cases it's a new cell, but we handle multi-line content too
                            row.append(content.strip())
                        else:
                            row.append(content.strip())
                else:
                    # This line doesn't start with | or !, so it continues the current cell
                    if row:  # Add to last cell
                        row[-1] += " " + check_line.strip()
                    else:  # Unexpected case, add as new cell
                        row.append(check_line.strip())
                
                j += 1
            
            if row:
                rows.append(row)
            i = j
            continue
        else:
            i += 1
    
    # Build the markdown table
    if headers:
        # Create header row
        header_row = '|'
        for header in headers:
            header_row += f" {header} |"
        result_lines.append(header_row)
        
        # Create separator row - make sure we have the right number of separators
        separator_row = '|'
        for _ in headers:
            separator_row += " --- |"
        result_lines.append(separator_row)
    
    # Create data rows
    for row in rows:
        data_row = '|'
        for cell in row:
            data_row += f" {cell} |"
        result_lines.append(data_row)
    
    return '\n'.join(result_lines)


def fix_wiki_syntax(content):
    """
    Fix various incompatible Wiki syntax patterns in the content
    """
    # Fix heading syntax first (e.g., == Heading == becomes ## Heading ##)
    # Match == Heading ==, === Heading ===, etc.
    def replace_heading(match):
        heading_level = len(match.group(1))
        heading_text = match.group(2).strip()
        return '#' * heading_level + ' ' + heading_text
    
    # Handle both == Heading == and === Heading === formats
    content = re.sub(r'(={2,6})\s*(.*?)\s*\1', replace_heading, content)
    
    # Fix template syntax like {{Delete|...}} and {{todo|...}}
    content = re.sub(r'\{\{[^}]+\}\}', lambda m: f"**Note:** {m.group(0)[2:-2].split('|', 1)[-1].strip()}", content)
    
    # Remove standalone templates that don't have content value
    content = re.sub(r'\{\{[^\|}]+\}\}', '', content)
    
    # Fix image links (remove [[Image:...|thumb|...]] syntax)
    content = re.sub(r'\[\[Image:[^\]]+\]\]', '', content)
    content = re.sub(r'\[\[File:[^\]]+\]\]', '', content)
    
    # Define known wiki pages mapping
    known_pages = {
        'User:Bluescreenofdeath/Hints': 'A-list-of-hints.md',
        'User:Bluescreenofdeath/FAQ': 'FAQ.md',
        'User:Bluescreenofdeath/Options_and_Hotkeys': 'Options,-hotkeys-and-commands.md',
        'User:Bluescreenofdeath/Version_history': 'A-rudimentary-version-history.md', 
        'User:Bluescreenofdeath/Skills': 'Skills-in-Slash\'EM-Extended.md',
        'User:Bluescreenofdeath/Techniques': 'Techniques-in-Slash\'EM-Extended.md',
        'User:Bluescreenofdeath/Dungeon_option': 'Dungeon-option-templates.md',
        'User:Bluescreenofdeath/Appearance_aptness': 'Appearance-aptnesses.md',
        'User:Bluescreenofdeath/Branches': 'Dungeon-overview.md',
        'User:Bluescreenofdeath/Materials': 'Item-materials.md',
        'User:Bluescreenofdeath/Egotypes': 'Monster-and-item-egotypes.md',
        'User:Bluescreenofdeath/Sinks_and_toilets': 'Identifying-rings-and-amulets.md',
        'User:Bluescreenofdeath/Evil_Variant': 'The-Evil-Variant.md',
        'User:Bluescreenofdeath/Friday_the_13th': 'Friday-the-13th.md',
        'User:Bluescreenofdeath/Known_Bugs': None,  # No corresponding page
        'Item_(Slash%27EM_Extended)': None,  # No corresponding page
        'Monster_(Slash%27EM_Extended)': None,  # No corresponding page
        'Trap_(Slash%27EM_Extended)': 'A-list-of-Slash\'EM-Extended\'s-new-traps.md',
        'Role difficulty/Variants#Slash.27EM_Extended_roles': 'A-list-of-Slash\'EM-Extended\'s-new-roles.md',
        'Race/Slash\'EM_Extended': 'A-list-of-Slash\'EM-Extended\'s-new-races.md',
        'Public_server': None,  # Could be server
    }
    
    # Special case for SlashTHEM Extended which exists as a page
    content = re.sub(r'\[\[SlashTHEM Extended\|SlashTHEM Extended\]\]', '[SlashTHEM Extended](SlashTHEM-Extended.md)', content)
    
    # Replace wiki links with GitHub Wiki links (preserving broken links for GitHub's edit mode)
    def replace_wiki_link(match):
        link_content = match.group(1)
        
        # Check if this is a category link, which should be removed
        if link_content.startswith('Category:'):
            # Return empty string to remove category links
            return ''
        
        # Check if this is a URL-style link (external link with space separator)
        # This handles cases like [[http://example.com text]] or [[ssh://server.com server]]
        if ' ' in link_content and any(link_content.startswith(proto) for proto in ['http://', 'https://', 'ftp://', 'ssh://', 'irc://', 'ircs://']):
            # Split on the first space to separate URL from display text
            space_index = link_content.find(' ')
            url = link_content[:space_index]
            display_text = link_content[space_index + 1:].strip()
            return f'[{display_text}]({url})'
        
        # Handle pipe syntax (e.g., [[Page|Display text]])
        if '|' in link_content:
            parts = link_content.split('|', 1)
            page_ref = parts[0].strip()
            display_text = parts[1].strip()
        else:
            page_ref = link_content.strip()
            display_text = page_ref
            
        # Convert page reference to file name format (with spaces replaced by hyphens)
        # For GitHub wikis, internal links should NOT have the .md extension
        file_name = page_ref.replace(" ", "-")
        
        # Check if page exists in our known pages
        page_key = page_ref.split('#')[0]  # Remove fragment identifier
        if page_key in known_pages:
            if known_pages[page_key]:
                # Use the mapped file name without .md for internal links
                mapped_name = known_pages[page_key]
                # Remove .md if it's present for consistency
                if mapped_name.endswith('.md'):
                    mapped_name = mapped_name[:-3]
                return f'[{display_text}]({mapped_name})'
            else:
                # If no corresponding page in known_pages mapping, preserve the link
                # so GitHub can direct to edit mode - but without .md extension
                return f'[{display_text}]({file_name})'
        else:
            # For other pages, preserve the link for GitHub to create - without .md extension
            # GitHub will show an edit page if the page doesn't exist
            return f'[{display_text}]({file_name})'
    
    # Apply the replacement for wiki links - exclude external links in [text](url) format
    # This regex matches [[text]] but not [text](url) patterns
    content = re.sub(r'\[\[([^\]]+)\]\](?!\()', replace_wiki_link, content)
    
    # Find and replace wiki tables with markdown tables using a more robust approach
    # Process the content to find and replace all wiki table patterns
    
    # Find all wiki tables by looking for {| ... |} patterns
    def find_all_tables(text):
        """Find all wiki table blocks in the text"""
        tables = []
        i = 0
        while i < len(text):
            start = text.find('{|', i)
            if start == -1:
                break
            # Find the matching |}
            level = 0
            j = start
            while j < len(text):
                if text[j:j+2] == '{|':
                    level += 1
                    j += 2
                elif text[j:j+2] == '|}':
                    level -= 1
                    if level == 0:
                        j += 2  # Move past |}
                        tables.append((start, j))
                        break
                    else:
                        j += 2
                else:
                    j += 1
            i = j if j > i else start + 2
        return tables
    
    # Process and replace all tables
    table_positions = find_all_tables(content)
    # Replace from the end backwards to avoid position shifting
    for start, end in reversed(table_positions):
        original_table = content[start:end]
        markdown_table = convert_wiki_table_to_markdown(original_table)
        content = content[:start] + markdown_table + content[end:]

    # Remove category links (both plain text and wiki format) at the end of files
    content = re.sub(r'\n*Category:[^\n]*\n*', '\n', content)  # Remove plain Category: lines
    content = re.sub(r'\[\[Category:[^\]]+\]\]', '', content)  # Remove wiki-style [[Category:...]] links
    
    # Clean up empty lines left after template removal
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content.strip()

def process_file(file_path):
    """
    Process a single file to fix wiki syntax
    """
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    new_content = fix_wiki_syntax(content)
    
    if original_content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Fixed syntax in {file_path}")
    else:
        print(f"  No changes needed for {file_path}")

def main():
    """
    Main function to process all markdown files in the current directory
    """
    import sys
    if len(sys.argv) > 1:
        # Process specific file
        process_file(sys.argv[1])
    else:
        # Process all markdown files in the directory
        for file in os.listdir('.'):
            if file.endswith('.md') and not file.startswith('fix_wiki_syntax'):
                process_file(file)

if __name__ == "__main__":
    main()