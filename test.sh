#!/bin/bash
# Run comprehensive tests using pytest with coverage
export PYTHONPATH=.
pytest --cov=math_logic tests/test_math_logic.py
