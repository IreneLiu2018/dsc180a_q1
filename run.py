import sys
import os
import json
import pandas as pd

sys.path.insert(0, 'src')

# import env_setup
# from etl import get_data
# from features import apply_features

# from model import model_build


# change the data path in ipynb with the test data's info can make the project work well


def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''

    # env_setup.make_datadir()
    # env_setup.auth()

    if 'test' in targets:
        with open('config/testdata-params.json') as fh:
            data_cfg = json.load(fh)

        # make the data target
        df_test = pd.DataFrame.from_dict(data_cfg, orient="index").transpose()

        print(df_test)

    # if 'features' in targets:
    #     with open('config/features-params.json') as fh:
    #         feats_cfg = json.load(fh)

    #     feats, labels = apply_features(data, **feats_cfg)

    # if 'model' in targets:
    #     with open('config/model-params.json') as fh:
    #         model_cfg = json.load(fh)

    #     # make the data target
    #     model_build(feats, labels, **model_cfg)

    return df_test


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)