import pandas as pd

# # Google Play Store vs. Apple App Store comparison
# play = pd.read_csv('resources/raw/playstore.csv')
# play.drop(
#     columns=['Free', 'Size', 'Developer Id', 'Developer Website', 'Developer Email', 'Content Rating', 'Privacy Policy',
#              'Editors Choice', 'Scraped Time', 'Installs', 'Minimum Installs', 'Currency'],
#     axis=1,
#     inplace=True)
# play = play[play['Rating Count'] > 1000]
# play = play[play['Rating'] > 4.2]
# play = play.iloc[0:5000]
# play.to_csv('resources/filtered/playstore_filtered.csv')
#
# app = pd.read_csv('resources/raw/appstore.csv')
# app.drop(
#     columns=['AppStore_Url', 'Size_Bytes', 'Version', 'Currency', 'Free', 'DeveloperId', 'Developer', 'Developer_Url',
#              'Developer_Website', 'Current_Version_Score', 'Current_Version_Reviews'],
#     axis=1,
#     inplace=True
# )
# app = app[app['Reviews'] > 10]
# app = app.iloc[0:5000]
# app.to_csv('resources/filtered/appstore_filtered.csv')
#
#
# # CBR, CDR, HDI Comparison
# cbr = pd.read_csv('resources/raw/cbr_1000.csv', index_col='country')
# cdr = pd.read_csv('resources/raw/cdr_1000.csv', index_col='country')
# hdi = pd.read_csv('resources/raw/hdi.csv', index_col='country')
#
# # print(hdi.at('Andorra', '1990'))
#
# hdi = hdi.dropna(axis='index', how='any', subset=['2000'])
#
# cbr_ind = cbr.index
# cdr_ind = cdr.index
# hdi_ind = hdi.index
#
# all_ind = cbr_ind.intersection(cdr_ind.intersection(hdi_ind))
#
# cbr = cbr.loc[all_ind]
# cdr = cdr.loc[all_ind]
# hdi = hdi.loc[all_ind]
#
# cbr.to_csv('resources/filtered/cbr_1000_filtered.csv')
# cdr.to_csv('resources/filtered/cdr_1000_filtered.csv')
# hdi.to_csv('resources/filtered/hdi_1000_filtered.csv')

# crime = pd.read_csv('resources/raw/sacramento_crime_2006.csv')
# crime = crime.drop(columns=['beat', 'district', 'grid'])
# crime.to_csv('resources/filtered/sacramento_crime_2006_filtered.csv')
