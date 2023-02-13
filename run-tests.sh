#!/bin/bash

set -e

python3 -m venv .venv
.venv/bin/pip install -U setuptools pip wheel
.venv/bin/pip install -e .
.venv/bin/pip install oarepo-model-builder-cf


BUILDER=.venv/bin/oarepo-compile-model


if true ; then
    test -d tests/referred && rm -rf tests/referred
    test -d tests/referrer && rm -rf tests/referrer
    ${BUILDER} tests/referred.yaml --output-directory tests/referred -vvv
    ${BUILDER} tests/referrer.yaml --output-directory tests/referrer -vvv --include referred=tests/referred/referred/models/model.json
fi

python3 -m venv .venv-tests
source .venv-tests/bin/activate

pip install -U setuptools pip wheel
pip install pyyaml opensearch-dsl 
pip install -e tests/referred
pip install -e tests/referrer
pip install pytest-invenio

pytest tests