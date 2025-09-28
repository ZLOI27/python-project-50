# Hexlet tests and linter status:
[![Actions Status](https://github.com/ZLOI27/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ZLOI27/python-project-50/actions)
[![Python CI](https://github.com/ZLOI27/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/ZLOI27/python-project-50/actions/workflows/pyci.yml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ZLOI27_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=ZLOI27_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ZLOI27_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=ZLOI27_python-project-50)


# gendiff configuration file diff tool

gendiff is a tool for easily comparing configuration files and displaying the differences between them in various formats. With gendiff, you can:

- Get diffs in different formats: from the human-readable stylish format to the simple plain format, and even json.
- Work with different file types, supporting YAML and JSON formats.
- Easily integrate with other tools and scripts for automatic configuration comparisons.

### Features:
- Simple command-line interface.
- Support for extendable output formats.
- Comparison of nested data structures.
- Suitable for working with any type of configuration or data files.

### Supported Output Formats:
- *Stylish*: Beautiful and human-readable output.
- *Plain*: Simple text-based output.
- *JSON*: Output in JSON format for integration with other tools.

# Installation Guide for gendiff

Follow the steps below to set up and install the gendiff project on your local machine.

### Clone the Repository

Start by cloning the repository from GitHub:

```bash
https://github.com/ZLOI27/python-project-50.git
```

### Installation
Navigate into the project directory and install the required dependencies:

```bash
cd python-project-50
```
```bash
make install
```

### Install the package globally
```bash
make build
```
```
make package-install
```

### Run the tool

```bash
gendiff -f <format> <first_file> <second_file>
```

Replace `<first_file>`, `<second_file>`, and `<format>` with the appropriate file paths and desired output format (such as `stylish`, `plain`, or `json`).

## Tests

### Run the tests
```bash
make test
```

### Run the tests with coverage, run with test-files and ruff check
```bash
make full-check
```

### Asciinema gendiff of two files
[![asciicast](https://asciinema.org/a/0naRf02Fr7ymDJ0kPU9AUXnbh.svg)](https://asciinema.org/a/0naRf02Fr7ymDJ0kPU9AUXnbh)

### Asciinema gendiff of two files for .yaml
[![asciicast](https://asciinema.org/a/L4rqd8r2dLX1dWcGifc5SFHlA.svg)](https://asciinema.org/a/L4rqd8r2dLX1dWcGifc5SFHlA)

### Asciinema gendiff format stylish
[![asciicast](https://asciinema.org/a/UcwLpdkKRdO1xMTVAh6NN2F2S.svg)](https://asciinema.org/a/UcwLpdkKRdO1xMTVAh6NN2F2S)

### Asciinema gendiff format plain
[![asciicast](https://asciinema.org/a/406KH8KdnWPyk14AtZLGKGdMg.svg)](https://asciinema.org/a/406KH8KdnWPyk14AtZLGKGdMg)

### Asciinema gendiff format json
[![asciicast](https://asciinema.org/a/dQTj1PLuTwLxFFj5ca1uFufG2.svg)](https://asciinema.org/a/dQTj1PLuTwLxFFj5ca1uFufG2)
