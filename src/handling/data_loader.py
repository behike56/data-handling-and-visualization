import pandas as pd

df = pd.DataFrame(
    [["Alice", 17], ["Bob", 24], ["Carol", 29]],
    index=[10, 20, 30],
    columns=["Name", "Age"],
)

def test_iloc(df: DataFrame):
    """ilocを使うと、行番号・列番号を使って範囲指定ができます。
       主な使い方は、行名・列名を使うlocとほぼ同じです。
    """
    print(df.loc[10])
    print("----")
    print(df.iloc[0])
    
    print(df.loc[:, "Name"])
    print("----")
    print(df.iloc[:, 0])
    
    print(df.loc[[20, 30], ["Name", "Age"]])
    print("----")
    print(df.iloc[[1, 2], [0, 1]])
    
    """
        Age   Name
        30   29  Carol
        20   24    Bob
        ----
            Age   Name
        30   29  Carol
        20   24    Bob
    """
    print(df.loc[[30, 20], ["Age", "Name"]])
    print("----")
    print(df.iloc[...])
    
    result = df.iloc[[2, 0], [0, 1]]
    """
        Name	Age
        30	Carol	29
        10	Alice	17
    """