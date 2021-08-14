from pathlib import Path
import markdown
from markdown.extensions.toc import TocExtension

BASE_DIR = "../files"

def list():
    paths = Path(BASE_DIR).glob('**/*')

    files = []

    for path in paths:
        if path.is_file():
            files.append(str(path).replace(BASE_DIR, ""))
    
    return sorted(files)

def html(file):
    return markdown.markdown(Path(BASE_DIR + file).read_text(), extensions=['fenced_code', TocExtension(title='Contents', toc_depth="2-5"), 'codehilite'])

def raw(file):
    return Path(BASE_DIR + file).read_text()

def save(file, contents):
    Path(BASE_DIR + file).write_text(contents, encoding="utf-8")

def new(file):
    path = Path(BASE_DIR + file)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.touch()