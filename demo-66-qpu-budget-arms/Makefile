# Demo 66: QPU Budget Arms - Makefile

SHELL := /bin/bash
PYTHON := python3
DEMO_DIR := $(CURDIR)

.PHONY: help setup test demo clean

help:
	@echo "Demo 66: QPU Budget Arms"
	@echo ""
	@echo "  make setup    # Verify Python (standard library only)"
	@echo "  make test     # Run all tests"
	@echo "  make demo     # Run the teaching demonstration"
	@echo "  make clean    # Remove generated files"

setup:
	@echo "Setting up demo-66-qpu-budget-arms..."
	@$(PYTHON) --version
	@mkdir -p $(DEMO_DIR)/results
	@echo "Setup complete (standard library only)."

test:
	@echo "Running tests for demo-66..."
	@cd $(DEMO_DIR) && $(PYTHON) -m pytest tests/ -v --tb=short

demo: setup
	@echo "=== Demo 66: QPU Budget Arms ==="
	@cd $(DEMO_DIR) && $(PYTHON) student/run_qpu_budget.py
	@echo "Wrote results/qpu_budget.json"

clean:
	@rm -rf $(DEMO_DIR)/results/
	@find $(DEMO_DIR) -name "__pycache__" -type d -prune -exec rm -rf {} +
	@find $(DEMO_DIR) -name "*.pyc" -delete
