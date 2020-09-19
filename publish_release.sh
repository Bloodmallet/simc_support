#!/bin/sh
source env/bin/activate

DIRECTORIES=("build" "dist" "simc_support.egg-info")
for D in ${DIRECTORIES}; do
    if [ -d "${D}" ]; then
        rm -r ${D}
    fi
done

pip install -U -r requirements.txt
pip install -U setuptools wheel twine

python -m unittest

python setup.py sdist bdist_wheel
python -m twine upload dist/*
