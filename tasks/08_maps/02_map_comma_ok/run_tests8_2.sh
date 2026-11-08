#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\ncat 5\ndog 7\nfish 2\ndog' $'7\n'
run_case $'1\na 0\na' $'0\n'
run_case $'1\na 1\nb' $'NOT FOUND\n'
run_case $'2\nx -1\ny 4\ny' $'4\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
