from backend import *

# filename = 'tweet_stream_01'
filename = 'tweet_stream_01_processed'
addendum = '_processed'
ending = '.txt'
key = 'text'

if __name__ == "__main__":

    tweet_dicts = load_data(filename, ending=ending)

    def boolean_loop(text='Keep'):
        while True:
                bool = str(input(f'{text} [y/n] :'))
                if bool == 'y':
                    return True
                elif bool == 'n':
                    return False

    while True:
        ### Insert Regex parsing here
        print("Write Regex Pattern to search:")
        pattern = str(input('Pattern [str]: '))
        found_tweet_dicts, filtered_tweet_dicts = regex_search(pattern, tweet_dicts)

        # Got to manual Filtering
        if boolean_loop("Use Pattern for Filter?"):
            tweet_dicts = merge_filtered(found_tweet_dicts, filtered_tweet_dicts, tweet_dicts)

        # Exit this loop?
        if boolean_loop("Filter with new Pattern?") is False:
            break
    
    save_tweets(tweet_dicts, filename+addendum, ending=ending)


    

    