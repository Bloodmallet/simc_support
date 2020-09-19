#!/bin/sh
. env/bin/activate

for D in "build" "dist" "simc_support.egg-info"; do
    if [ -d "${D}" ]; then
        rm -r ${D}
    fi
done

pip install -U -r requirements.txt
pip install -U setuptools wheel twine

python -m unittest

python setup.py sdist bdist_wheel
python -m twine upload dist/*
