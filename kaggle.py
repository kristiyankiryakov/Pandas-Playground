import pandas as pd

reviews = pd.read_csv('./winemag-data-130k-v2.csv')

# print(reviews.columns)

reviews_written = reviews.groupby('taster_twitter_handle').size()

best_rating_per_price = reviews.groupby('price').points.max()

price_extremes = reviews.groupby('variety').price.agg(['min','max'])

sorted_varieties = price_extremes.sort_values(by=['min','max'],ascending=[False, False])

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

country_variety_counts = reviews.groupby(['country', 'variety']).size()

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

reindexed = reviews.rename_axis("wines", axis='columns')

# print(reindexed)