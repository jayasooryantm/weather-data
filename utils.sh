#!/bin/bash

# Remove existing zip file
rm -f data_bundle.zip

# Zip JSON files
zip -r data_bundle.zip data/*.json

echo "JSON files zipped and existing zip deleted."
