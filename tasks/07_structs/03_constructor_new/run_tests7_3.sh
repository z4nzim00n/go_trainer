#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "Alice 30" $'Name: Alice, Age: 30\n'
run_case "Bob 18" $'Name: Bob, Age: 18\n'
run_case "Eve 0" $'Name: Eve, Age: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
