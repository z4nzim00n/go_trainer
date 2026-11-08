#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n1 2 3 2 1' $'3\n'
run_case $'3\n4 4 -7' $'-7\n'
run_case $'1\n42' $'42\n'
run_case $'5\n8 8 0 0 5' $'5\n'
run_case $'7\n1 2 3 1 3 2 9' $'9\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
