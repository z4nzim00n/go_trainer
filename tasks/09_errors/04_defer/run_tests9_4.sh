#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "hive" $'open hive\nwork\nclose\n'
run_case "go" $'open go\nwork\nclose\n'
run_case "x" $'open x\nwork\nclose\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
