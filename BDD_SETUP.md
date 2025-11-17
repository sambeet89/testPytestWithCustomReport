# Pytest-BDD Setup Documentation

## Overview

This project uses **pytest-bdd** (Behavior-Driven Development) to write tests in Gherkin format. The setup requires two essential files that work together to make BDD tests work.

## Project Structure

```
prsc_pytest/
├── pytest.ini                 # Pytest configuration
├── tests/
│   ├── conftest.py            # ⚠️ REQUIRED: Imports step definitions
│   ├── test_common_step.py    # ⚠️ REQUIRED: Registers feature files
│   ├── features/
│   │   └── test_one.feature   # Gherkin feature file
│   └── steps/
│       └── test_type1.py      # Step definition implementations
```

## Why Two Files Are Required

### 1. `conftest.py` - Step Definitions (The "HOW")

**Purpose:** Makes step definitions available to all test files.

**What it does:**
- Imports all step definitions from the `steps/` directory
- Automatically loaded by pytest before any test files
- Makes step definitions globally available across all test files

**File content:**
```python
from .steps.test_type1 import *
```

**Why it's needed:**
- Without it, pytest-bdd cannot find the step implementations
- Error: `StepDefinitionNotFoundError: Step definition is not found`
- Step definitions define **what code runs** when a Gherkin step is executed

**Example step definition (from `steps/test_type1.py`):**
```python
from pytest_bdd import given, parsers, when, then

@given("we are executing background")
def step_background():
    print("executing background")

@when(parsers.parse('the testdata is {data}'))
def step_testdata(data):
    print(f'executing-the testdata is {data} ')
```

---

### 2. `test_common_step.py` - Feature File Registration (The "WHAT")

**Purpose:** Tells pytest-bdd which feature files to process and convert into test cases.

**What it does:**
- Calls `scenarios()` to register Gherkin feature files
- Converts `.feature` files into pytest test cases
- Must follow pytest naming convention: `test_*.py` or `*_test.py`

**File content:**
```python
from pytest_bdd import scenarios

scenarios('features/test_one.feature')
```

**Why it's needed:**
- Without it, pytest collects **0 tests** (doesn't know which features to process)
- Tells pytest-bdd **which feature files** to convert into test cases
- Each test file can register one or more feature files

**What happens:**
- `scenarios()` reads the `.feature` file
- Parses Gherkin syntax (Given/When/Then)
- Creates pytest test functions for each scenario
- Matches steps to step definitions imported in `conftest.py`

---

## How They Work Together

```
┌─────────────────────────────────────────────────────────────┐
│                    pytest -v                                 │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Load conftest.py                                   │
│  └─> Imports step definitions from steps/test_type1.py       │
│      (Makes "how" available)                                │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 2: Discover test files (test_*.py)                    │
│  └─> Finds test_common_step.py                             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 3: Execute test_common_step.py                        │
│  └─> Calls scenarios('features/test_one.feature')          │
│      (Tells pytest-bdd "what" to process)                   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 4: Parse feature file                                 │
│  └─> Reads test_one.feature                                 │
│      Creates test cases from scenarios                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 5: Match steps to definitions                         │
│  └─> For each step in feature file:                        │
│      - Finds matching step definition (from conftest.py)   │
│      - Executes the Python function                         │
└─────────────────────────────────────────────────────────────┘
```

## Key Points

### ✅ Both Files Are Required

| File | Purpose | What Happens Without It |
|------|---------|------------------------|
| `conftest.py` | Imports step definitions | ❌ `StepDefinitionNotFoundError` - pytest-bdd can't find step implementations |
| `test_common_step.py` | Registers feature files | ❌ `collected 0 items` - pytest doesn't know which features to process |

### 🔄 Alternative Approach (Not Recommended)

You could import step definitions directly in `test_common_step.py`:

```python
from pytest_bdd import scenarios
from .steps.test_type1 import *  # Import here instead

scenarios('features/test_one.feature')
```

**Why `conftest.py` is better:**
- ✅ Standard pytest convention
- ✅ Step definitions available to multiple test files
- ✅ Cleaner separation of concerns
- ✅ Scales better as project grows

## File Naming Requirements

### Critical: Test File Must Follow Naming Convention

- ✅ `test_common_step.py` - **Will be discovered**
- ✅ `test_anything.py` - **Will be discovered**
- ✅ `common_step_test.py` - **Will be discovered**
- ❌ `common_step.py` - **Won't be discovered** (no `test_` prefix/suffix)

Pytest only discovers files matching `test_*.py` or `*_test.py` patterns.

## Gherkin Feature File Format

The feature file (`test_one.feature`) uses Gherkin syntax:

```gherkin
Feature: this is a test festure

  Background: test bck ground
    Given we are executing background

  @regression
  Scenario Outline:
    Given we ar ein the testoutline with example
    When the testdata is <data>
    Then lets print the output
    Examples:
      |data|
      |10|
      |20|
```

**Important syntax notes:**
- Use `Examples:` (not `@example:`)
- Scenario Outline uses `<variable>` in steps, but step definitions use `{variable}` with `parsers.parse()`
- Background steps run before each scenario

## Step Definition Syntax

### Using `parsers.parse()` for Parameterized Steps

When a step has parameters (like `<data>` in Scenario Outline):

**Feature file:**
```gherkin
When the testdata is <data>
```

**Step definition:**
```python
@when(parsers.parse('the testdata is {data}'))  # Note: {data} not <data>
def step_testdata(data):
    print(f'executing-the testdata is {data} ')
```

**Key difference:**
- Feature file: `<data>` (Gherkin syntax)
- Step definition: `{data}` (parse library syntax)

### Function Names Must Be Unique

❌ **Wrong:** All functions named `step_impl`
```python
@given("step 1")
def step_impl():  # This gets overwritten
    pass

@given("step 2")
def step_impl():  # This overwrites the previous one
    pass
```

✅ **Correct:** Unique function names
```python
@given("step 1")
def step_one():
    pass

@given("step 2")
def step_two():
    pass
```

## Running Tests

```bash
# Activate virtual environment
source env/bin/activate

# Run all tests
pytest -v

# Run with more output
pytest -v -s

# Run specific test
pytest -v tests/test_common_step.py::test_[10]
```

## Troubleshooting

### Problem: `collected 0 items`
**Solution:** Check that your test file follows naming convention (`test_*.py` or `*_test.py`)

### Problem: `StepDefinitionNotFoundError`
**Solution:** Ensure `conftest.py` imports step definitions, or import them in your test file before calling `scenarios()`

### Problem: `FileNotFoundError` for feature file
**Solution:** Check the path in `scenarios()` - it should be relative to the test file location

### Problem: Gherkin syntax errors
**Solution:** 
- Use `Examples:` not `@example:`
- Ensure proper indentation
- Check for typos in keywords (Given/When/Then)

## Summary

**Both files are essential:**

1. **`conftest.py`** = The "HOW" (step implementations)
2. **`test_common_step.py`** = The "WHAT" (which features to test)

They work together to make pytest-bdd function:
- `conftest.py` provides the step definitions
- `test_common_step.py` tells pytest-bdd which features to process
- Together, they convert Gherkin scenarios into executable pytest tests

