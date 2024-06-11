import os 
import sys
from src.utils.logger import logging
from pathlib import Path
import pandas as pd
import numpy as np
from src.config.configuration import Configuration
from src.components.model_prediction import ModelPrediction
from src.components.model_training import ModelTraining



if __name__ == '__main__':

    try: 
        logging.info("Model Evaluation Pipeline Started")
        config = Configuration()
        model_training_config = config.model_training_config()
        model_training = ModelTraining(config=model_training_config)


        model_prediction_config = config.model_prediction_config()
        model_prediction = ModelPrediction(config=model_prediction_config)


        random_states = [12,24,31,42,55]
        r2_list, mse_list, mae_list = [], [], []

        for state in random_states:
            model_training.run_pipeline(random_state=state)
            model_prediction.run_pipeline()
            r2_, mse_score, mae_score = model_prediction.get_results()
            r2_list.append(r2_)
            mse_list.append(mse_score)
            mae_list.append(mae_score)

        logging.critical(f'Average r2_score is: {np.mean(r2_list)}')
        logging.critical(f'Average mse score is: {np.mean(mse_list)}')
        logging.critical(f'Average mae score is: {np.mean(mae_list)}')    
    
    except Exception as e:

        print('error in model evaluation: ', e)


        