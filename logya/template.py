# -*- coding: utf-8 -*-
import io
import os

from jinja2 import Environment, BaseLoader, TemplateNotFound, escape


def filesource(logya_inst, name, lines=None):
    """Read and return source of text files.

    A template function that reads the source of the given file and returns it.
    The text is escaped so it can be rendered safely on a Web page.
    The lines keyword argument is used to limit the number of lines returned.

    A use case is for documentation projects to show the source code used
    to render the current example.
    """

    fname = os.path.join(logya_inst.dir_site, name)
    with io.open(fname, 'r', encoding='utf-8') as f:
        if lines is None:
            content = f.read()
        else:
            content = ''.join(f.readlines()[:lines])
    return escape(content)


def get_doc(logya_inst, url):
    """Get document located at given URL."""

    return logya_inst.docs.get(url)


class Template():
    """Class to handle templates."""

    def __init__(self, logya_inst):
        """Initialize template environment."""

        self.vars = {}
        self.dir_templates = logya_inst.dir_templates
        self.env = Environment(loader=TemplateLoader(self.dir_templates))

        # self.env.trim_blocks = True

        # add filesource global to allow for including the source of a file
        self.env.globals['filesource'] = lambda x, lines=None: filesource(
            logya_inst, x, lines=lines)

        self.env.globals['get_doc'] = lambda x: get_doc(logya_inst, x)


class TemplateLoader(BaseLoader):

    """Class to handle template Loading."""

    def __init__(self, path):
        """Set template path."""

        self.path = path

    def get_source(self, environment, template):
        """Set template source."""

        path = os.path.join(self.path, template)
        if not os.path.exists(path):
            raise TemplateNotFound(template)
        mtime = os.path.getmtime(path)
        with io.open(path, 'r', encoding='utf-8') as f:
            source = f.read()
        return source, path, lambda: mtime == os.path.getmtime(path)
