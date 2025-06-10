import pandas as pd

df = pd.read_csv("Lab4.csv")


def find_s(df, target_col):
    positive_examples = df[df[target_col] == "Yes"]
    attributes = df.columns.tolist()
    attributes.remove(target_col)

    hypothesis = positive_examples.iloc[0][attributes].tolist()

    for _, example in positive_examples.iterrows():
        for i, attr in enumerate(attributes):
            if hypothesis[i] != example[attr]:
                hypothesis[i] = "?"

    return hypothesis


hypothesis = find_s(df, "Job offer")
print(hypothesis)
