import nbformat
from nbformat.v4 import new_markdown_cell
import os

NOTEBOOK_DIR = os.path.join(os.path.dirname(__file__), '..', 'notebooks')

HEADER_TEMPLATE = """# {title}\n\nThis curated notebook demonstrates {title_lower}.\n\n## Contents\n1. Setup\n2. Tutorial\n3. Next Steps\n"""

def title_from_filename(path):
    base = os.path.splitext(os.path.basename(path))[0]
    return base.replace('-', ' ').replace('_', ' ').title()

def standardize_notebook(path):
    nb = nbformat.read(path, as_version=4)
    title = title_from_filename(path)
    header = HEADER_TEMPLATE.format(title=title, title_lower=title.lower())
    first_cell = nb.cells[0] if nb.cells else None
    if not first_cell or first_cell.get('cell_type') != 'markdown' or header.strip() not in ''.join(first_cell.get('source', '')).strip():
        nb.cells.insert(0, new_markdown_cell(header))
    for cell in nb.cells:
        if cell.get('cell_type') == 'code':
            source = cell.get('source', '') or ''
            lines = source.splitlines()
            if not lines:
                lines = []
            if not lines or not lines[0].strip().startswith('#'):
                lines.insert(0, '# TODO: describe cell')
            cell['source'] = '\n'.join(lines)
            cell['outputs'] = []
            cell['execution_count'] = None
    nbformat.write(nb, path)

if __name__ == '__main__':
    for fname in os.listdir(NOTEBOOK_DIR):
        if fname.endswith('.ipynb'):
            standardize_notebook(os.path.join(NOTEBOOK_DIR, fname))
