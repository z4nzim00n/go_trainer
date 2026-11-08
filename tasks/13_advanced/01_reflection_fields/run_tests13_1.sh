#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "Alice 30" $'Name=Alice Age=30\n'
run_case "Bob 0" $'Name=Bob Age=0\n'
run_case "Eve -1" $'Name=Eve Age=-1\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
