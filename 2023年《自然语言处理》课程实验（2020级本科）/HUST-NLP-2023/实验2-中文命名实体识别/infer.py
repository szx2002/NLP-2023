import torch
import pickle

if __name__ == '__main__':
    model = torch.load('save/model_epoch9.pkl', map_location=torch.device('cpu'))
    output = open('ner_result.txt', 'w', encoding='gbk')

    with open('data/ner_data_save.pkl', 'rb') as fnp:
        word2id = pickle.load(fnp)
        id2word = pickle.load(fnp)
        tag2id = pickle.load(fnp)
        id2tag = pickle.load(fnp)

    with open('data/test_data.txt', 'r', encoding='gbk') as f:
        line_test = ''
        for test in f:
            test = test.strip()

            if not test:
                x = torch.LongTensor(1, len(line_test))
                mask = torch.ones_like(x, dtype=torch.uint8)
                length = [len(line_test)]
                for i in range(len(line_test)):
                    if line_test[i] in word2id:
                        x[0, i] = word2id[line_test[i]]
                    else:
                        x[0, i] = len(word2id)

                predict = model.infer(x, mask, length)[0]
                for i in range(len(line_test)):
                    print(line_test[i], id2tag[predict[i]], file=output)
                print(file=output)

                line_test = ''
            
            else:
                test = test.split(' ')
                line_test += test[0]
