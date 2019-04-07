

```python
from pathlib import Path
import os

import pandas as pd

from pyensembl import EnsemblRelease, genome_for_reference_name
from pyensembl.species import human, mouse
```


```python
def fetch_genes_and_transcripts(release, species, datadir=Path('data')):
    er = EnsemblRelease(release=release, species=species)
    er.download()
    er.index()

    genes = er.genes()
    tx = er.transcripts()

    gdf = pd.DataFrame([x.to_dict() for x in genes])
    gdf = gdf[['gene_id', 'gene_name', 'contig', 'start', 'end', 'strand', 'biotype']]
    gdf.set_index('gene_id', inplace=True)

    tdf = pd.DataFrame([x.to_dict() for x in tx])
    tdf = tdf[['gene_id', 'transcript_id', 'transcript_name']]
    tdf.set_index('transcript_id', inplace=True)

    os.makedirs(datadir, exist_ok=True)
    gdf.to_csv(datadir / f'{species.latin_name}-ensembl{release}-{ref}.csv.xz')
    tdf.to_csv(datadir / f'{species.latin_name}-ensembl{release}-{ref}-tx2gene.csv.xz')

    return gdf, tdf
```

## Human annotations

### GRCh38


```python
release = 95
species = human
ref = human.which_reference(release)
gdf, tdf = fetch_genes_and_transcripts(release, species)
```

    INFO:pyensembl.sequence_data:Loaded sequence dictionary from /Users/gokcen/Library/Caches/pyensembl/GRCh38/ensembl95/Homo_sapiens.GRCh38.cdna.all.fa.gz.pickle
    INFO:pyensembl.sequence_data:Loaded sequence dictionary from /Users/gokcen/Library/Caches/pyensembl/GRCh38/ensembl95/Homo_sapiens.GRCh38.ncrna.fa.gz.pickle
    INFO:pyensembl.sequence_data:Loaded sequence dictionary from /Users/gokcen/Library/Caches/pyensembl/GRCh38/ensembl95/Homo_sapiens.GRCh38.pep.all.fa.gz.pickle



```python
gdf.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gene_name</th>
      <th>contig</th>
      <th>start</th>
      <th>end</th>
      <th>strand</th>
      <th>biotype</th>
    </tr>
    <tr>
      <th>gene_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ENSG00000000003</th>
      <td>TSPAN6</td>
      <td>X</td>
      <td>100627109</td>
      <td>100639991</td>
      <td>-</td>
      <td>protein_coding</td>
    </tr>
    <tr>
      <th>ENSG00000000005</th>
      <td>TNMD</td>
      <td>X</td>
      <td>100584802</td>
      <td>100599885</td>
      <td>+</td>
      <td>protein_coding</td>
    </tr>
    <tr>
      <th>ENSG00000000419</th>
      <td>DPM1</td>
      <td>20</td>
      <td>50934867</td>
      <td>50958555</td>
      <td>-</td>
      <td>protein_coding</td>
    </tr>
    <tr>
      <th>ENSG00000000457</th>
      <td>SCYL3</td>
      <td>1</td>
      <td>169849631</td>
      <td>169894267</td>
      <td>-</td>
      <td>protein_coding</td>
    </tr>
    <tr>
      <th>ENSG00000000460</th>
      <td>C1orf112</td>
      <td>1</td>
      <td>169662007</td>
      <td>169854080</td>
      <td>+</td>
      <td>protein_coding</td>
    </tr>
  </tbody>
</table>
</div>




```python
tdf.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gene_id</th>
      <th>transcript_name</th>
    </tr>
    <tr>
      <th>transcript_id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ENST00000000233</th>
      <td>ENSG00000004059</td>
      <td>ARF5-201</td>
    </tr>
    <tr>
      <th>ENST00000000412</th>
      <td>ENSG00000003056</td>
      <td>M6PR-201</td>
    </tr>
    <tr>
      <th>ENST00000000442</th>
      <td>ENSG00000173153</td>
      <td>ESRRA-201</td>
    </tr>
    <tr>
      <th>ENST00000001008</th>
      <td>ENSG00000004478</td>
      <td>FKBP4-201</td>
    </tr>
    <tr>
      <th>ENST00000001146</th>
      <td>ENSG00000003137</td>
      <td>CYP26B1-201</td>
    </tr>
  </tbody>
</table>
</div>



### GRCh37


```python
release = 75
species = human
ref = human.which_reference(release)
gdf, tdf = fetch_genes_and_transcripts(release, species)
```

    INFO:pyensembl.sequence_data:Loaded sequence dictionary from /Users/gokcen/Library/Caches/pyensembl/GRCh37/ensembl75/Homo_sapiens.GRCh37.75.cdna.all.fa.gz.pickle
    INFO:pyensembl.sequence_data:Loaded sequence dictionary from /Users/gokcen/Library/Caches/pyensembl/GRCh37/ensembl75/Homo_sapiens.GRCh37.75.ncrna.fa.gz.pickle
    INFO:pyensembl.sequence_data:Loaded sequence dictionary from /Users/gokcen/Library/Caches/pyensembl/GRCh37/ensembl75/Homo_sapiens.GRCh37.75.pep.all.fa.gz.pickle


## Mouse annotations

### GRCm38


```python
release = 95
species = mouse
ref = human.which_reference(release)
gdf, tdf = fetch_genes_and_transcripts(release, species)
```

    INFO:pyensembl.sequence_data:Loaded sequence dictionary from /Users/gokcen/Library/Caches/pyensembl/GRCm38/ensembl95/Mus_musculus.GRCm38.cdna.all.fa.gz.pickle
    INFO:pyensembl.sequence_data:Loaded sequence dictionary from /Users/gokcen/Library/Caches/pyensembl/GRCm38/ensembl95/Mus_musculus.GRCm38.ncrna.fa.gz.pickle
    INFO:pyensembl.sequence_data:Loaded sequence dictionary from /Users/gokcen/Library/Caches/pyensembl/GRCm38/ensembl95/Mus_musculus.GRCm38.pep.all.fa.gz.pickle

