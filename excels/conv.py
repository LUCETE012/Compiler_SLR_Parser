import pandas as pd

df = pd.read_excel('excels/Reduction.xlsx', index_col=0)

ACTION = {}

for row_idx, row in df.iterrows():
    for col_name, value in row.items():
        if pd.notna(value): 
            action = value[0]
            number = value[1:]
            if row_idx not in ACTION:
                ACTION[row_idx] = {}
            ACTION[row_idx][col_name] = (action, number)

for state, transitions in ACTION.items():
    for token, (action, number) in transitions.items():
        print(f'ACTION[{state}][{token}] = ("{action}", {number})')
