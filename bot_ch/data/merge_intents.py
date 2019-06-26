# coding=utf-8
import glob
import os

def write_intent_data(data_dir, outfile):
    files = glob.glob('intents/*.md')
    for fname in files:
        with open(fname, 'r') as infile:
            outfile.write(infile.read() + '\n')
            outfile.write('\n')

def create_train_file(train_file, data_dir):
    with open(train_file, 'w') as outfile:
        write_intent_data(data_dir, outfile)   
 
if __name__ == '__main__':
    create_train_file('nlu.md', 'data_dir') 