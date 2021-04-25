import json
import re
from tqdm import tqdm
from language import get_lange_cld


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

def language_search(tweet_dicts, key='text', language='de', min_words=0):
    filtered_tweet_dicts = []
    found_tweet_dicts = []
    not_applicable_tweet_dicts = []
    for i, tweet in enumerate(tqdm(tweet_dicts)):
        text = tweet[key]
        if len(text.split(' ')) < min_words:
            not_applicable_tweet_dicts.append(i)
        else:
            lang = get_lange_cld(text)
            match = lang == language
            if match is False:
                found_tweet_dicts.append(i)
            else:
                filtered_tweet_dicts.append(i)

    print(f"Tweets found in language {language} : {len(filtered_tweet_dicts)}")
    print(f"Tweets found not language {language} : {len(found_tweet_dicts)}")
    print(f"Tweets too short for identifier to be trusted : {len(not_applicable_tweet_dicts)}")
    return found_tweet_dicts, filtered_tweet_dicts, not_applicable_tweet_dicts



def regex_search(pattern, tweet_dicts, key='text'):
    """Seaches for matches between the tweet_dict[key] and the regex patterns.
        Returns list of indices where there is a match

    Args:
        pattern ([type]): [description]
        tweet_dicts ([type]): [description]
        key (str, optional): [description]. Defaults to 'text'.

    Returns:
        [type]: [description]
    """
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
        print(f"Language Classifer : {get_lange_cld(tweet[key])}")
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
