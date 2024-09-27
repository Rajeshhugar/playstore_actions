import os
import pandas as pd
from datetime import datetime
from google_play_scraper import Sort, reviews_all

#app_id_lst = ["com.jio.media.jiobeats", "com.spotify.music", "com.bsbportal.music"]

app_id_lst = ["com.tmobile.familycontrols","com.verizon.verizonidauth","com.bsbportal.music"]

# Create the 'artifacts' directory if it doesn't exist
if not os.path.exists('artifacts'):
    os.makedirs('artifacts')

for app_id in app_id_lst:
    result_all = []

    result = reviews_all(
        app_id,
        sleep_milliseconds=0,
        lang='en',
        country='in',
        sort=Sort.NEWEST
    )
    result_all.extend(result)
    
    df = pd.DataFrame(result_all)
    df = df.drop_duplicates()
    print(df.shape)

    today = datetime.now().strftime("%m-%d-%Y_%H%M%S")
    file_name = f'reviews-{app_id}_{today}.parquet'
    file_path = os.path.join('artifacts', file_name)
    
    # Save DataFrame to Parquet
    df.to_parquet(file_path, index=False)
