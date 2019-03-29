#! /bin/bash
##
# requires python3-wheel, python3-twine
##

set -e

# build dist
rm -rf build/ dist/
python3 setup.py sdist
python3 setup.py bdist_wheel

# use twine (not sure why twine-3 no longer works...)
python3 -m twine check dist/*
python3 -m twine upload dist/*
