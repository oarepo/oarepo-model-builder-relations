#!/bin/bash

set -e

python3 -m venv .venv-builder
.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install -e .


BUILDER=.venv-builder/bin/oarepo-compile-model


if true ; then
    test -d model-referred && rm -rf model-referred
    test -d model-referrer && rm -rf model-referrer
    ${BUILDER} tests/referred.yaml --output-directory model-referred -vvv
    ${BUILDER} tests/referrer.yaml --output-directory model-referrer -vvv --include referred=model-referred/referred/models/model.json
fi

python3 -m venv .venv-tests
source .venv-tests/bin/activate

pip install -U setuptools pip wheel
pip install pyyaml opensearch-dsl 
pip install -e model-referred
pip install -e model-referrer
pip install pytest-invenio

pytest tests