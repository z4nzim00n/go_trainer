#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "2 3" $'5\n'
run_case "-4 10" $'6\n'
run_case "0 0" $'0\n'
run_case "1000000 2000000" $'3000000\n'
run_case $'7\n8' $'15\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
