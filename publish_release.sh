#!/bin/sh
echo "Activating environment"
. ./env/bin/activate

echo "Removing old artifacts"
for D in "build" "dist" "simc_support.egg-info"; do
    if [ -d "${D}" ]; then
        rm -r ${D}
    fi
done

echo "Install requirements"
pip install -U -r requirements.txt
pip install -U setuptools wheel build twine

echo "Execute unittest"
python -m unittest

echo "Build wheel"
python -m build

echo "Publish"
python -m twine upload dist/*
