import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_grade_distribution(data_path: str, save_path: str):
    """Generates and saves grade distribution plots"""
    df = pd.read_csv(data_path)
    
    plt.figure(figsize=(12,6))
    
    # Subplot 1: Histogram
    plt.subplot(1,2,1)
    sns.histplot(data=df, x='total_score', bins=20, kde=True)
    
    # Subplot 2: Boxplot
    plt.subplot(1,2,2)
    sns.boxplot(data=df[['math_score', 'science_score']])
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
