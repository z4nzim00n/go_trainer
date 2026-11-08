#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "Bob Acme" $'Name: Bob, Company: Acme\n'
run_case "Ann Globex" $'Name: Ann, Company: Globex\n'
run_case "Eve Initech" $'Name: Eve, Company: Initech\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
