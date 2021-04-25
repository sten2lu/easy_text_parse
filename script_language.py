from backend import *

filename = 'tweet_stream_01' # Filename to be used (without filetype)
min_words=0 # The language classifer performance depends on the amount of words
ending = '.txt' # Filetype 
key = 'text' #key of dictionary by which it is filtered
language = 'de' # wich language in the text is wished

if __name__ == "__main__":

    tweet_dicts = load_data(filename, ending=ending)
    found_tweet_dicts, filtered_tweet_dicts, short_tweet_dicts =  \
        language_search(tweet_dicts, min_words=min_words, language=language)

    tweet_found =[tweet_dicts[i] for i in found_tweet_dicts]
    save_tweets(tweet_found, filename+'_outfiltered', ending=ending)
    tweet_filtered =[tweet_dicts[i] for i in filtered_tweet_dicts]
    save_tweets(tweet_dicts, filename+'_processed', ending=ending)
    tweet_short =[tweet_dicts[i] for i in short_tweet_dicts]
    save_tweets(tweet_short, filename+'_short', ending=ending)
    