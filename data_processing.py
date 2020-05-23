import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data():
    # Default values.
    train_set = 'F:/UNSW_NB15_training-set.csv'
    test_set = 'F:/UNSW_NB15_testing-set.csv'
    train = pd.read_csv(train_set, index_col='id')
    test = pd.read_csv(test_set, index_col='id')

    # 二分类数据
    training_label = train['label'].values
    testing_label = test['label'].values
    temp_train = training_label
    temp_test = testing_label

    # Creates new dummy columns from each unique string in a particular feature
    unsw = pd.concat([train, test])
    unsw = pd.get_dummies(data=unsw, columns=['proto', 'service', 'state'])

    # Normalising all numerical features:
    unsw.drop(['label', 'attack_cat'], axis=1, inplace=True)
    unsw_value = unsw.values
    name = unsw.columns.tolist()
    scaler = MinMaxScaler(feature_range=(0, 1))
    unsw_value = scaler.fit_transform(unsw_value)
    train_set = unsw_value[:len(train), :]
    test_set = unsw_value[len(train):, :]

    # return train_set, training_label, test_set, testing_label
    return train_set, temp_train, test_set, temp_test, name
