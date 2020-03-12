# ml1m images

This repository provides researchers with URLs to each movie from the ![MovieLens-1M data set](https://grouplens.org/datasets/movielens/1m)  

This can be easily used together with the existing information provided by merging the two CSVs on the item_id column:  
```
import pandas as pd  
ml1m_images = pd.read_csv("ml1m_images.csv")
other_df_with_the_ids.merge(ml1m_images, on="item_id", how="left")
```

The script provides a way to automatically download all images, named accordingly `item_id.jpg`.

