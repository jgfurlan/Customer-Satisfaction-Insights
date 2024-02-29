from zenml import pipeline

from steps.data_cleaner import clean_df
from steps.ingest_data import ingest_df
from steps.evaluation import evaluate_model
from steps.model_train import train_model

@pipeline
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)
    
