# TOPSIS
A pypi library created using python to implement TOPSIS

## Overview

The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) is a multi-criteria decision analysis method, which was originally developed by Ching-Lai Hwang and Yoon in 1981 with further developments by Yoon in 1987, and Hwang, Lai and Liu in 1993.TOPSIS is based on the concept that the chosen alternative should have the shortest geometric distance from the positive ideal solution (PIS) and the longest geometric distance from the negative ideal solution (NIS).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the library.

```bash
pip install Topsis_Saiyam_101917188
```

## Usage

```python
import Topsis_Saiyam_101917188 as tp

# Create a TOPSIS class
# Syntax
# t = tp.topsis(INPUT_FILENAME,WEIGHT_STRING,IMPACT_STRING,OUTPUT_FILENAME)

# Example
t = tp.topsis("data.xlsx", "1,1,1,2,1", "+,-,-,+,-", "output.csv")

#Calculate TOPSIS
t.calculate()
```

## Parameters for Initialization

### INPUT_FILENAME
The input file (with .xlsx extension) which contains the data to be processed.

### WEIGHT_STRING
Weight for each indicator in the form of a string (seperated by commas).  
E.g. "5,4,6,2" for 4 indicators.

### IMPACT_STRING
Impact of each indicator in the form of a string (seperated by commas).  
E.g. "+,-,+,+" for 4 indicators.

### OUTPUT_FILENAME
The filename of output file in .csv format.  
E.g. "output.csv"

## Outputs

### 101917188-data.csv
Creates a csv file from the given .xlsx file.

### 101917188-output.csv
Creates .csv file with the TOPSIS score and rank columns.

## License
[MIT](https://choosealicense.com/licenses/mit/)
