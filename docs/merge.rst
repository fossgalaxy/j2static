j2merge
====================================

j2merge is a command line utilty that ships with j2static. It is a system for generating a set of documents from a template and a set of source data ('mail merge').

Using the tool
--------------
j2merge needs to know two things in order to generate outputs, the source data
(in csv format) and the template (jinja2 template). The template name defaults
to `base.html` so you can omit it if you do this::

    $ j2merge data.csv

j2merge assumes the csv file contains headers, which will be used as the
variable names in the template. j2merge also assumes that there is a column
named id, which will be used to generate the resulting filename.

Contextual data
---------------
Sometimes it is useful to be able to pass additional data into the template
system from another source. Presently, the only supported sources are json
files.

To use this functionality, pass the name of the json file is as a parameter::

    $ j2merge data.csv --context=extra.json

The data stored in the json file will be loaded into the template.

PDF mode
--------
j2merge can generate PDFs using its LaTeX support, to do so you must tell it
that you want to generate pdfs as your artifacts::

    $ j2merge data.csv --builder=pdf

in this mode, j2merge will assume that your template is named `base.tex`. You
will need a LaTeX distribution and latemk installed in order to use this
feature.
