import pkg_resources
import os
from string import Template
from .project import Project

def add_file_from_template(template_path, out_path, project):
    if os.path.isfile(out_path):
        print(f"file {out_path} already exists, skipping")
    if not pkg_resources.resource_exists('ary', template_path):
        raise FileNotFoundError(template_path)

    template_path = pkg_resources.resource_filename('ary', f'{template_path}')
    template_file = open(template_path)
    text = template_file.read()
    text = Template(text)
    text = text.substitute(name=project.name, language=project.language, author=project.author)
    out_file = open(out_path, 'x')
    out_file.write(text)
    out_file.close()