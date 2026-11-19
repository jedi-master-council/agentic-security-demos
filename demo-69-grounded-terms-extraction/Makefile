# Demo 69: Grounded Terms Extraction - Makefile

SHELL := /bin/bash
PYTHON := python3
DEMO_DIR := $(CURDIR)

.PHONY: help setup test demo clean

help:
	@echo "Demo 69: Grounded Terms Extraction"
	@echo ""
	@echo "  make setup    # Verify Python (standard library only)"
	@echo "  make test     # Run all tests"
	@echo "  make demo     # Run the teaching demonstration"
	@echo "  make clean    # Remove generated files"

setup:
	@echo "Setting up demo-69-grounded-terms-extraction..."
	@$(PYTHON) --version
	@mkdir -p $(DEMO_DIR)/results
	@echo "Setup complete (standard library only)."

test:
	@echo "Running tests for demo-69..."
	@cd $(DEMO_DIR) && $(PYTHON) -m pytest tests/ -v --tb=short

demo: setup
	@echo "=== Demo 69: Grounded Terms Extraction ==="
	@cd $(DEMO_DIR) && $(PYTHON) student/run_grounding.py
	@echo "Wrote results/grounding.json"

clean:
	@rm -rf $(DEMO_DIR)/results/
	@find $(DEMO_DIR) -name "__pycache__" -type d -prune -exec rm -rf {} +
	@find $(DEMO_DIR) -name "*.pyc" -delete
