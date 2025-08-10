# README — From-Scratch Logistic Regression + Gradient Descent

**Project status:** Completed ✅ — `gradient_descent.py` (supports Batch / Mini-batch / SGD) and `logistic_regression.py` (from-scratch logistic regression) implemented, evaluated, and submitted to the Kaggle competition.

---

# Summary

This repository contains a clean-from-scratch implementation of:

* `gradient_descent.py` — Gradient Descent optimizer that supports:

  * **Batch Gradient Descent**
  * **Mini-batch Gradient Descent**
  * **Stochastic Gradient Descent (SGD)**
* `logistic_regression.py` — Logistic Regression built on top of the optimizer that:

  * Uses **sigmoid** + **log-loss** (numerically stable implementation)
  * Supports **L1 (Lasso)** and **L2 (Ridge)** regularization (configurable)
  * Exposes `fit`, `predict_proba`, and `predict` methods
  * Tracks loss history for monitoring/convergence plots

---

# Files included

* `gradient_descent.py` — gradient descent implementation (batch / mini-batch / SGD)
* `logistic_regression.py` — logistic regression model using the optimizer
* `notebook.ipynb` — example notebook showing data loading, preprocessing, training, and evaluation (including polynomial feature experiments)
* `requirements.txt` — Python package requirements
* `README.md` — this file

---

# Key features & details

## Gradient descent (`gradient_descent.py`)

* API highlights:

  ```py
  theta, history = gradient_descent(
      X, y, theta_init,
      learning_rate=0.01,
      iterations=1000,
      lambda_=0.0,
      regularization=None,   # 'l1', 'l2', or None
      no_of_batches=1,       # 1 => Batch, m => SGD, k => Mini-batch
      verbose=False
  )
  ```
* Numerical stability: sigmoid and log-loss use clipping to avoid overflow / log(0).
* Regularization applied correctly and excludes bias term from penalty.
* Returns optimized `theta` and `history` (loss per epoch).

## Logistic regression (`logistic_regression.py`)

* API highlights:

  ```py
  model = LogisticRegression(
      learning_rate=0.01,
      iterations=1000,
      lambda_=0.0,
      regularization=None,    # 'l1' or 'l2' or None
      no_of_batches=1,        # batch / mini-batch / sgd
      verbose=False
  )
  model.fit(X_train, y_train)
  probs = model.predict_proba(X_test)
  preds = model.predict(X_test, threshold=0.5)
  ```
* Implements log-loss (cross-entropy) with added L1/L2 terms when requested.
* Internally adds bias column; accepts raw `X` (n\_samples, n\_features).
* Records `loss_history` for plotting training curves.

---

# Results & Kaggle leaderboard

* **Official submission achieved:** **3rd place** on the competition leaderboard.

  * **Public score:** `0.13572` (achieved using polynomial features degree = **3**).
* **Notes:** When experimenting further, increasing polynomial degree to **5** produced a **test loss of 0.121**, which would have pushed the submission to **1st place** — however, that run was after the competition cutoff / or otherwise not submitted to the competition leaderboard, so it is noted here for completeness only.

---

# How to reproduce (quick start)

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux / macOS
   venv\Scripts\activate           # Windows
   pip install -r requirements.txt
   ```

2. Run the notebook or a script that follows these steps:

   * Load dataset (Kaggle dataset used in the competition).
   * Train / validation split (e.g. `train_test_split(..., test_size=0.2, random_state=42)`).
   * Optional: scale features with `StandardScaler`.
   * Optional: expand features with `PolynomialFeatures(degree=3)` for the reported run.
   * Initialize and fit model:

     ```py
     model = LogisticRegression(
         learning_rate=0.1,
         iterations=2000,
         lambda_=0.1,
         regularization='l2',
         no_of_batches=1,   # batch GD
         verbose=True
     )
     model.fit(X_train, y_train)
     ```
   * Evaluate using `log_loss`, `accuracy_score`, `f1_score`, and create a Kaggle submission using `predict_proba`.

3. For the exact run that reached 3rd place:

   * Polynomial degree: `3`
   * Regularization: `L2` with `lambda_` used in training (check notebook hyperparams)
   * Seed / reproducibility: `random_state=42` (set everywhere: splitting, shuffling, numpy)
   * Number of iterations and learning rate as in notebook (see the notebook for final hyperparameters)

---

# Tuning & experiments tried

* Polynomial feature expansion (degree 2, 3, 4, 5) — degree 3 used for final submission.
* Regularization: L1 and L2 compared; L2 chosen for final due to better leaderboard behavior.
* Gradient descent types compared:

  * Full batch: stable, used for final submission.
  * Mini-batch: faster convergence in some settings; requires tuning batch size.
  * SGD: noisy but fast — useful for very large datasets.
* Observed that very high polynomial degree (degree 5) reduced test loss to `0.121` but introduced overfitting risks; that run would have given higher rank, but was not submitted on time / or dataset split differences caused it to be unsubmitted.

---

# Reproducibility tips

* Fix seeds:

  ```py
  import numpy as np, random
  np.random.seed(42)
  random.seed(42)
  ```
* Ensure you use the exact train/test split used for final submission.
* If you change polynomial degree or preprocessing, re-tune `learning_rate`, `lambda_`, and `iterations`.
* For numerical stability, prefer clipping logits and adding `eps=1e-15` in log computations (already implemented).

---

# Troubleshooting & common issues

* If you see `TypeError` about unexpected keyword arguments, confirm you are importing the correct `logistic_regression.py` (check `inspect.getfile(LogisticRegression)`).
* In notebooks, ensure the working directory is the package root or `sys.path` is adjusted so local `utils` is imported first:

  ```py
  import sys, os
  sys.path.insert(0, os.path.abspath('.'))
  ```
* When metrics complain about continuous vs binary targets, use `model.predict(X)` (binary) for `accuracy_score` / `f1_score`, and `model.predict_proba(X)` for log-loss and Kaggle submission.

---

# License

MIT License — feel free to reuse and adapt the code for learning and competitions. Please keep credits if you redistribute.

---

# Contact

If you want the exact training script or the saved model/weights used for the final submission, or want me to convert the older constructor names back in (so your notebook runs without edits), say the word and I’ll provide the file or a PR-ready patch.
