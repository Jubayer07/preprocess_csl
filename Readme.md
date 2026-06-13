# Text preprocessing python package



### Installation
You can install this package using pip as follows
```
pip install preprocess_csl

```
### Install form github
You can install this package from Github as follows:
```
pip install git+https://github.com/Jubayer07/preprocess_csl.git --upgrade --force-reinstall

```
### Requirements
You need to install these python package

```
pip install spacy==3.8.13
python -m spacy download en_core_web_sm==3.8.0
pip install nltk==3.9.2
pip install beautifulsoup4==4.13.5
pip install textblob== 0.20.0
```

### Download NLTK Data
You need to download NLTK data as follows:
```
import preprocess_csl as pcsl
pcsl.download_nltk_data()
```