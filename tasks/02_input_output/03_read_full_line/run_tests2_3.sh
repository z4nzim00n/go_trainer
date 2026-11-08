#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "hello world" $'Line: hello world\n'
run_case "Go is fun" $'Line: Go is fun\n'
run_case "" $'Line: \n'
run_case "   " $'Line:    \n'
run_case_devnull ""

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
