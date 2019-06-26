# first line: 1
@mem_svd.cache
def get_svd_array(dataset):
    svd = TruncatedSVD(n_components=10)
    svd_dataset = np.array([svd.fit_transform(day) for day in dataset])
    return svd_dataset
