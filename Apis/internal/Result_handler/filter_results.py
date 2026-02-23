from General.kafkaContracts import CompletedInfluentialTaskContract, CompletedBulkTaskContract, Results, Output
import numpy as np


def most_common_sentiment_KDE(sentiments: list[float]) -> float:
    sentiments = np.array(sentiments)
    n = len(sentiments)
    sigma = np.std(sentiments)
    h = 1.06 * sigma * (n ** (-1 / 5))

    # --- 2. Create the testing grid ---
    # We will test 1000 points between the min and max of your scores
    x_grid = np.linspace(sentiments.min(), sentiments.max(), 1000)

    # --- 3. The Math (Calculating the KDE) ---
    # We subtract every data point from every grid point
    diffs = x_grid[:, None] - sentiments[None, :]
    z = diffs / h

    # Apply the Gaussian curve formula
    kernels = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * z ** 2)

    # Sum the curves together and normalize by n and h
    density = np.sum(kernels, axis=1) / (n * h)

    # --- 4. Find the Peak (The Mode) ---
    mode_index = np.argmax(density)
    continuous_mode = x_grid[mode_index]

    return continuous_mode.item()


def log_odds_of_sentiments(results: list[Results]) -> list[float]:
    positive = np.array([result.positive for result in results])

    negative = np.array([result.negative for result in results])

    logit = np.log(positive / negative)

    return logit.tolist()


def filter_result(output: CompletedBulkTaskContract | CompletedInfluentialTaskContract) -> Output:
    logit = log_odds_of_sentiments(output.y)

    max_positive_sentiment = max(logit)
    max_negative_sentiment = min(logit)

    most_common_sentiment = most_common_sentiment_KDE(logit)

    filtered = Output(id=output.id,
                      most_positive=max_positive_sentiment,
                      most_negative=max_negative_sentiment,
                      modal_sentiment=most_common_sentiment)

    return filtered
