#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "21.5" $'Temp: 21.50°C\n'
run_case "-5" $'Temp: -5.00°C\n'
run_case "0" $'Temp: 0.00°C\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
