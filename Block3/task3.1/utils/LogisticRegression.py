# logistic_regression.py
import numpy as np
from utils.gradient_descent import gradient_descent

class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=1000, lambda_=0, 
                 regularization=None, no_of_batches=1, verbose=False):
        """
        Custom Logistic Regression using Gradient Descent from scratch.

        Parameters
        ----------
        learning_rate : float, default=0.01
            Step size for gradient updates.
            
        iterations : int, default=1000
            Number of epochs over the dataset.
            
        lambda_ : float, default=0
            Regularization strength.
            
        regularization : str or None, default=None
            'l1', 'l2', or None.
            
        no_of_batches : int, default=1
            Number of batches per epoch:
            1 → Batch GD
            m → SGD
            k → Mini-batch GD
            
        verbose : bool, default=False
            Whether to print loss during training.
        """
        
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.lambda_ = lambda_
        self.regularization = regularization
        self.no_of_batches = no_of_batches
        self.verbose = verbose
        self.theta = None
        self.loss_history = []

    def _add_bias(self, X):
        """Add bias column (ones) to the input features."""
        return np.c_[np.ones((X.shape[0], 1)), X]

    def fit(self, X, y):
        """
        Fit the logistic regression model.

        Parameters
        ----------
        X : ndarray, shape (n_samples, n_features)
            Training data.
        y : ndarray, shape (n_samples,)
            Binary target values (0 or 1).
        """
        X_bias = self._add_bias(X)
        n_features = X_bias.shape[1]

        # Initialize weights
        self.theta = np.zeros(n_features)

        # Call our gradient descent function
        self.theta, self.loss_history = gradient_descent(
            X_bias, y, self.theta,
            learning_rate=self.learning_rate,
            iterations=self.iterations,
            lambda_=self.lambda_,
            regularization=self.regularization,
            no_of_batches=self.no_of_batches,
            verbose=self.verbose
        )

    def predict_proba(self, X):
        """
        Predict probabilities for input data.

        Parameters
        ----------
        X : ndarray, shape (n_samples, n_features)
            Input data.

        Returns
        -------
        probs : ndarray, shape (n_samples,)
            Predicted probabilities of class 1.
        """
        X_bias = self._add_bias(X)
        z = np.dot(X_bias, self.theta)
        return 1 / (1 + np.exp(-z))  # sigmoid

    def predict(self, X, threshold=0.5):
        """
        Predict binary labels for input data.

        Parameters
        ----------
        X : ndarray, shape (n_samples, n_features)
            Input data.

        threshold : float, default=0.5
            Decision threshold.

        Returns
        -------
        labels : ndarray, shape (n_samples,)
            Predicted class labels (0 or 1).
        """
        return (self.predict_proba(X) >= threshold).astype(int)
