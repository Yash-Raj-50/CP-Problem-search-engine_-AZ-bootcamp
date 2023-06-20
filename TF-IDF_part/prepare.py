# importing chardet to determine encoding of file
import chardet

# finding encoding of index file that has all the title names
def find_encoding(filename):
    r_file = open(filename, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

my_file = 'Qdata/index.txt'
my_encoding = find_encoding(my_file)

# opening index file here
# with open(my_file, 'r', encoding=my_encoding) as f:
with open(my_file, 'r', encoding="utf-8") as f:
    lines = f.readlines()

# preprocess function to take title from index file & break it into terms and return ut
def preprocess(document_text):
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms

vocab = {}
documents = []

# code to run through terms(token) in lines and update vocab dictionary
for index, line in enumerate(lines):
    tokens = preprocess(line)
    documents.append(tokens)
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

# sorting vocab in reverse order
vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

print('Number of documents: ', len(documents))
print('Size of vocab: ', len(vocab))
print('Sample document: ', documents[0])

# writing keys and values of vocab in different files
with open('TF-IDF_part/vocab.txt', 'w',encoding="utf-8") as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

with open('TF-IDF_part/idf-values.txt', 'w',encoding="utf-8") as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

with open('TF-IDF_part/documents.txt', 'w',encoding="utf-8") as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))


# code to obtain inverted index frequency 
inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)

with open('TF-IDF_part/inverted-index.txt', 'w',encoding="utf-8") as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))