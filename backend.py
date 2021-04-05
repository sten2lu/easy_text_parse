import json
import re


# filename = 'tweet_stream_01'
# addendum = '_processed'
# ending = '.txt'
# key = 'text'

def load_data(filename, ending='.txt'):
    #Load lines
    with open(filename+ending, 'r') as file:
        lines = file.readlines()


    # Lines of strings to lines of dictionaries
    tweet_dicts = []
    for i, line in enumerate(lines):
        try:
            tweet_dicts.append(json.loads(line))
        except:
            print(f"Error in Line {i}")
            print(line)

    print(f"Tweets processed: {len(tweet_dicts)}")
    print(f"Lines in file: {len(lines)}")

    del lines
    return tweet_dicts


def regex_search(pattern, tweet_dicts, key='text'):
    filtered_tweet_dicts = []
    found_tweet_dicts = []
    for i, tweet in enumerate(tweet_dicts):
        text = tweet[key]
        match = re.search(pattern, text)
        if match is not None:
            found_tweet_dicts.append(i)
        else:
            filtered_tweet_dicts.append(i)

    print(f"Tweets found matching regex Pattern : {len(found_tweet_dicts)}")
    return found_tweet_dicts, filtered_tweet_dicts

def merge_filtered(found_tweet_dicts, filtered_tweet_dicts, tweet_dicts, key='text'):
    merge_tweet_dicts = []
    for item in found_tweet_dicts:
        
        tweet = tweet_dicts[item]
        print()
        print("Do you want to keep this tweet?")
        print("Tweet:")
        print(tweet[key])
        print(f"Name : {tweet['user']['name']}")
        print(f"Screen Name : {tweet['user']['screen_name']}")
        print(f"Location : {tweet['user']['location']}")
        while True:
            keep = str(input('Keep [y/n] :'))
            if keep == 'y':
                merge_tweet_dicts.append(item)
                break
            elif keep == 'n':
                break
    return use_mask(tweet_dicts, merge_(merge_tweet_dicts, filtered_tweet_dicts))
    
def merge_(merge_tweet_dicts, filtered_tweet_dicts):
    if len(merge_tweet_dicts) > 0:
        filtered_tweet_dicts.extend(merge_tweet_dicts)

    filtered_tweet_dicts = sorted(filtered_tweet_dicts)
    return filtered_tweet_dicts

def use_mask(tweet_dicts, filtered_tweet_dicts):
    return [ tweet_dicts[index] for index in filtered_tweet_dicts]

def save_tweets(filtered_tweet_dicts, filename, ending='.txt'):
    # Save the processed tweet_dict
    with open(filename+ending, 'w') as file:

        lines = [json.dumps(tweet) for tweet in filtered_tweet_dicts]
        for line in lines:
            file.write(line+"\n")
