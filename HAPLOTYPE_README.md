# Haplotype Data Organizer

This repository contains a Python script that organizes genetic data by haplotype groups.

## Description

The `organize_haplotype_data.py` script reads data from `data_analysis.json` and reorganizes it by haplotype (Hap0 through Hap4). It extracts and combines the fields 'x', 'y', 'a', and 'data_1' for each haplotype group.

## Usage

1. Ensure you have a `data_analysis.json` file in the same directory as the script
2. Run the script:
   ```bash
   python3 organize_haplotype_data.py
   ```

## Input File Format

The `data_analysis.json` file should contain a JSON object with a "data" array:

```json
{
  "data": [
    {
      "hap": "Hap0",
      "x": [1, 2, 3],
      "y": [4, 5, 6],
      "a": [7, 8, 9],
      "data_1": {"sample": "value1", "count": 10}
    },
    ...
  ]
}
```

## Output

The script creates `organized_haplotype_data.json` with the following structure:

```json
{
  "Hap0": {
    "x": [...],
    "y": [...],
    "a": [...],
    "data_1": { ... }
  },
  "Hap1": { ... },
  "Hap2": { ... },
  "Hap3": { ... },
  "Hap4": { ... }
}
```

## Features

- Combines multiple entries for the same haplotype
- Merges arrays (x, y, a) by extending them
- Merges data_1 objects by updating keys
- Provides detailed error handling
- Shows processing summary with counts

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)