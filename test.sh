#!/bin/bash
# Проверяем функции из math_logic.py

echo "Testing add(2, 2)..."
result=$(python3 -c "from math_logic import add; print(add(2, 2))")
if [ "$result" == "4.0" ] || [ "$result" == "4" ]; then
  echo "  OK"
else
  echo "  FAILED! Expected 4, got $result"
  exit 1
fi

echo "Testing sqrt(9)..."
result=$(python3 -c "from math_logic import sqrt; print(sqrt(9))")
if [ "$result" == "3.0" ]; then
  echo "  OK"
else
  echo "  FAILED! Expected 3.0, got $result"
  exit 1
fi

echo "Testing pow(2, 3)..."
result=$(python3 -c "from math_logic import pow; print(pow(2, 3))")
if [ "$result" == "8.0" ]; then
  echo "  OK"
else
  echo "  FAILED! Expected 8.0, got $result"
  exit 1
fi

echo "All manual tests passed!"
exit 0
