#!/usr/bin/python3

import sys
import os
import markdown


def convert_markdown_to_html(input_file, output_file):
    try:
        # Check if the Markdown file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError

        # Read Markdown content
        with open(input_file, 'r') as f:
            markdown_content = f.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Write HTML content to the output file
        with open(output_file, 'w') as f:
            f.write(html_content)

    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)

    # Extract input and output file names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML
    convert_markdown_to_html(input_file, output_file)

    # If conversion is successful, exit with code 0
    sys.exit(0)
