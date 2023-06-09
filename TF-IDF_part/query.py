import math

# function to return dictionary of vocan terms & their tf-idf value
def load_vocab():
    vocab = {}
    with open('TF-IDF_part/vocab.txt', 'r') as f:
        vocab_terms = f.readlines()
    with open('TF-IDF_part/idf-values.txt', 'r') as f:
        idf_values = f.readlines()
    
    for (term,idf_value) in zip(vocab_terms, idf_values):
        vocab[term.strip()] = int(idf_value.strip())
    
    return vocab

# funtion loads documents & prints their number
def load_documents():
    documents = []
    with open('TF-IDF_part/documents.txt', 'r') as f:
        documents = f.readlines()
    documents = [document.strip().split() for document in documents]

    print('Number of documents: ', len(documents))
    # print('Sample document: ', documents[0])
    return documents

# function to load inverted index terms & the relevant documents
def load_inverted_index():
    inverted_index = {}
    with open('TF-IDF_part/inverted-index.txt', 'r') as f:
        inverted_index_terms = f.readlines()

    # going through  all the terms
    for row_num in range(0,len(inverted_index_terms),2):
        term = inverted_index_terms[row_num].strip()
        documents = inverted_index_terms[row_num+1].strip().split()# second line of inverted index file has the documents list
        inverted_index[term] = documents
    
    print('Size of inverted index: ', len(inverted_index))
    return inverted_index

vocab_idf_values = load_vocab()
documents = load_documents()
inverted_index = load_inverted_index()

def get_tf_dictionary(term):
    tf_values = {}
    if term in inverted_index:
        for document in inverted_index[term]:
            if document not in tf_values:
                tf_values[document] = 1
            else:
                tf_values[document] += 1
                
    for document in tf_values:
        tf_values[document] /= len(documents[int(document)]) #function calculates the tf value of the documents
    
    return tf_values

def get_idf_value(term):
    return math.log(len(documents)/vocab_idf_values[term])

# main function to obtain sorted list of documents
def calculate_sorted_order_of_documents(query_terms):
    potential_documents = {}
    for term in query_terms:
        if vocab_idf_values[term] == 0:
            continue
        tf_values_by_document = get_tf_dictionary(term)
        idf_value = get_idf_value(term)
        # print(term,tf_values_by_document,idf_value)
        for document in tf_values_by_document:
            if document not in potential_documents:
                potential_documents[document] = tf_values_by_document[document] * idf_value
            potential_documents[document] += tf_values_by_document[document] * idf_value #final score calculation for documents

    print('------------------------------------------------------------')
    print('Relevent documents result count: ', len(potential_documents))
    print('------------------------------------------------------------')
    # divite by the length of the query terms
    for document in potential_documents:
        potential_documents[document] /= len(query_terms)

    # sorting of documents by score
    potential_documents = dict(sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))

    for document_index in potential_documents:
        print('Document: ', documents[int(document_index)], ' Score: ', potential_documents[document_index])

# Getting input query from the user
query = input('Enter your query term: ')
query_terms = [term.lower() for term in query.strip().split()]

print(query_terms)
calculate_sorted_order_of_documents(query_terms)