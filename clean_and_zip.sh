#!/usr/bin/env bash
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace *.ipynb
zip -r solution.zip ml_project notebooks
