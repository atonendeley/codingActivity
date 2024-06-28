
Readme File: Text Preprocessing for Twitter Data
Overview
This Python script performs text preprocessing on Twitter data using various libraries and techniques. The preprocessing steps include cleaning, filtering out stopwords and URLs, and tokenizing tweets to prepare them for further analysis.

Libraries Used
The script utilizes the following Python libraries:

scikit-learn (sklearn): CountVectorizer for text vectorization.
gensim: Dictionary for creating a dictionary from a list of tokenized documents, LdaModel for Latent Dirichlet Allocation topic modeling, and CoherenceModel for model coherence evaluation.
nltk (Natural Language Toolkit): stopwords for filtering out common English stopwords, RegexpTokenizer for tokenizing tweets based on regular expressions.
pandas: pd for data manipulation and analysis.
datetime: datetime for date and time manipulation.
re (Regular Expression): re for working with regular expressions.
math: math for mathematical operations.
Function: clean_tweets
The script defines a function clean_tweets to preprocess Twitter data. Here’s a brief description of what the function does:

Parameters:

df: DataFrame containing Twitter data (df_tweets loaded from 'trump_tweets.csv').
tweet_col: Column name containing tweet text (default: 'text').
date_col: Column name containing tweet creation date (default: 'created_at').
start_datetime: Starting date for filtering tweets (default: January 20, 2017).
Steps:

Data Cleaning: Drops rows with empty values and formats the date column.
Date Filtering: Filters out tweets older than start_datetime.
Text Preprocessing:
Converts tweet text to lowercase.
Removes stopwords and URLs from tweets.
Tokenizes tweets using RegexpTokenizer.
Returns: Returns a cleaned DataFrame (df_copy) with additional columns for preprocessed and tokenized tweet text.
