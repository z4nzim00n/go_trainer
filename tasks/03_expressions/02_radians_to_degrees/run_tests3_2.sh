#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "3.141592653589793" $'Degrees: 180.00\n'
run_case "1.5707963267948966" $'Degrees: 90.00\n'
run_case "0" $'Degrees: 0.00\n'
run_case "1" $'Degrees: 57.30\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
