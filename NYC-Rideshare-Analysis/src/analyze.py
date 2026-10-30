"""Car sales coursework reconstruction. Usage: python src/analyze.py --input data/car_sales.csv"""
import argparse
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', default='data/car_sales.csv')
    p.add_argument('--output', default='results')
    args = p.parse_args()
    source = Path(args.input)
    if not source.exists():
        raise SystemExit(f'Dataset missing: {source}. Add your original CSV before running.')
    out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(source)
    df.columns = df.columns.str.strip()
    initial = len(df)
    duplicates = int(df.duplicated().sum())
    df = df.drop_duplicates()
    df.to_csv(out/'cleaned_data.csv', index=False)
    lines = [f'Original rows: {initial}', f'Duplicate rows removed: {duplicates}', f'Rows after deduplication: {len(df)}', f'Columns: {list(df.columns)}', '', 'Missing values:', df.isna().sum().to_string(), '', 'Summary:', df.describe(include='all').to_string()]
    (out/'summary.txt').write_text('\n'.join(lines), encoding='utf-8')
    numeric = df.select_dtypes(include='number')
    if not numeric.empty:
        numeric.hist(figsize=(12, 8), bins=25)
        plt.tight_layout(); plt.savefig(out/'numeric_distributions.png', dpi=150); plt.close('all')
        if numeric.shape[1] >= 2:
            corr = numeric.corr()
            fig, ax = plt.subplots(figsize=(9,7))
            im = ax.imshow(corr, vmin=-1, vmax=1, cmap='coolwarm')
            ax.set_xticks(range(len(corr))); ax.set_xticklabels(corr.columns, rotation=65, ha='right')
            ax.set_yticks(range(len(corr))); ax.set_yticklabels(corr.columns)
            fig.colorbar(im, ax=ax); fig.tight_layout(); fig.savefig(out/'correlations.png', dpi=150); plt.close(fig)
    print('Analysis saved to', out)

if __name__ == '__main__': main()
