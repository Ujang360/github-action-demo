#!/usr/bin/env bash

././setup-test.sh
echo
echo 'PyTest PEP8 Tests...'
py.test --pep8
echo
echo 'PyTest Unit Tests...'
py.test
echo
