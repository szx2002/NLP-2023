import random

corpus_file = 'RMRB_NER_CORPUS.txt'
corpus = []
with open(corpus_file, 'r', encoding='utf-8')as f:
    record = []
    for line in f:
        if line != '\n':
            record.append(line.strip('\n').split(' '))
        else:
            corpus.append(record)
            record = []


random.seed(9999)
random.shuffle(corpus)

fullLen = len(corpus)
splitLen = len(corpus) // 10

train = corpus[:splitLen * 8]
valid = corpus[splitLen * 8:splitLen * 9]
test = corpus[splitLen * 9:]

train_file = 'ner_train.txt'
valid_file = 'ner_valid.txt'
test_file = 'ner_test.txt'

for split_file, split_corpus in zip([train_file, valid_file, test_file],
                                    [train, valid, test]):
    with open(split_file, 'w')as f:
        for sentence in split_corpus:
            for word, label in sentence:
                f.write(word)
                f.write(' ')
                f.write(label)
                f.write('\n')
            f.write('\n')
