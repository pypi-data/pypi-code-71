import numpy as np

from sklearn.datasets import load_iris
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.testing import assert_true
from sklearn.utils.testing import assert_equal

from lightning.classification import SVRGClassifier
from lightning.regression import SVRGRegressor
from lightning.impl.sgd_fast import SmoothHinge

iris = load_iris()
X, y = iris.data, iris.target

X_bin = X[y <= 1]
y_bin = y[y <= 1] * 2 - 1


def test_svrg():
    clf = SVRGClassifier(eta=1e-3, max_iter=20, random_state=0, verbose=0)
    clf.fit(X_bin, y_bin)
    assert not hasattr(clf, 'predict_proba')
    assert_equal(clf.score(X_bin, y_bin), 1.0)


def test_svrg_callback():
    class Callback(object):

        def __init__(self, X, y):
            self.X = X
            self.y = y
            self.obj = []

        def __call__(self, clf):
            clf._finalize_coef()
            y_pred = clf.decision_function(self.X).ravel()
            loss = (np.maximum(1 - self.y * y_pred, 0) ** 2).mean()
            coef = clf.coef_.ravel()
            regul = 0.5 * clf.alpha * np.dot(coef, coef)
            self.obj.append(loss + regul)

    cb = Callback(X_bin, y_bin)
    clf = SVRGClassifier(loss="squared_hinge", eta=1e-3, max_iter=20,
                         random_state=0, callback=cb)
    clf.fit(X_bin, y_bin)
    assert_true(np.all(np.diff(cb.obj) <= 0))


def test_svrg_regression():
    reg = SVRGRegressor(eta=1e-3)
    reg.fit(X_bin, y_bin)
    y_pred = np.sign(reg.predict(X_bin))
    assert_equal(np.mean(y_bin == y_pred), 1.0)


def test_bin_classes():
    clf = SVRGClassifier()
    clf.fit(X_bin, y_bin)
    assert_equal(list(clf.classes_), [-1, 1])


def test_multiclass_classes():
    clf = SVRGClassifier()
    clf.fit(X, y)
    assert_equal(list(clf.classes_), [0, 1, 2])
