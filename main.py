from app.logger_setup import create_logger
from app.wine_loader import load_wine_dataset
from app.quality_analyzer import analyze_wine_quality
import time

def main():
    logger = create_logger("WineAnalytics.Main")
    logger.info("Wine Analytics Application Started.")

    # Start runtime timer
    start_time = time.time()

    # Load dataset
    df = load_wine_dataset("winequality-white.csv")

    if df is None:
        logger.error("Dataset failed to load. Terminating application.")
        return

    # Analyze numeric features
    results = analyze_wine_quality(df)

    if results is None:
        logger.error("Analysis failed. No results to show.")
        return

    # Present results to user
    logger.info("\n=== Wine Feature Summary (mean, min, max) ===\n")
    for col, stats in results.items():

        # Skip the special quality distribution for now
        if col == "quality_distribution":
            continue

        print(f"{col}:")
        print(f"   Mean: {stats['mean']:.3f}")
        print(f"   Min : {stats['min']:.3f}")
        print(f"   Max : {stats['max']:.3f}\n")

    # Display quality distribution
    if "quality_distribution" in results:
        logger.info("\n=== Wine Quality Rating Distribution ===\n")
        print("Quality Rating Counts:")
        for rating, count in results["quality_distribution"].items():
            print(f"   Rating {rating}: {count} samples")

    # End runtime timer
    end_time = time.time()
    total_time = end_time - start_time

    logger.info(f"Analysis runtime: {total_time:.2f} seconds")
    logger.info("Wine Analytics Application Finished Successfully.")

if __name__ == "__main__":
    main()
