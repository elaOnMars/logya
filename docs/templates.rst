.. templates:

Templates
=========

The template engine that comes with Logya is `jinja2 <http://jinja.pocoo.org/>`_. In addition to the many features jinja2 provides you can use the following filters/functions.

urlencode
---------

This filter can be used to encode variables so they are safe to use as URL parameters, see an example as used in the default starter site.

::

    <a href="http://reddit.com/submit?url={{canonical|urlencode}}&title={{title|urlencode}}">Reddit</a><

Here ``urlencode`` is used to encode the values of the ``url`` and ``title`` parameters in a link to submit the current page to Reddit.

filesource
----------

You can use the ``filesource`` function to include the text of an external file on a page. The optional ``limit`` parameter specifies how many lines to include, if not provided the whole file will be included. The file content is escaped, so that you can display HTML or other source code. The example below is taken from the `d3.geomap documentation <http://d3-geomap.github.io/>`_.

::

    {{ filesource('static/html/d3.geomap.html') }}
    {{ filesource('static/js/maps/world-plain.js') }}

This function is mainly intended for documentation purposes as it allows you to include the same source code that is used to render an example visible on the current page. Restricting the number of lines works as follows.

::

     <pre>{{ filesource(data, lines=6) }}...</pre>