#!/usr/bin/python3

"""
Usage:
    ./spotlight.py \
        --article_plaintext_path=/mnt/crypto/data/wiki-articles/Allan_Dwan.txt \
        --output_path=Allan_Dwan.spotlight.json
"""

import argparse

import json
import requests

def annotate_text(text):
    server = 'http://spotlight.sztaki.hu:2222'
    url = server + '/rest/annotate'
    r = requests.get(url, params={
      'text': text,
      'confidence': '0.35'
    }, headers={'Accept': 'application/json'})
    return r.json()

def main():
    parser = argparse.ArgumentParser(description='Get DBpedia entity mentions using Spotlight')
    parser.add_argument('--article_plaintext_path', required=True)
    parser.add_argument('--output_path', required=True)
    args = parser.parse_args()

    text = open(args.article_plaintext_path).read()
    result = annotate_text(text)
    with open(args.output_path, 'w') as f:
        f.write(json.dumps(result))

if __name__ == '__main__':
    main()
