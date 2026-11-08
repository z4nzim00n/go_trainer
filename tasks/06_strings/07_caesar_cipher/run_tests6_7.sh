#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\nHello, World!' $'Khoor, Zruog!\n'
run_case $'1\nabcXYZ' $'bcdYZA\n'
run_case $'0\nNo change' $'No change\n'
run_case $'26\nabc' $'abc\n'
run_case $'-1\nabc' $'zab\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
