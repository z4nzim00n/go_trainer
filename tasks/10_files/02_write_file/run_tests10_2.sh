#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f out.txt' EXIT
run_case "out.txt hello" $'Saved: hello\n'
diff <(printf 'hello\n') out.txt
run_case "out.txt Go" $'Saved: Go\n'
diff <(printf 'Go\n') out.txt

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
