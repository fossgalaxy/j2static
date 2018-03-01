j2static
====================================

j2static is a static site generator based around jinja2.

Using the tool
--------------
j2static assumes that you have jinja templates stored in _template/ which should
be coverted into html documents. You can generate html documents by executing
generate::

    $ j2static generate

Webserver Mode
--------------
j2static can also provide a (very basic) webserver operating on localhost, you
can use this to develop your templates. To activate webserver mode, use the
serve command::

    $ j2static serve

When in webserver mode, files are not generated. Instead, the server rebuilds
the template on every request. This is slower than fetching the files from disk
but should mean it always reflects your changes.
