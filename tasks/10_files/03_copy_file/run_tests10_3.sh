#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f f1.txt f2.txt' EXIT
printf 'hello\n' > f1.txt
run_case "f1.txt f2.txt" $'Copied: hello\n'
diff f1.txt f2.txt
printf 'a b\n' > f1.txt
run_case "f1.txt f2.txt" $'Copied: a b\n'
diff f1.txt f2.txt
run_case "missing.txt f2.txt" $'Error: cannot read source\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
