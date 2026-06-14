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
### Uninstall the package
To uninstall the package user the following commands
```
bash
pip uninstall preprocess_csl
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

## How to Use the Package

### 1. Basic Text Preprocessing

#### Lowercasing Text

```python
import preprocess_csl as pcsl

text = "HELLO WORLD!"
processed_text = pcsl.to_lower_case(text)
print(processed_text)  # Output: hello world!
```

#### Expanding Contractions

```python
import preprocess_csl as pcsl

text = "I'm learning Natural Languge Processing."
processed_text = pcsl.contraction_to_expansion(text)
print(processed_text)  # Output: I am learning Natural Languge Processing.
```

#### Removing Emails

```python
import preprocess_csl as pcsl

text = "Contact me at example@example.com"
processed_text = pcsl.remove_emails(text)
print(processed_text)  # Output: Contact me at 
```

#### Removing URLs

```python
import preprocess_csl as pcsl

text = "Check out https://example.com"
processed_text = pcsl.remove_urls(text)
print(processed_text)  # Output: Check out
```

#### Removing HTML Tags

```python
import preprocess_csl as pcsl

text = "<p>Hello World!</p>"
processed_text = pcsl.remove_html_tags(text)
print(processed_text)  # Output: Hello World!
```

#### Removing Special Characters

```python
import preprocess_csl as pcsl

text = "Hello @World! #NLP"
processed_text = pcsl.remove_special_chars(text)
print(processed_text)  # Output: Hello World NLP
```

### 2. Advanced Text Processing

#### Lemmatization

```python
import preprocess_csl as pcsl

text = " ate eating eats"
processed_text = pcsl.lemmatize(text)
print(processed_text)  # Output: eat
```

#### Sentiment Analysis

```python
import preprocess_csl as pcsl

text = "I love programming!"
sentiment = pcsl.sentiment_analysis(text)
print(sentiment)  # Output: Sentiment(polarity=0.5, subjectivity=0.6)
```



### 3. Feature Extraction

#### Word Count

```python
import preprocess_csl as pcsl

text = "I Like Natural Language Processing."
count = pcsl.word_count(text)
print(count)  # Output: 5
```

#### Character Count

```python
import preprocess_csl as pcsl

text = "I Love Python programming! It's amazing. 123"
count = pcsl.char_count(text)
print(count)  # Output: 38
```

#### N-Grams

```python
import preprocess_csl as pcsl

text = "I love NLP"
ngrams = pcsl.n_grams(text, n=2)
print(ngrams)  # Output: [('I', 'love'), ('love', 'NLP')]
```

### 4. Full Example: Cleaning Text

Here’s an example of how you might use several functions together to clean text data:

```python
import preprocess_csl as pcsl

text = "I'm loving this NLP tutorial!"
cleaned_text = pcsl.clean_text(text)
print(cleaned_text)
# Output: i am loving this nlp tutorial
```

###  Feature Extraction
```python
import preprocess_csl as pcsl

pcsl.extract_features("I love Natural Language Processing")
```