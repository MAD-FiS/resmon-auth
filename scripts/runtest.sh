#!/bin/bash

# Run tests
if [ -z ${RESMONAUTHENV+x} ]; then
    source ./data/resmon-auth.env
fi

python3 test/unit_test.py
