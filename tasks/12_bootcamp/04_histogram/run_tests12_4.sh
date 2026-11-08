#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n1 2 1 3 3' $'1: **\n2: *\n3: **\n'
run_case $'3\n9 9 9' $'9: ***\n'
run_case "0" ""

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
