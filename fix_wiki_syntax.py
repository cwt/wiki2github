#!/usr/bin/env python3
"""
Script to fix incompatible Wiki syntax in GitHub Wiki files
"""

import re
import os

# Use toml from standard library for Python 3.11+, fallback to external library for older versions
try:
    import tomllib  # Python 3.11+
except ImportError:
    import toml as tomllib  # External library as fallback


def convert_wiki_table_to_markdown(table_content):
    """
    Convert wiki table format to markdown table format
    """
    lines = table_content.split("\n")
    result_lines = []

    headers = []
    rows = []

    # Process table lines to extract headers and rows
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if line.strip().startswith("{|"):  # Start of table
            i += 1
            continue
        elif line.strip() == "|}":  # End of table
            break
        elif line.strip() == "|-":  # Row separator
            i += 1
            continue
        elif line.lstrip().startswith("!"):  # Header line
            # Handle headers - split by !! or process line by line
            line.lstrip()[1:]  # Remove leading '!'

            # Extract individual headers. In wiki syntax, each ! starts a new cell
            # Look for subsequent ! lines that continue the same header row
            headers = []
            j = i
            while j < len(lines):
                check_line = lines[j].rstrip()
                if check_line.lstrip().startswith("!"):
                    content = check_line.lstrip()[1:]  # Remove leading '!'
                    # Check if this line contains multiple headers separated by !!
                    if "!!" in content:
                        headers.extend([h.strip() for h in content.split("!!")])
                        break  # All headers are on this line
                    else:
                        headers.append(content.strip())
                elif check_line.strip() in ["|-", "|}"]:
                    break  # End of header row
                else:
                    # For multiline header content, append to the last header
                    if headers:
                        headers[-1] += " " + check_line.strip()
                j += 1
            i = j
            continue
        elif (
            line.lstrip().startswith("|") and not line.strip() == "|-"
        ):  # Data row
            # Process data cells - each | starts a new cell in wiki syntax
            # But we need to handle cells that span multiple lines
            row = []
            j = i
            while j < len(lines):
                check_line = lines[j].rstrip()
                if check_line.strip() == "|-":  # Next row separator
                    break
                elif check_line.strip() == "|}":  # End of table
                    break
                elif check_line.lstrip().startswith("|"):  # Data cell
                    content = check_line.lstrip()[1:]  # Remove leading '|'
                    # Check if this line contains multiple cells separated by ||
                    if "||" in content:
                        cells = [cell.strip() for cell in content.split("||")]
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
        header_row = "|"
        for header in headers:
            header_row += f" {header} |"
        result_lines.append(header_row)

        # Create separator row - make sure we have the right number of separators
        separator_row = "|"
        for _ in headers:
            separator_row += " --- |"
        result_lines.append(separator_row)

    # Create data rows
    for row in rows:
        data_row = "|"
        for cell in row:
            data_row += f" {cell} |"
        result_lines.append(data_row)

    return "\n".join(result_lines)


def extract_template_content(match):
    """
    Extract content from wiki template syntax {{template|content}} to create a note
    """
    template_text = match.group(0)[2:-2]  # Remove the {{ and }}
    if "|" in template_text:
        content = template_text.split("|", 1)[
            -1
        ].strip()  # Get content after first |
    else:
        content = template_text.strip()
    return f"**Note:** {content}"


def load_known_pages_mapping(mapping_file="mapping.toml"):
    """
    Load the known pages mapping from a TOML file.
    If the file doesn't exist, return an empty dictionary.
    """
    if os.path.exists(mapping_file):
        with open(mapping_file, "r", encoding="utf-8") as f:
            data = tomllib.load(f)

        # Convert TOML data to the expected format (None for None values)
        known_pages = {}
        for key, value in data.items():
            known_pages[key] = value
        return known_pages
    else:
        # Return empty mapping if file doesn't exist
        return {}


def fix_wiki_syntax(content, mapping_file="mapping.toml"):
    """
    Fix various incompatible Wiki syntax patterns in the content
    """
    # Load known pages mapping from external file
    known_pages = load_known_pages_mapping(mapping_file)

    # Fix heading syntax first (e.g., == Heading == becomes ## Heading ##)
    # Match == Heading ==, === Heading ===, etc.
    def replace_heading(match):
        heading_level = len(match.group(1))
        heading_text = match.group(2).strip()
        return "#" * heading_level + " " + heading_text

    # Handle both == Heading == and === Heading === formats
    content = re.sub(r"(={2,6})\s*(.*?)\s*\1", replace_heading, content)

    # Fix template syntax like {{Delete|...}} and {{todo|...}}
    content = re.sub(r"\{\{[^}]+\}\}", extract_template_content, content)

    # Remove standalone templates that don't have content value
    content = re.sub(r"\{\{[^\|}]+\}\}", "", content)

    # Fix image links (remove [[Image:...|thumb|...]] syntax)
    content = re.sub(r"\[\[Image:[^\]]+\]\]", "", content)
    content = re.sub(r"\[\[File:[^\]]+\]\]", "", content)

    # Special case for SlashTHEM Extended which exists as a page
    content = re.sub(
        r"\[\[SlashTHEM Extended\|SlashTHEM Extended\]\]",
        "[SlashTHEM Extended](SlashTHEM-Extended.md)",
        content,
    )

    def convert_wiki_link_to_markdown(match):
        """
        Convert wiki link syntax [[Page|Display Text]] to markdown [Display Text](Page)
        """
        link_content = match.group(1)

        # Check if this is a category link, which should be removed
        if link_content.startswith("Category:"):
            # Return empty string to remove category links
            return ""

        # Check if this is a URL-style link (external link with space separator)
        # This handles cases like [[http://example.com text]] or [[ssh://server.com server]]
        if " " in link_content and any(
            link_content.startswith(proto)
            for proto in [
                "http://",
                "https://",
                "ftp://",
                "ssh://",
                "irc://",
                "ircs://",
            ]
        ):
            # Split on the first space to separate URL from display text
            space_index = link_content.find(" ")
            url = link_content[:space_index]
            display_text = link_content[space_index + 1 :].strip()
            return f"[{display_text}]({url})"

        # Handle pipe syntax (e.g., [[Page|Display text]])
        if "|" in link_content:
            parts = link_content.split("|", 1)
            page_ref = parts[0].strip()
            display_text = parts[1].strip()
        else:
            page_ref = link_content.strip()
            display_text = page_ref

        # Convert page reference to file name format (with spaces replaced by hyphens)
        # For GitHub wikis, internal links should NOT have the .md extension
        file_name = page_ref.replace(" ", "-")

        # Check if page exists in our known pages
        page_key = page_ref.split("#")[0]  # Remove fragment identifier
        if page_key in known_pages:
            if known_pages[page_key]:
                # Use the mapped file name without .md for internal links
                mapped_name = known_pages[page_key]
                # Remove .md if it's present for consistency
                if mapped_name.endswith(".md"):
                    mapped_name = mapped_name[:-3]
                return f"[{display_text}]({mapped_name})"
            else:
                # If no corresponding page in known_pages mapping, preserve the link
                # so GitHub can direct to edit mode - but without .md extension
                return f"[{display_text}]({file_name})"
        else:
            # For other pages, preserve the link for GitHub to create - without .md extension
            # GitHub will show an edit page if the page doesn't exist
            return f"[{display_text}]({file_name})"

    # Apply the replacement for wiki links - exclude external links in [text](url) format
    # This regex matches [[text]] but not [text](url) patterns
    content = re.sub(
        r"\[\[([^\]]+)\]\](?!\()", convert_wiki_link_to_markdown, content
    )

    # Find and replace wiki tables with markdown tables using a more robust approach
    # Process the content to find and replace all wiki table patterns

    def find_all_tables(text):
        """Find all wiki table blocks in the text using a stack-based approach"""
        tables = []
        start_positions = []

        i = 0
        while i < len(text) - 1:
            if text[i : i + 2] == "{|":
                start_positions.append(i)
                i += 2
            elif text[i : i + 2] == "|}" and start_positions:
                start_pos = start_positions.pop()
                if (
                    not start_positions
                ):  # Only when we've closed the outermost table
                    tables.append((start_pos, i + 2))
                i += 2
            else:
                i += 1
        return tables

    # Process and replace all tables
    table_positions = find_all_tables(content)
    # Replace from the end backwards to avoid position shifting
    for start, end in reversed(table_positions):
        original_table = content[start:end]
        markdown_table = convert_wiki_table_to_markdown(original_table)
        content = content[:start] + markdown_table + content[end:]

    # Remove category links (both plain text and wiki format) at the end of files
    content = re.sub(
        r"\n*Category:[^\n]*\n*", "\n", content
    )  # Remove plain Category: lines
    content = re.sub(
        r"\[\[Category:[^\]]+\]\]", "", content
    )  # Remove wiki-style [[Category:...]] links

    # Clean up empty lines left after template removal
    content = re.sub(r"\n\s*\n\s*\n", "\n\n", content)

    return content.strip()


def process_file(file_path, mapping_file="mapping.toml"):
    """
    Process a single file to fix wiki syntax
    """
    print(f"Processing {file_path}...")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    new_content = fix_wiki_syntax(content, mapping_file)

    if original_content != new_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Fixed syntax in {file_path}")
    else:
        print(f"  No changes needed for {file_path}")


def get_markdown_files():
    """
    Get all markdown files in the current directory, excluding this script
    """
    return [
        f
        for f in os.listdir(".")
        if f.endswith(".md") and not f.startswith("fix_wiki_syntax")
    ]


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
        for file in get_markdown_files():
            process_file(file)


if __name__ == "__main__":
    main()
