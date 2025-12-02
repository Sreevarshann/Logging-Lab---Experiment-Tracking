from app.logger_setup import create_logger

logger = create_logger("WineAnalytics.Analyzer")

def analyze_wine_quality(df):
    logger.info("Starting wine quality analysis...")

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        logger.error("No numeric columns found for analysis.")
        return None

    results = {}

    try:
        for col in numeric_df.columns:

            # Skip the quality label for special handling later
            if col == "quality":
                continue

            try:
                col_mean = numeric_df[col].mean()
                col_min = numeric_df[col].min()
                col_max = numeric_df[col].max()

                results[col] = {
                    "mean": col_mean,
                    "min": col_min,
                    "max": col_max
                }

                logger.debug(
                    f"Processed '{col}' -> mean={col_mean:.3f}, min={col_min:.3f}, max={col_max:.3f}"
                )

            except Exception:
                logger.error(f"Error analyzing column '{col}'", exc_info=True)

        # Special analysis for the 'quality' label
        if "quality" in numeric_df.columns:
            quality_counts = numeric_df["quality"].value_counts().sort_index()
            logger.info("Quality distribution (rating frequency):")
            logger.info("\n" + str(quality_counts))

            results["quality_distribution"] = quality_counts.to_dict()

        logger.info("Wine quality analysis completed successfully.")
        return results

    except Exception:
        logger.error("Unexpected error during wine quality analysis.", exc_info=True)
        return None
