# Wiki to GitHub Markdown Converter

This script converts MediaWiki syntax to GitHub-flavored markdown, specifically designed for migrating content from MediaWiki-based wikis (like Wikipedia) to GitHub wikis.

## Features

- Converts MediaWiki headings (`== Heading ==`) to GitHub markdown headings (`# Heading`)
- Converts MediaWiki tables (`{| ... |}`) to GitHub markdown tables
- Converts MediaWiki links (`[[Page]]`) to GitHub markdown links (`[Page](Page)`)
- Converts MediaWiki templates (`{{Template|Content}}`) to formatted notes (`**Note:** Content`)
- Removes MediaWiki image syntax (`[[Image:...]]`)
- Removes MediaWiki category links (`[[Category:...]]`)
- Links to non-existent pages are preserved, allowing GitHub to create an edit page

## Requirements

- Python 3.6 or higher
- `toml` library (install with `pip install toml` if using Python < 3.11)

## Usage

### Convert a single file:

```bash
python fix_wiki_syntax.py path/to/your/file.md
```

### Convert multiple files:

```bash
python fix_wiki_syntax.py file1.md file2.md file3.md
```

### Convert files with a custom mapping file:

```bash
python fix_wiki_syntax.py -m path/to/your/mapping.toml file1.md file2.md
```

### Convert all markdown files in the current directory:

```bash
python fix_wiki_syntax.py
```

## Configuration

The script looks for a `mapping.toml` file in the same directory to map specific wiki page names to GitHub wiki file names. The script supports two TOML formats:

**Format 1 - Simple key-value pairs:**
```toml
["Wiki Page Name"] = "filename"     # For existing pages (no .md extension needed)
["Another Page"] = null             # For pages that don't exist (creates edit link)
```

**Format 2 - Table format:**
```toml
["Wiki Page Name"]
dest = "filename"

["Another Page"]
dest = "null"                       # For pages that don't exist (creates edit link)
```

Example mapping.toml:
```toml
["User:Example/Hints"] = "hints"
["User:Example/FAQ"] = "faq"
["NonExistentPage"] = null
```

Or using the table format:
```toml
["User:Example/Hints"]
dest = "hints"

["User:Example/FAQ"]
dest = "faq"

["NonExistentPage"]
dest = "null"
```

If no `mapping.toml` file exists, all wiki links will be converted using a simple transformation (spaces replaced with hyphens).

You can specify a custom mapping file using the `-m` or `--mapping` command-line option.

## Customization

You can customize the mapping file to handle specific page name transformations for your wiki. This allows you to maintain proper links between pages during the migration process.

## How It Works

The script processes wiki syntax patterns and converts them as follows:

- Headings: `== Heading ==` → `# Heading`
- Links: `[[Page]]` → `[Page](Page)`
- Tables: MediaWiki table syntax → GitHub markdown table syntax
- Templates: `{{template|content}}` → `**Note:** content`

For GitHub wiki pages that don't exist, the script creates links that will take you to an edit page where you can create the new page.

## Notes

- The script modifies files in place, so make sure to backup your files before running it.
- Links to non-existent pages will appear as broken links but will take you to a page where you can create the content.
- The script is designed to work with GitHub wikis, but the output is also compatible with regular GitHub markdown.