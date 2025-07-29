import pandas as pd
from pathlib import Path

def clean_data(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Cleans student performance data:
    - Removes missing values
    - Calculates total score
    - Filters invalid grades
    """
    df = pd.read_csv(input_path)
    
    # Data validation
    assert {'math_score', 'science_score'}.issubset(df.columns), "Missing required columns"
    
    # Processing pipeline
    df = (df
          .dropna()
          .assign(total_score=lambda x: (x['math_score'] + x['science_score']) / 2)
          .query("0 <= math_score <= 100 and 0 <= science_score <= 100")
          .sort_values('total_score', ascending=False)
    )
    
    # Save processed data
    Path(output_path).parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    clean_data(
        input_path="../data/raw/students.csv",
        output_path="../data/processed/cleaned_students.csv"
    )
