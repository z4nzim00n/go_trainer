#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\n20 20 20' $'Coffee: 10\n'
run_case $'1\n20' $'Need: 30\n'
run_case $'2\n50 10' $'Coffee: 10\n'
run_case "0" $'Need: 50\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
