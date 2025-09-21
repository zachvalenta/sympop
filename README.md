# my existing tool

little tool I have to preview markdown doc headers.

```sh
#!/usr/bin/env python

"""
Extracts a heading-based outline tree from a Markdown file and prints it,
or writes to a file if --output=FILE is passed.

Usage:
    ext $FILE [--output=out.txt]
"""

import sys
from pathlib import Path
from markdown_it import MarkdownIt

def extract_heading_tree(md_text):
    md = MarkdownIt()
    tokens = md.parse(md_text)

    tree = []
    stack = []

    for token in tokens:
        if token.type == 'heading_open':
            level = int(token.tag[1])  # 'h2' -> 2
            inline = next(t for t in tokens if t.map == token.map and t.type == 'inline')
            text = ''.join(child.content for child in inline.children if child.type == 'text')

            while stack and stack[-1][0] >= level:
                stack.pop()

            indent = '\t' * len(stack)
            tree.append(f"{indent}{text}")
            stack.append((level, text))

    return '\n'.join(tree)

def main(argv):
    if not argv:
        print("Usage: ext file.md [--output=out.txt]")
        sys.exit(1)

    output_path = None
    paths = []

    for arg in argv:
        if arg.startswith("--output="):
            output_path = arg.split("=", 1)[1]
        else:
            paths.append(arg)

    for path_str in paths:
        path = Path(path_str)
        if not path.exists():
            print(f"File not found: {path}")
            continue

        md_text = path.read_text()
        output = extract_heading_tree(md_text)

        if output_path:
            Path(output_path).write_text(output)
        else:
            print(output)

if __name__ == "__main__":
    main(sys.argv[1:])
```

# what we're trying to build

Here's a screenshot of a tool I love, yazi, which is an interview file previewer.

Let's write yazi but strip it down to:

* can nav dir using vim motions
* can preview MD files by header i.e. output like the above mentioned CLI I wrote

This should be a TUI. Let's use Textual for implementation to start.

