import pandas as pd
from app.logger_setup import create_logger

logger = create_logger("WineAnalytics.Loader")

def load_wine_dataset(path: str):
    logger.info(f"Loading wine quality dataset from: {path}")

    try:
        df = pd.read_csv(path, sep=";")
        logger.debug(f"File loaded successfully. Shape: {df.shape}")

        # Log first few columns as a preview
        logger.debug(f"Columns detected: {list(df.columns)}")
        logger.debug("Preview of dataset head:\n" + str(df.head()))

        # Missing value check
        missing = df.isnull().sum().sum()
        if missing > 0:
            logger.warning(f"Dataset contains {missing} missing values.")
        else:
            logger.info("No missing values detected in dataset.")

        return df

    except FileNotFoundError:
        logger.error("Dataset file not found.", exc_info=True)
    except pd.errors.ParserError:
        logger.error("Error parsing the dataset file.", exc_info=True)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
