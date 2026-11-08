#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'6\n3 1 3 2 1 4' $'Unique: 4\n1 2 3 4\n'
run_case $'2\n5 5' $'Unique: 1\n5\n'
run_case $'1\n-1' $'Unique: 1\n-1\n'
run_case "0" $'Unique: 0\n\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
