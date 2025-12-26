import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

class SVDPCA:
    def __init__(self, n_components=None):
        self.n_components = n_components

    @staticmethod
    def svd_flip_vector(U):
        max_abs_cols_U = np.argmax(np.abs(U), axis=0)
        # extract the signs of the max absolute values
        signs_U = np.sign(U[max_abs_cols_U, range(U.shape[1])])

        return U * signs_U

    def fit_transform(self, X):
        n_samples, n_features = X.shape
        X_centered = X - X.mean(axis=0)

        if self.n_components is None:
            self.n_components = min(n_samples, n_features)

        U, S, Vt = np.linalg.svd(X_centered)
        # flip the eigenvector sign to enforce deterministic output
        U_flipped = self.svd_flip_vector(U)

        self.explained_variance = (S[:self.n_components] ** 2) / (n_samples - 1)
        self.explained_variance_ratio = self.explained_variance / np.sum(self.explained_variance)

        # X_new = X * V = U * S * Vt * V = U * S
        X_transformed = U_flipped[:, : self.n_components] * S[: self.n_components]

        return X_transformed

if __name__ == "__main__":
    X, y = load_iris(return_X_y=True, as_frame=True)
    print(X)

    # pca = SVDPCA()
    # X_transformed = pca.fit_transform(X)
    #
    # print('transformed data', X_transformed[:10], '', sep='\n')
    # print('explained_variance', pca.explained_variance)
    # print('explained_variance_ratio', pca.explained_variance_ratio)

    sk_pca = PCA()
    sk_X_transformed = sk_pca.fit_transform(X)

    print('sk transformed data', sk_X_transformed[:10], '', sep='\n')
    print('sk explained_variance', sk_pca.explained_variance_)
    print('sk explained_variance_ratio_', sk_pca.explained_variance_ratio_)