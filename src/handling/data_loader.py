""" データのロード

    - データの入出力
        CSVやExcel、DBなど、さまざまな形式のデータソースから表形式のデータを読み込めます。また、pandasで処理したデータを、各形式のファイルに書き込めます。
    - データの絞り込み
        「列Aが 100 以上の行だけを抽出する」など、指定した条件に合致するデータだけを絞り込めます。
    - データのクリーニング
        「身長のデータなのに負の値になっている」といった異常な値をチェック・修正したり、欠損値を補間・削除するなど、「おかしなデータ」を分析可能な形に整備できます。
    - データの集約
        「店舗ごとの売り上げの合計値を計算する」「ユーザの年齢ごとに契約日数の平均値を計算する」など、グループごとに特定の処理を適用できます。
    - データの統合
        複数のデータをひとつのデータに統合します。単純な連結のほか、SQLのJOINのような異なる種類のデータも結合できます。
    - データの分析・可視化
        各列の基本統計量を計算したり、棒グラフや散布図などいろいろなグラフを作成できます。
"""
import pandas as pd

# pandas.DataFrame
df = pd.DataFrame(
    [["Alice", 17], ["Bob", 24], ["Carol", 29]],
    index=[10, 20, 30],
    columns=["Name", "Age"],
)

# 列、pandas.Series
df["Name"]

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
