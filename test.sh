#!/bin/bash
# Проверяем, что 2 + 2 = 4
result=$(python3 -c "from math_logic import add; print(add(2, 2))")

if [ "$result" -eq 4 ]; then
  echo "Test Passed!"
  exit 0
else
  echo "Test Failed! Expected 4, got $result"
  exit 1
fi