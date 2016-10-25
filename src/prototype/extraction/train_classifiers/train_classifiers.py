from src.prototype.extraction import feature_extraction
from src.prototype.extraction import model as model_lib
from src.prototype.lib import flags
from src.prototype.lib import plot
from src.prototype.lib import sample_repo
from src.prototype.lib import wikidata
from sklearn import calibration
from sklearn import linear_model
from sklearn import metrics
import numpy

def train_classifier_for_relation(relation, relation_name):
    print('Training extractor for', relation, relation_name)

    print('Loading samples...')
    train_samples = sample_repo.load_samples(relation, 'train')
    positive_count = len([s for s in train_samples if s.positive])
    negative_count = len([s for s in train_samples if not s.positive])
    print('Positive in train:', positive_count)
    print('Negative in train:', negative_count)

    test_samples = sample_repo.load_samples(relation, 'test')

    if positive_count < 10 or negative_count < 10:
        print('Too few samples to train for', relation, '.')
        return

    print('Selecting head features...')
    features_labels = feature_extraction.samples_to_all_features(train_samples)
    feature_counts = feature_extraction.get_feature_counts(features_labels)
    head_features_dict = feature_extraction.get_head_features(
        feature_counts,
        train_samples
    )

    print('Converting to feature matrix...')
    X_train, y_train = feature_extraction.samples_to_matrix_target(
        train_samples,
        head_features_dict
    )
    X_test, y_test = feature_extraction.samples_to_matrix_target(
        test_samples,
        head_features_dict
    )

    def try_classifier(name, classifier, prefix):
        print('Training %s...' % name)
        clf = classifier.fit(X_train, y_train)
        score = clf.predict_proba(X_test)
        score = [row[1] for row in score]

        fpr, tpr, _ = metrics.roc_curve(y_test, score)
        auc = metrics.auc(fpr, tpr)
        print("%s AUC:" % name, auc)

        plot.plot_roc(fpr, tpr, auc, prefix,
                      relation=relation,
                      relation_name=relation_name)

        predicted = clf.predict(X_test)
        print("%s accuracy:" % name, numpy.mean(predicted == y_test))

        return clf

    c = calibration.CalibratedClassifierCV(
        base_estimator=linear_model.LogisticRegression(verbose=True),
        method='isotonic',
    )
    clf = try_classifier('Logistic regression', c, 'logreg')
    model = model_lib.Model(clf, head_features_dict, relation)
    model.save()

    #try_classifier('Linear SVM',
    #               linear_model.SGDClassifier(loss='hinge', penalty='l2',
    #                                          alpha=1e-3, n_iter=5,
    #                                          random_state=42),
    #               'linear-svm')

def main():
    flags.add_argument('--relation', action='append')
    flags.make_parser(description='TODO')
    args = flags.parse_args()

    if args.relation:
        relations = args.relation
    else:
        assert False
        # relations = sample_repo.all_relations()

    wikidata_client = wikidata.WikidataClient()

    for relation in relations:
        relation_name = wikidata_client.get_name(relation)
        train_classifier_for_relation(relation, relation_name)

if __name__ == '__main__':
    main()