import matplotlib.pyplot as plt
import seaborn as sns

def save_grade_distribution(df_path: str, output_path: str):
    df = pd.read_csv(df_path)
    plt.figure(figsize=(10,6))
    sns.histplot(data=df, x='math_score', bins=20, kde=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
