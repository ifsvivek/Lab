"""Converted from Lab4.ipynb"""

import pandas as pd

df= pd.read_csv('data.csv')

def find_S_algorithm(df, target_attribute):
    positive_examples = df[df[target_attribute].isin([1, "Yes", True])]

    attributes = df.columns.tolist()
    attributes.remove(target_attribute)

    first_positive = positive_examples.iloc[0]
    h = {attr: first_positive[attr] for attr in attributes}

    for i, example in positive_examples.iterrows():
        for attr in attributes:
            if h[attr] != example[attr]:
                h[attr] = "?"
    return h

hypothesis = find_S_algorithm(df, "Job offer")
print(list(hypothesis.values()))