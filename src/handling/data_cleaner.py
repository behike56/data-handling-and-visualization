"""
    データのチェックの例:
        データの最大値・最小値を確認し、期待する範囲外の値がないか確認する
        欠損値の有無を確認する
        データの種類を確認し、意図しない値や表記揺れがないか確認する
        データの分布を確認し、不自然な点がないか確認する
        データの重複を確認し、本来なら発生しないような不自然な重複がないか確認する

    想定されるデータ:
        (1) 範囲外の値: 身長のデータなのに、負の値になっている
        (2) 欠損値: 体重のデータが欠損している（ NaN は「データがないこと」を表す値）
        (3) 表記揺れ: 部活動のデータに、同じような意味の値がある（ "無所属" と "所属なし" ）
"""

import pandas as pd
from pnadas import DataFrame

# データの読み込み
df = pd.read_csv("dataset/physical_measurement_dirty.csv")
df


def delete_row(column: str, value: int, df: DataFrame) -> DataFrame:
    """ columnがvalue以下の行だけを選択
    """
    return df[df[column] <= value]


def search_loss(df: DataFrame) -> DataFrame:
    return df.info()


def search_row_loss(column: str, df: DataFrame) -> DataFrame:
    return df[column].isna()


def delete_loss_row(column: str, df: DataFrame) -> DataFrame:
    return df.dropna(subset=[column])



