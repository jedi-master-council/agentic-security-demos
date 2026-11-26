# Demo 89: Tool-Schema Interpretation Divergence - Makefile

SHELL := /bin/bash
PYTHON := python3
DEMO_DIR := $(CURDIR)

.PHONY: help setup test demo clean

help:
	@echo "Demo 89: Tool-Schema Interpretation Divergence"
	@echo ""
	@echo "  make setup    # Verify Python (standard library only)"
	@echo "  make test     # Run all tests"
	@echo "  make demo     # Run the demonstration"
	@echo "  make clean    # Remove generated files"

setup:
	@echo "Setting up demo-89-schema-divergence..."
	@$(PYTHON) --version
	@mkdir -p $(DEMO_DIR)/results
	@echo "Setup complete (standard library only)."

test:
	@cd $(DEMO_DIR) && $(PYTHON) -m pytest tests/ -v --tb=short

demo: setup
	@echo "=== Demo 89: Tool-Schema Interpretation Divergence ==="
	@echo ""
	@cd $(DEMO_DIR) && $(PYTHON) student/divergence.py
	@echo ""
	@echo "Wrote results/divergence.json"

clean:
	@rm -rf $(DEMO_DIR)/results/ $(DEMO_DIR)/student/__pycache__ $(DEMO_DIR)/tests/__pycache__
