import math
import sys
import re
import pandas as pd

def main():
    if len(sys.argv) != 3:
        print('usage: duplicate_columns.py single_filename columns_filename')
        exit(1)
    single_name = sys.argv[1]
    columns = sys.argv[2]
    df = pd.read_excel(single_name, sheet_name=0)
    lines = []
    with open(columns) as f:
        lines = f.read().splitlines()
    columns = list(df) 
    for col in columns:
        if col in lines:
            loc = df.columns.get_loc(col)
            df.insert(loc + 1, col + '_CLUSTER', df[col])
    df.to_excel('duplicated_' + single_name, index_label=None, index=False)


if __name__ == '__main__':
    main()
