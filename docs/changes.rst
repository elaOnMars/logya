.. changes:

Changes
=======

3.3.0 to 4.0.0
--------------

The 4.0.0 release includes several backwards incompatible changes, that affect external scripts that access Logya attibutes, as well as RSS and index templates.

* Renamed docs_parsed to docs.
* Enable configuration of index templates.
* Restructured site configuration.
* Renamed indexes to index/docs/collections.
* Removed all_vars and doc_vars from Template.
* Removed Config class, the config module now consits of load and search_dict_list functions.
* More structured data markup in starter site.
* More comprehensive and updated documentation.
* Removed run command, import Logya in custom scripts instead.
* Removed automatic execution of scripts in bin directory.
* Renamed logya.dir_current to logya.dir_site.
* Renamed dir_dst and dir_current.
* Removed FileWriter class entirely.
* Moved canonical_filename to path module.
* Set feed limit in rss template so user can set this to a preferred value.
* Updated dependecies.

3.2.2 to 3.3.0
--------------

* More pythonic and readable code.
* Use tox for running tests against different python versions.
* Issue #58: header attribute url is now optional and will be set from file name if not present.
* Added path module and tests for it.
* Made logya run Python3 compatible.
* Fixed #52: Removed ext and test.py and code that referenced them.
* Fixed #48: Use .htaccess from HTML5 Boilerplate.
* New style string formatting.
* Added tests for docparser and docreader modules.
* More appropriate function names.
* Use fontawesome icons for reddit and stumbleupon.
* Fixed #39: added sample video macro.
* Updated bootstrap.
* Better documentation of filesource template function.
* Write count of generated documents and indexes in verbose mode of generate command, not individual index file names.
* Added default robots.txt to starter site.
* Added datePublished and dateModified schema markup to post and postinfo templates.

3.2.1 to 3.2.2
--------------

* Updated bootstrap, jquery and fontawesome.
* Use updated property for lastmod in xml sitemap.
* Added postinfo template and sample post that displays it.
* Added author setting to site.yaml.
* Added updated property to document header, if not set by author.

3.2.0 to 3.2.1
--------------

* Allow for non-existing body so a doc can only consist of header values.

3.1.0 to 3.2.0
--------------

* Use yaml's CLoader if available. For complex data structures performance gains are huge.
* Added run command.

3.0 to 3.1.0
------------

* Added get_doc template function.

2.3 to 3.0
----------

Logya version 3.0 is not backwards compatible due to changed configuration.

* YAML based site configuration.
* Python 3 compatibility.
* RSS is generated using template that is now included from create command.