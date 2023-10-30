#!/bin/bash

set -e

OAREPO_VERSION=${OAREPO_VERSION:-11}
OAREPO_VERSION_MAX=$((OAREPO_VERSION+1))

if [ -d .venv-builder ] ; then
    rm -rf .venv-builder
fi

python3 -m venv .venv-builder
.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install -e .


BUILDER=.venv-builder/bin/oarepo-compile-model


if true ; then
    test -d model-referred && rm -rf model-referred
    test -d model-referrer && rm -rf model-referrer
    ${BUILDER} tests/referred.yaml --output-directory model-referred -vvv
    ${BUILDER} tests/referrer.yaml --output-directory model-referrer -vvv --include referred=model-referred/referred/models/records.json
fi

if [ -d .venv-tests ] ; then
    rm -rf .venv-tests
fi


python3 -m venv .venv-tests
source .venv-tests/bin/activate

pip install -U setuptools pip wheel
pip install pyyaml opensearch-dsl
pip install "oarepo>=$OAREPO_VERSION,<$OAREPO_VERSION_MAX"
pip install -e model-referred
pip install -e model-referrer
pip install pytest-invenio

pytest tests