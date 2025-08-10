# gradient_descent.py
import numpy as np

def gradient_descent(X, y, theta, learning_rate=0.01, iterations=1000, lambda_=0, 
                     regularization=None, no_of_batches=1, verbose=False):
    """
    Gradient Descent optimizer for Logistic Regression with support for 
    Batch, Mini-batch, and Stochastic modes.
    and regularization techniques (L1, L2).
    
    Parameters
    ----------
    X : ndarray, shape (n_samples, n_features)
        Training data (including bias column if already added)
        
    y : ndarray, shape (n_samples,)
        Target values (0 or 1 for binary classification)
        
    theta : ndarray, shape (n_features,)
        Initial weights.
        
    learning_rate : float, default=0.01
        Step size for updates.
        
    iterations : int, default=1000
        Number of iterations over the entire dataset.
        
    lambda_ : float, default=0
        Regularization strength.
        
    regularization : str or None, default=None
        Type of regularization: 'l1', 'l2', or None.
        
    no_of_batches : int, default=1
        Number of batches per iteration.
        no_of_batches = 1        # Batch
        no_of_batches = len(X)   # SGD
        no_of_batches = k        # Mini-batch (k batches per epoch)

        
    verbose : bool, default=False
        If True, prints loss every 100 iterations.
    
    Returns
    -------
    theta : ndarray
        Optimized weights.
        
    history : list
        Loss values for each iteration.
    """
    
    m = len(y)
    history = []

    for epoch in range(iterations):
        # Shuffle data each epoch for SGD/mini-batch
        indices = np.arange(m)
        np.random.shuffle(indices)
        X_shuffled = X[indices]
        y_shuffled = y[indices]

        batch_size = m // no_of_batches

        for batch in range(no_of_batches):
            start = batch * batch_size
            end = start + batch_size if batch != no_of_batches - 1 else m

            X_batch = X_shuffled[start:end]
            y_batch = y_shuffled[start:end]
            mb_size = len(y_batch)

            # Hypothesis
            z = np.dot(X_batch, theta)
            h = 1 / (1 + np.exp(-z))  # sigmoid

            # Gradient calculation
            error = h - y_batch
            gradient = (1 / mb_size) * np.dot(X_batch.T, error)

            # Regularization in gradient
            if regularization == 'l2':
                gradient += (lambda_ / mb_size) * theta
                gradient[0] -= (lambda_ / mb_size) * theta[0]
            elif regularization == 'l1':
                gradient += (lambda_ / mb_size) * np.sign(theta)
                gradient[0] -= (lambda_ / mb_size) * np.sign(theta[0])

            # Update theta
            theta -= learning_rate * gradient

        # Loss calculation after epoch
        z_all = np.dot(X, theta)
        h_all = 1 / (1 + np.exp(-z_all))
        loss = - (1 / m) * np.sum(y * np.log(h_all + 1e-15) + (1 - y) * np.log(1 - h_all + 1e-15))
        if regularization == 'l2':
            loss += (lambda_ / (2 * m)) * np.sum(theta[1:] ** 2)
        elif regularization == 'l1':
            loss += (lambda_ / (2 * m)) * np.sum(np.abs(theta[1:]))

        history.append(loss)

        if verbose and epoch % 100 == 0:
            print(f"Epoch {epoch}/{iterations} - Loss: {loss:.6f}")

    return theta, history
