# Custom Helpers

A small Python utility package providing helper functions for configuration management and import utilities.

## Installation

```bash
pip install custom_helpers
```

## Features

### Configuration Management

Load configuration from YAML files with `omegaconf`:

```python
from custom_helpers import get_config

# Load configuration file with automatic root_dir setting
config = get_config("path/to/conf.yaml")

# Or specify a custom root directory
config = get_config("path/to/conf.yaml", root="/custom/root/path")
```

### Python Path Utilities

Add the project root directory to the Python path:

```python
from custom_helpers import add_root_to_pythonpath

# Add the current directory to Python path
add_root_to_pythonpath()

# Add a parent directory to Python path (go up n levels)
add_root_to_pythonpath(n_up=1)

# Get the root directory path
root_dir = add_root_to_pythonpath(return_root=True)

# Print the added directory
add_root_to_pythonpath(verbose=True)
```

> **Note**: `add_root_to_pythonpath` is designed for script use and will raise an error if used in Jupyter/IPython environments.

## Requirements

- Python 3.10+
- omegaconf
