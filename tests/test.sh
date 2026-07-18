#!/bin/bash
set -uo pipefail

mkdir -p /logs/verifier

pytest /tests/test_outputs.py \
  -rA \
  --ctrf /logs/verifier/ctrf.json
test_status=$?

if [ "$test_status" -eq 0 ]; then
  printf '1\n' > /logs/verifier/reward.txt
else
  printf '0\n' > /logs/verifier/reward.txt
fi

exit "$test_status"
