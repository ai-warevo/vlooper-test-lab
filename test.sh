#!/bin/bash
# Run existing simple test
result=$(python3 -c "from math_logic import add; print(add(2, 2))")

if [ "$result" -ne 4 ]; then
  echo "Simple Test Failed! Expected 4, got $result"
  exit 1
fi

echo "Simple Test Passed!"

# Run pytest suite
echo "Running pytest..."
pytest test_math_logic.py
if [ $? -eq 0 ]; then
  echo "All tests passed successfully!"
  exit 0
else
  echo "Pytest failed!"
  exit 1
fi