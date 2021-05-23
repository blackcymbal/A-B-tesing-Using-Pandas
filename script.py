
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')


most_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()

print (most_views)

#step 3
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.isnull()

#step 4
clicks_by_source =  ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()

#step 6
clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False])*100

#step 7
num_people=ad_clicks.groupby('experimental_group').user_id.count().reset_index()

#step 8
adA_adB = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()

# step 9
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# step 10
click_by_day_A = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()

A_pivot = click_by_day_A\
   .pivot(columns='is_click',
          index='day',
          values='user_id')\
   .reset_index()

A_pivot['percent_clicked'] = A_pivot[True]/(A_pivot[True]+A_pivot[False])

click_by_day_B = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()

B_pivot = click_by_day_B\
   .pivot(columns='is_click',
          index='day',
          values='user_id')\
   .reset_index()

B_pivot['percent_clicked'] = B_pivot[True]/(B_pivot[True]+B_pivot[False])
print (A_pivot)
print (B_pivot)
#print (ad_clicks.head(10))

