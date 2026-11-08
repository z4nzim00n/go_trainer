#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "9" $'true\n'
run_case "17" $'true\n'
run_case "10" $'false\n'
run_case "21" $'true\n'
run_case "0" $'true\n'
run_case "7" $'true\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
