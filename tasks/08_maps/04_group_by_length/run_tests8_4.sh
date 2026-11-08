#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "a cat dog bee" $'1: a\n3: bee cat dog\n'
run_case "go" $'2: go\n'
run_case "dd cc a bbb" $'1: a\n2: cc dd\n3: bbb\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
