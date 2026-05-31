import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "hr_data.csv")
MODEL_PIPELINE_PATH = os.path.join(BASE_DIR, "models", "model_pipeline.pkl")
SHAP_BACKGROUND_PATH = os.path.join(BASE_DIR, "models", "shap_background.pkl")

# ML Parameters
MODEL_THRESHOLD = 0.3
CV_SPLITS = 5
TEST_SIZE = 0.2
RANDOM_STATE = 42

RF_PARAM_GRID = {
    'classifier__n_estimators': [100, 200, 300],
    'classifier__max_depth': [5, 10, None],
}
