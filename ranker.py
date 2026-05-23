import pandas as pd

def rank_candidates(results):

    df = pd.DataFrame(results)

    ranked_df = df.sort_values(
        by="Match Score",
        ascending=False
    )

    return ranked_df