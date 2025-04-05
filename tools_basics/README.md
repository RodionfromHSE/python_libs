# Tools Basics

A Python library providing basic tools for data handling and visualization.

## Features

- **DataHandler**: Load and manage datasets from Hugging Face
- **Visualizer**: Create visualizations using matplotlib and bokeh
- **Helpers**: Utility functions for configuration and data saving

## Installation

```bash
pip install tools_basics
```

## Usage

```python
from tools_basics.data_handler import DataHandler
from tools_basics.visualizer import Visualizer
from tools_basics.helpers import get_config

# Load configuration
config = get_config("path/to/config.yaml")

# Initialize data handler and load data
data_handler = DataHandler(config)
train_df, test_df = data_handler.get_data()

# Visualize data
Visualizer.pretty_sample(train_df)
Visualizer.plot_series([train_df['text'].str.len()], ['Train Text Length'])
```

## Requirements

- Python 3.10+
- pandas
- numpy
- matplotlib
- datasets
- omegaconf
- tabulate
- bokeh