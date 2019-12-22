# -*- coding: utf-8 -*-

from pathlib import Path
from pkg_resources import resource_listdir, resource_filename

import pandas as pd

__data_files = resource_listdir('pyannotables.data', '')
__full_data_files = {Path(filename).stem.split('.')[0].split('datafile_')[1]: resource_filename('pyannotables.data', filename) for filename in __data_files if filename.startswith('datafile_')}
tables = {key: pd.read_pickle(val) for key, val in __full_data_files.items()}
