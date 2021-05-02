$ErrorActionPreference = "Stop"

echo "Activating environment"
.\env\Scripts\activate

function Remove-Artifacts {
    [CmdletBinding()]
    param ()

    echo "Removing Build Artifacts"
    Foreach ($D in @("build", "dist", "simc_support.egg-info")) {
        if (Test-Path "${D}") {
            echo "    ${D}"
            rm -r "${D}"
        }
    }
}

Remove-Artifacts

echo "Install requirements"
pip install -U -r requirements.txt
pip install -U setuptools wheel twine

echo "Execute unittest"
python -m unittest

echo "Build wheel"
python setup.py sdist bdist_wheel

echo "Publish"
# python -m twine upload dist/*

Remove-Artifacts
