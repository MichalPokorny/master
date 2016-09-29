import json
from prototype.lib import flags
from prototype.lib import relations
from prototype.lib import plot
from prototype.fusion import fuser
from sklearn import linear_model
from sklearn import metrics
from sklearn import cross_validation
import math
import numpy
import paths

def show_certainty_histogram(samples):
    certainties = []
    for sample in samples:
        for certainty in sample:
            certainties.append(certainty)

    certainties.sort()

    for p in 10, 50, 90:
        print('Percentile', p, ':', numpy.percentile(certainties, p))

def show_support_count_histogram(samples):
    histogram = {}
    for sample in samples:
        length = len(sample)
        if length not in histogram:
            histogram[length] = 0
        histogram[length] += 1
    total = sum(histogram.values())
    for length in sorted(histogram.keys()):
        count = histogram[length]
        percentage = (100.0 * count / total)
        print(('%d' % length).ljust(5), count) # "%.2f" % percentage)

def train_relation_fuser(relation, samples):
    positive_sentence_scores = samples['true']
    negative_sentence_scores = samples['false']

    features = []
    labels = []

    print('Positive support count histogram:')
    show_support_count_histogram(positive_sentence_scores)
    print('Positive certainty histogram:')
    show_certainty_histogram(positive_sentence_scores)
    print('Negative support count histogram:')
    show_support_count_histogram(negative_sentence_scores)
    print('Negative certainty histogram:')
    show_certainty_histogram(negative_sentence_scores)

    for sample in positive_sentence_scores:
        features.append(fuser.sentence_scores_to_features(sample))
        labels.append(1)

    for sample in negative_sentence_scores:
        features.append(fuser.sentence_scores_to_features(sample))
        labels.append(0)

    # train-test split
    # TODO: Separate out the sets?
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(
        features, labels, test_size=0.33, random_state=42)

    # TODO: Decision trees instead?
    clf = linear_model.LogisticRegression(verbose=True)
    clf.fit(X_train, y_train)
    score = clf.decision_function(X_test)

    fpr, tpr, _ = metrics.roc_curve(y_test, score)
    auc = metrics.auc(fpr, tpr)
    print("%s AUC:" % relation, auc)

    predicted = clf.predict(X_test)
    print("%s accuracy:" % relation, numpy.mean(predicted == y_test))

    plot.plot_roc_general(
        fpr,
        tpr,
        '%s (area = %.02f)' % (relation, auc),
        paths.CHARTS_PATH + '/' + relation + '.png'
    )

    f = fuser.Fuser(
        relation = relation,
        classifier = clf,
    )
    f.save()

def main():
    flags.add_argument('--relation', action='append')
    flags.make_parser(description='TODO')
    args = flags.parse_args()

    if args.relation:
        run_on = args.relation
    else:
        run_on = relations.RELATIONS

    for relation in run_on:
        input_file = fuser.FUSER_TRAINING_DATA_PATH + '/' + relation + '.json'
        with open(input_file, 'r') as f:
            relation_data = json.load(f)
        samples = relation_data
        train_relation_fuser(relation, samples)

if __name__ == '__main__':
    main()