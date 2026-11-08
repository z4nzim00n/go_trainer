#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "hello world" $'2\n'
run_case "" $'0\n'
run_case "  a  b   c " $'3\n'
run_case "one" $'1\n'
run_case $'a\tb\nc' $'3\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
