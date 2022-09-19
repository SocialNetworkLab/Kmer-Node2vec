KMer-Node2Vec
====================================
KMer-Node2Vec is an open-source library to train distributued vector representations of k-mers from the k-mer graph. For more information, please refer to the paper: [KMer-Node2Vec: Learning Vector Representations of K-mers from the K-mer Graph](https://doi.org/10.1101/2022.08.30.505832).

------------------------------------

### Requirements

The codebase is implemented in Python 3.8 package versions used for development are just below.
```
arrow                 1.2.2
Bio                   1.3.3
gensim                4.1.0
Logbook               1.5.3
networkx              2.6.3
numba                 0.54.1
numba_progress        0.0.2
numpy                 1.20.3
prettytable           3.2.0
scikit_learn          1.0.2
scipy                 1.7.3
setuptools            58.0.4
tqdm                  4.62.3
```
### Datasets
<p align="justify">
The code takes FASTA format files with file extension of **.fna**. Note that all training FASTA format files should be under the same input directory. A sample FASTA format file is included in the  `data_dir/input/` directory. </p>
<p align="justify">
Training the model is handled by the `src/cli.py` script which provides the following command line arguments.</p>

#### Input and output options
```
  --input-seqs-dir   STR   Sequence files directory.   Default is `data_dir/input/`.
  --output           STR   K-mer embedding path.       Default is `data_dir/output/kmernode2vec-{}.txt'.format(arrow.utcnow().format('YYYYMMDD-HHmm'))`.
  --edge-list-file   STR   Edge file path.             Default is `data_dir/output/edge-list-file-{}.edg'.format(arrow.utcnow().format('YYYYMMDD-HHmm'))`
```
#### Random walk options
```
  --window-size      INT    Skip-gram window size.        Default is 10.
  --walk-number      INT    Number of walks per node.     Default is 40.
  --walk-length      INT    Number of nodes in walk.      Default is 150.
  --P                FLOAT  Return parameter.             Default is 1.0.
  --Q                FLOAT  In-out parameter.             Default is 0.001.
```
#### Factorization options
```
  --dimensions       INT      Number of dimensions.      Default is 128
  --min-count        INT      Minimal count.             Default is 1
  --workers          INT      Number of cores.           Default is 4.
  --epochs           INT      Number of epochs.          Default is 1.
```

#### Feature creation options

```
  --mer              INT      Length of a sliding window to fragment Mer.         Default is 8.
```

### Examples
<p align="justify">
The following commands learn a KMerNode2Vec embedding. The first example trains an embedding based on the default dataset with standard hyperparameter settings.  The script saves the embedding at the default path.</p>
```
python3 src/cli.py
```

Using a custom length of mer for the embedding.
```
python3 src/main.py --mer 8
```
Using a custom factorization dimension for the embedding.
```
python3 src/main.py --dimensions 64
```
Using second-order ranom walks for sampling.
```
python3 src/main.py --P 1 --Q 4
```



--------------------------------------------------------------------------------

**License**

- This software is licensed under the [MIT license](http://en.wikipedia.org/wiki/MIT_License)

--------------------------------------------------------------------------------
