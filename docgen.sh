#!/usr/bin/env bash

# Generates python documentation. Move html files to docs dictionary
if [ -z ${RESMONAUTHENV+x} ]; then
    echo "RESMONAUTHENV is unset."
    echo "Please perform 'source ./resmon-auth-env.sh'"
    exit 1
else
    pydoc3 -w $(pydoc3 -k src)
    for f in ./*.html ; do mv "$f" ./docs/ ; done
fi
