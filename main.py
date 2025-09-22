#!/usr/bin/env python3

"""
A minimal TUI file browser for Markdown files with header preview.
Inspired by yazi but focused on Markdown outline viewing.

Usage:
    python md_browser.py [directory]

Controls:
    j/k or ↓/↑  - Navigate files
    h/l or ←/→  - Navigate directories (h=up, l=down)
    Enter       - Enter directory / view file
    q           - Quit
"""

import sys
from pathlib import Path
from typing import List, Optional

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import DirectoryTree, Static, Header, Footer
from textual.binding import Binding
from textual import events
from markdown_it import MarkdownIt


class MarkdownOutline(Static):
    """Widget to display Markdown heading outline."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.border_title = "Preview"
    
    def extract_heading_tree(self, md_text: str) -> str:
        """Extract heading outline from markdown text."""
        md = MarkdownIt()
        tokens = md.parse(md_text)

        tree = []
        stack = []

        for token in tokens:
            if token.type == 'heading_open':
                level = int(token.tag[1])  # 'h2' -> 2
                # Find the corresponding inline token
                inline_token = None
                for i, t in enumerate(tokens):
                    if t.map == token.map and t.type == 'inline':
                        inline_token = t
                        break
                
                if inline_token:
                    text = ''.join(child.content for child in inline_token.children 
                                 if child.type == 'text')
                else:
                    text = "Untitled"

                while stack and stack[-1][0] >= level:
                    stack.pop()

                indent = '  ' * len(stack)  # Use spaces for better display
                tree.append(f"{indent}{text}")
                stack.append((level, text))

        return '\n'.join(tree) if tree else "No headings found"
    
    def update_preview(self, file_path: Optional[Path]):
        """Update the preview with file content."""
        if not file_path or not file_path.exists():
            self.update("No file selected")
            return
        
        if file_path.is_dir():
            # Show directory contents
            try:
                contents = sorted(file_path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
                items = []
                for item in contents[:20]:  # Limit to first 20 items
                    prefix = "📁 " if item.is_dir() else "📄 "
                    items.append(f"{prefix}{item.name}")
                if len(contents) > 20:
                    items.append("...")
                self.update("\n".join(items))
            except PermissionError:
                self.update("Permission denied")
            return
        
        if file_path.suffix.lower() in ['.md', '.markdown']:
            try:
                md_text = file_path.read_text(encoding='utf-8')
                outline = self.extract_heading_tree(md_text)
                self.update(outline)
            except Exception as e:
                self.update(f"Error reading file: {e}")
        else:
            # Show file info for non-markdown files
            try:
                size = file_path.stat().st_size
                size_str = f"{size:,} bytes"
                if size > 1024:
                    size_str += f" ({size/1024:.1f} KB)"
                if size > 1024*1024:
                    size_str += f" ({size/(1024*1024):.1f} MB)"
                
                self.update(f"File: {file_path.name}\nSize: {size_str}\nType: {file_path.suffix or 'No extension'}")
            except Exception as e:
                self.update(f"Error reading file info: {e}")


class FileTree(DirectoryTree):
    """Custom DirectoryTree with vim-like keybindings."""
    
    def __init__(self, path: str, **kwargs):
        super().__init__(path, **kwargs)
        self.border_title = f"Files: {Path(path).resolve()}"


class MarkdownBrowser(App):
    """A Textual app for browsing Markdown files with header preview."""
    
    CSS = """
    FileTree {
        width: 50%;
        border: solid $primary;
    }
    
    MarkdownOutline {
        width: 50%;
        border: solid $primary;
        padding: 1;
    }
    
    .file-browser {
        height: 100%;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("j", "cursor_down", "Down", show=False),
        Binding("k", "cursor_up", "Up", show=False),
        Binding("h", "cursor_left", "Back", show=False),
        Binding("l", "cursor_right", "Forward", show=False),
        Binding("enter", "select", "Select", show=False),
    ]
    
    def __init__(self, start_dir: str = "."):
        super().__init__()
        self.start_dir = Path(start_dir).resolve()
    
    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(classes="file-browser"):
            yield FileTree(str(self.start_dir), id="file_tree")
            yield MarkdownOutline(id="preview")
        yield Footer()
    
    def on_mount(self) -> None:
        """Initialize the app."""
        file_tree = self.query_one("#file_tree", FileTree)
        preview = self.query_one("#preview", MarkdownOutline)
        
        # Set initial focus and preview
        file_tree.focus()
        if file_tree.cursor_node:
            preview.update_preview(Path(file_tree.cursor_node.data.path))
    
    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        """Handle file selection."""
        preview = self.query_one("#preview", MarkdownOutline)
        preview.update_preview(Path(event.path))
    
    def on_directory_tree_directory_selected(self, event: DirectoryTree.DirectorySelected) -> None:
        """Handle directory selection."""
        preview = self.query_one("#preview", MarkdownOutline)
        preview.update_preview(Path(event.path))
    
    def action_cursor_down(self) -> None:
        """Move cursor down (j key)."""
        file_tree = self.query_one("#file_tree", FileTree)
        file_tree.action_cursor_down()
        if file_tree.cursor_node:
            preview = self.query_one("#preview", MarkdownOutline)
            preview.update_preview(Path(file_tree.cursor_node.data.path))
    
    def action_cursor_up(self) -> None:
        """Move cursor up (k key)."""
        file_tree = self.query_one("#file_tree", FileTree)
        file_tree.action_cursor_up()
        if file_tree.cursor_node:
            preview = self.query_one("#preview", MarkdownOutline)
            preview.update_preview(Path(file_tree.cursor_node.data.path))
    
    def action_cursor_left(self) -> None:
        """Go to parent directory (h key)."""
        file_tree = self.query_one("#file_tree", FileTree)
        file_tree.action_cursor_parent()
        if file_tree.cursor_node:
            preview = self.query_one("#preview", MarkdownOutline)
            preview.update_preview(Path(file_tree.cursor_node.data.path))
    
    def action_cursor_right(self) -> None:
        """Enter directory or expand (l key)."""
        file_tree = self.query_one("#file_tree", FileTree)
        if file_tree.cursor_node:
            if Path(file_tree.cursor_node.data.path).is_dir():
                if not file_tree.cursor_node.is_expanded:
                    file_tree.cursor_node.expand()
                # Move cursor to first child if directory has children
                if file_tree.cursor_node.children:
                    file_tree.cursor_node = file_tree.cursor_node.children[0]
            preview = self.query_one("#preview", MarkdownOutline)
            preview.update_preview(Path(file_tree.cursor_node.data.path))
    
    def action_select(self) -> None:
        """Select file/directory (Enter key)."""
        file_tree = self.query_one("#file_tree", FileTree)
        if file_tree.cursor_node:
            if Path(file_tree.cursor_node.data.path).is_dir():
                file_tree.cursor_node.toggle()
            preview = self.query_one("#preview", MarkdownOutline)
            preview.update_preview(Path(file_tree.cursor_node.data.path))


def main():
    """Main entry point."""
    start_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    if not Path(start_dir).exists():
        print(f"Error: Directory '{start_dir}' does not exist")
        sys.exit(1)
    
    app = MarkdownBrowser(start_dir)
    app.run()


if __name__ == "__main__":
    main()
