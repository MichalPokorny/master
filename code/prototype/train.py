from prototype.lib import sample_repo
import random
import nltk

relations = [
    'P25', # mother
    'P22', # father
    'P7', # brother
    'P40', # child
    'P26', # spouse
    'P108', # employer
    'P710', # participant
    'P463', # member of
    'P27', # country of citizenship
    'P36', # capital
    'P31', # instance of
    'P1066', # student of
    'P551', # residence
    'P112', # founder
    'P115', # follows
    'P175', # performer
    'P457', # member of political party
    'P50', # author
    'P19', # place of birth
    'P361', # part of
    'P86', # composer
    'P57', # director
]

# relations = sample_repo.all_relations()

def sample_to_features_label(sample):
    features = {}
    for token in sample.sentence.tokens:
        features['lemma_' + token.lemma.lower()] = 1
        word = sample.sentence.text[token.start_offset:token.end_offset]
        features['word_' + word] = 1
    return (features, sample.relation)

#samples = sample_repo.load_samples(mother)
#for sample in samples:
#    lemmas = []
#    for i, token in enumerate(sample.sentence.tokens):
#        lemmas.append(token.lemma)
#    print(" ".join(lemmas))

def cull_uninformative_features(samples):
    feature_counts = {}
    for sample in samples:
        for feature in list(sample[0].keys()):
            if feature not in feature_counts:
                feature_counts[feature] = 0
            feature_counts[feature] += 1

    min_feature_occurrences = 10

    for sample in samples:
        for feature in list(sample[0].keys()):
            if feature_counts[feature] < min_feature_occurrences:
                del sample[0][feature]

samples = []
for relation in relations:
    print('Loading relation', relation, '...')
    for sample in sample_repo.load_samples(relation):
        samples.append(sample_to_features_label(sample))

cull_uninformative_features(samples)

print("Samples:", len(samples))

random.shuffle(samples)
n_train = round(len(samples) * 0.5)
train = samples[:n_train]
test = samples[n_train:]
print("N training samples:", len(train), "test:", len(test))

print('Training...')
classifier = nltk.NaiveBayesClassifier.train(train)
print('Accuracy:', nltk.classify.accuracy(classifier, test))
classifier.show_most_informative_features(10)
