# Business Profit Calculator

This repository contains simple tools for calculating profit and gross margin.

## HTML Tools

The files `EVA_GP_Simulator_Final (1).html` and `利潤試算表.html` can be opened directly in a web browser. They provide interactive tables for entering item prices and costs with automatic gross profit calculations.

## Python Script

`profit_calculator.py` is a command-line tool for similar calculations.

### Usage

Run interactively:

```bash
python profit_calculator.py
```

You will be prompted to enter item names, prices and costs. Leave the name blank to finish input. A summary report will be printed, and you can optionally export results to CSV using `--export`.

Run with a CSV file:

```bash
python profit_calculator.py --csv data.csv --export result.csv
```

The input CSV should contain the columns `name`, `price`, `cost`, and an optional `note` column. The script will read the file, calculate profit and margin for each item, print a report, and write the results to `result.csv`.
