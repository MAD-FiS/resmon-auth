#!/bin/bash

# Generates python documentation. Move html files to docs dictionary
if [ -z ${RESMONAUTHENV+x} ]; then
    source data/resmon-auth.env
fi

pydoc3 -w $(pydoc3 -k src)
for f in ./*.html ; do mv "$f" ./docs/ ; done
