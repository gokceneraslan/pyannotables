# -*- coding: utf-8 -*-

def tables():
    import pandas as pd
    
    from pathlib import Path
    from pkg_resources import resource_listdir, resource_filename

    __data_files = resource_listdir('pyannotables.data', '')
    __full_data_files = {Path(filename).stem.split('.')[0].split('datafile_')[1]: resource_filename('pyannotables.data', filename) for filename in __data_files if filename.startswith('datafile_')}
    
    t = {key: pd.read_pickle(val) for key, val in __full_data_files.items()}
    
    return t


def homology_convert(gene_symbols, source_organism, target_organism):
    import pandas as pd
    
    t = tables()
    homology = t['homology']
    homology_grouped_genesymbol = t['homology_grouped_genesymbol']    
    
    genes_dict =  homology[(homology.tax_name == source_organism) & homology.gene_symbol.isin(gene_symbols)].set_index('gene_symbol').to_dict()['homology_id']
    
    homology2target = homology_grouped_genesymbol[target_organism].to_dict()
    res_genes = {symbol: homology2target[h] for symbol, h in genes_dict.items()}
    
    df = pd.DataFrame({source_organism: list(res_genes.keys())})
    df[target_organism] = res_genes.values()
    df = df[~df[target_organism].isnull()]
    df = df.explode(target_organism).reset_index(drop=True)

    return df