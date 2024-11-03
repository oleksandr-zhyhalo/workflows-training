# Python Data Processor

![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/oleksandr-zhyhalo/a9666265a2fd6c15ffbdf8d49e2eb903/raw/coverage.json)

A simple Python application that processes numerical data and generates statistical results.

## Features

- Process lists of numbers
- Calculate basic statistics (sum, average)
- Save results to JSON files
- Comprehensive test coverage
- Automated CI/CD pipeline

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from app import DataProcessor

processor = DataProcessor()
results = processor.process_data([1, 2, 3, 4, 5])
processor.save_results(results)
```

## Testing

Run tests with coverage:

```bash
pytest --cov=./
```

## CI/CD

This repository uses GitHub Actions for:
- Automated testing
- Code coverage reporting
- Artifact generation
