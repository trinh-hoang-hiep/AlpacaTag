def load_data_and_labels(filename, encoding='utf-8'):
    sents, labels = [], []
    words, tags = [], []
    with open(filename, encoding=encoding) as f:
        for line in f:
            line = line.rstrip()
            if line:
                word, tag = line.split(' ')
                words.append(word)
                tags.append(tag)
                # except:
                #     print(line)
                #     pass
            else:
                sents.append(words)
                labels.append(tags)
                words, tags = [], []

    return sents, labels
x_train, y_train = load_data_and_labels('com.bio')#vlsp#myfile
print(len(x_train))