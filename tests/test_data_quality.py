import pandas as pd
import pytest
from scripts.data_cleaning import clean_data

class TestDataQuality:
    @pytest.fixture
    def sample_data(self, tmp_path):
        input_file = tmp_path / "test_data.csv"
        pd.DataFrame({
            'math_score': [80, None, 110],
            'science_score': [75, 85, None],
            'attendance': [0.9, 0.8, 0.7]
        }).to_csv(input_file, index=False)
        return input_file

    def test_clean_data(self, sample_data, tmp_path):
        output_file = tmp_path / "output.csv"
        result = clean_data(sample_data, output_file)
        
        assert len(result) == 1  # Only 1 valid row
        assert 0 <= result.iloc[0]['total_score'] <= 100
        assert os.path.exists(output_file)
