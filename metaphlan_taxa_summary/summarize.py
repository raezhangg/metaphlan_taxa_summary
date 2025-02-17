import pandas as pd
import argparse

def summarize_taxa(meta_table_path):
    df = pd.read_csv(meta_table_path, sep='\t', skiprows=1) 
    taxa_column = df['clade_name']  
    unique_taxa = len(df) - 1 
    t_count = taxa_column[taxa_column.str.contains('t__')].count()
    s_count = taxa_column[taxa_column.str.contains('s__') & ~taxa_column.str.contains('t__')].count()
    g_count = taxa_column[taxa_column.str.contains('g__') & ~taxa_column.str.contains('s__')].count()
    f_count = taxa_column[taxa_column.str.contains('f__') & ~taxa_column.str.contains('g__')].count()
    o_count = taxa_column[taxa_column.str.contains('o__') & ~taxa_column.str.contains('f__')].count()
    c_count = taxa_column[taxa_column.str.contains('c__') & ~taxa_column.str.contains('o__')].count()
    p_count = taxa_column[taxa_column.str.contains('p__') & ~taxa_column.str.contains('c__')].count()
    k_count = taxa_column[taxa_column.str.contains('k__') & ~taxa_column.str.contains('p__')].count()

    total_count = t_count + s_count + g_count + f_count + o_count + c_count + p_count + k_count
    if total_count != unique_taxa:
        print(f"Warning: Sum of counts does not match the number of unique taxa.")

    return {
        'Unique Taxa': unique_taxa,
        't': t_count,
        's': s_count,
        'g': g_count,
        'f': f_count,
        'o': o_count,
        'c': c_count,
        'p': p_count,
        'k': k_count
    }

def main():
    parser = argparse.ArgumentParser(description='Summarize taxa from a MetaPhlAn table.')
    parser.add_argument('input_path', help='Path to the input MetaPhlAn table file')
    parser.add_argument('output_path', help='Path to the output summary file')
    args = parser.parse_args()

    summary = summarize_taxa(args.input_path)

    for key, value in summary.items():
        print(f'{key}: {value}')
    
    with open(args.output_path, 'w') as f:
        for key, value in summary.items():
            f.write(f'{key}: {value}\n')

if __name__ == '__main__':
    main()
