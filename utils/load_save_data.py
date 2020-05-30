# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import datetime


def load_origin_data(data_path, data_name):

    df = pd.read_csv(os.path.join(data_path, data_name+'.csv'))

    return df


def save_feature(df, data_path, data_name):

    df.to_csv(
        os.path.join(data_path, 'feature_{0}.csv'.format(data_name))
        , index=False
        , header=True
        , encoding='utf-8'
    )


def save_submission(df, data_path, owner='x'):

    if not (len(df) == len(np.unique(df.user)) == 1000000):
        raise ValueError('df 预测条目数量不对！')
    if ('user_id' not in df) or ('predicted_age' not in df) or ('predicted_gender' not in df):
        raise ValueError('df 字段名不！')

    df[['user_id', 'predicted_age', 'predicted_gender']].to_csv(
        os.path.join(data_path, 'submission_{0}_{1}.csv'.format(owner, datetime.datetime.now().strftime('%m%d%H%M%S')))
        , index=False
        , header=True
        , encoding='utf-8'
    )