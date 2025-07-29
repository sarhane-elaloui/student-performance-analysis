import pandas as pd
import os

def test_data_integrity():
    """Validate processed data meets expectations"""
    df = pd.read_csv("data/processed/clean_data.csv")
    assert not df.empty, "Processed data is empty"
    assert {'student_id', 'math_score', 'science_score'}.issubset(df.columns)
    assert df['math_score'].between(0, 100).all()
