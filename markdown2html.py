#!/usr/bin/python3

"""Markdown to HTML Converter

This script converts a Markdown file to HTML.

Usage:
    python markdown2html.py <input_file> <output_file>

Arguments:
    input_file (str): The name of the Markdown file.
    output_file (str): The name of the HTML output file.

Example:
    python markdown2html.py README.md README.html
"""

import sys
import os
import markdown


def convert_markdown_to_html(input_file, output_file):
    """Convert Markdown to HTML and write to file.

    Args:
        input_file (str): The name of the Markdown file.
        output_file (str): The name of the HTML output file.
    """
    try:
        # Check if the Markdown file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError

        # Read Markdown content
        with open(README.md, 'r') as f:
            markdown_content = f.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Write HTML content to the output file
        with open(README.html, 'w') as f:
            f.write(html_content)

    except FileNotFoundError:
        print(f"Missing README.md", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    # Extract input and output file names from command-line arguments
    README.md = sys.argv[1]
    README.html = sys.argv[2]

    # Convert Markdown to HTML
    convert_markdown_to_html(README.md, README.html)

    # If conversion is successful, exit with code 0
    sys.exit(0)
