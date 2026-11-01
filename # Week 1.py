# Week 1
# Combines monthly CRMLS files (Jan 2024 - Apr 2026) into two datasets,
# filters both to Residential only, and saves them as new CSVs.

import pandas as pd

# SOLD: read each monthly file
sold_202401 = pd.read_csv('data/CRMLSSold202401.csv', low_memory=False)
sold_202402 = pd.read_csv('data/CRMLSSold202402.csv', low_memory=False)
sold_202403 = pd.read_csv('data/CRMLSSold202403.csv', low_memory=False)
sold_202404 = pd.read_csv('data/CRMLSSold202404.csv', low_memory=False)
sold_202405 = pd.read_csv('data/CRMLSSold202405.csv', low_memory=False)
sold_202406 = pd.read_csv('data/CRMLSSold202406.csv', low_memory=False)
sold_202407 = pd.read_csv('data/CRMLSSold202407.csv', low_memory=False)
sold_202408 = pd.read_csv('data/CRMLSSold202408.csv', low_memory=False)
sold_202409 = pd.read_csv('data/CRMLSSold202409.csv', low_memory=False)
sold_202410 = pd.read_csv('data/CRMLSSold202410.csv', low_memory=False)
sold_202411 = pd.read_csv('data/CRMLSSold202411.csv', low_memory=False)
sold_202412 = pd.read_csv('data/CRMLSSold202412.csv', low_memory=False)
sold_202501 = pd.read_csv('data/CRMLSSold202501.csv', low_memory=False)
sold_202502 = pd.read_csv('data/CRMLSSold202502.csv', low_memory=False)
sold_202503 = pd.read_csv('data/CRMLSSold202503.csv', low_memory=False)
sold_202504 = pd.read_csv('data/CRMLSSold202504.csv', low_memory=False)
sold_202505 = pd.read_csv('data/CRMLSSold202505.csv', low_memory=False)
sold_202506 = pd.read_csv('data/CRMLSSold202506.csv', low_memory=False)
sold_202507 = pd.read_csv('data/CRMLSSold202507.csv', low_memory=False)
sold_202508 = pd.read_csv('data/CRMLSSold202508.csv', low_memory=False)
sold_202509 = pd.read_csv('data/CRMLSSold202509.csv', low_memory=False)
sold_202510 = pd.read_csv('data/CRMLSSold202510.csv', low_memory=False)
sold_202511 = pd.read_csv('data/CRMLSSold202511.csv', low_memory=False)
sold_202512 = pd.read_csv('data/CRMLSSold202512.csv', low_memory=False)
sold_202601 = pd.read_csv('data/CRMLSSold202601.csv', low_memory=False)
sold_202602 = pd.read_csv('data/CRMLSSold202602.csv', low_memory=False)
sold_202603 = pd.read_csv('data/CRMLSSold202603.csv', low_memory=False)
sold_202604 = pd.read_csv('data/CRMLSSold202604.csv', low_memory=False)

# LISTINGS: read each monthly file
list_202401 = pd.read_csv('data/CRMLSListing202401.csv', low_memory=False)
list_202402 = pd.read_csv('data/CRMLSListing202402.csv', low_memory=False)
list_202403 = pd.read_csv('data/CRMLSListing202403.csv', low_memory=False)
list_202404 = pd.read_csv('data/CRMLSListing202404.csv', low_memory=False)
list_202405 = pd.read_csv('data/CRMLSListing202405.csv', low_memory=False)
list_202406 = pd.read_csv('data/CRMLSListing202406.csv', low_memory=False)
list_202407 = pd.read_csv('data/CRMLSListing202407.csv', low_memory=False)
list_202408 = pd.read_csv('data/CRMLSListing202408.csv', low_memory=False)
list_202409 = pd.read_csv('data/CRMLSListing202409.csv', low_memory=False)
list_202410 = pd.read_csv('data/CRMLSListing202410.csv', low_memory=False)
list_202411 = pd.read_csv('data/CRMLSListing202411.csv', low_memory=False)
list_202412 = pd.read_csv('data/CRMLSListing202412.csv', low_memory=False)
list_202501 = pd.read_csv('data/CRMLSListing202501.csv', low_memory=False)
list_202502 = pd.read_csv('data/CRMLSListing202502.csv', low_memory=False)
list_202503 = pd.read_csv('data/CRMLSListing202503.csv', low_memory=False)
list_202504 = pd.read_csv('data/CRMLSListing202504.csv', low_memory=False)
list_202505 = pd.read_csv('data/CRMLSListing202505.csv', low_memory=False)
list_202506 = pd.read_csv('data/CRMLSListing202506.csv', low_memory=False)
list_202507 = pd.read_csv('data/CRMLSListing202507.csv', low_memory=False)
list_202508 = pd.read_csv('data/CRMLSListing202508.csv', low_memory=False)
list_202509 = pd.read_csv('data/CRMLSListing202509.csv', low_memory=False)
list_202510 = pd.read_csv('data/CRMLSListing202510.csv', low_memory=False)
list_202511 = pd.read_csv('data/CRMLSListing202511.csv', low_memory=False)
list_202512 = pd.read_csv('data/CRMLSListing202512.csv', low_memory=False)
list_202601 = pd.read_csv('data/CRMLSListing202601.csv', low_memory=False)
list_202602 = pd.read_csv('data/CRMLSListing202602.csv', low_memory=False)
list_202603 = pd.read_csv('data/CRMLSListing202603.csv', low_memory=False)
list_202604 = pd.read_csv('data/CRMLSListing202604.csv', low_memory=False)

# Row counts BEFORE concatenation
# (Add up the monthly row counts to check against the combined total)
sold_rows_before_concat = (
    len(sold_202401) + len(sold_202402) + len(sold_202403) + len(sold_202404)
    + len(sold_202405) + len(sold_202406) + len(sold_202407) + len(sold_202408)
    + len(sold_202409) + len(sold_202410) + len(sold_202411) + len(sold_202412)
    + len(sold_202501) + len(sold_202502) + len(sold_202503) + len(sold_202504)
    + len(sold_202505) + len(sold_202506) + len(sold_202507) + len(sold_202508)
    + len(sold_202509) + len(sold_202510) + len(sold_202511) + len(sold_202512)
    + len(sold_202601) + len(sold_202602) + len(sold_202603) + len(sold_202604)
)
list_rows_before_concat = (
    len(list_202401) + len(list_202402) + len(list_202403) + len(list_202404)
    + len(list_202405) + len(list_202406) + len(list_202407) + len(list_202408)
    + len(list_202409) + len(list_202410) + len(list_202411) + len(list_202412)
    + len(list_202501) + len(list_202502) + len(list_202503) + len(list_202504)
    + len(list_202505) + len(list_202506) + len(list_202507) + len(list_202508)
    + len(list_202509) + len(list_202510) + len(list_202511) + len(list_202512)
    + len(list_202601) + len(list_202602) + len(list_202603) + len(list_202604)
)
print('Sold rows before concat (sum of monthly files):', sold_rows_before_concat)
print('Listing rows before concat (sum of monthly files):', list_rows_before_concat)

# Concatenate
sold = pd.concat([
    sold_202401, sold_202402, sold_202403, sold_202404,
    sold_202405, sold_202406, sold_202407, sold_202408,
    sold_202409, sold_202410, sold_202411, sold_202412,
    sold_202501, sold_202502, sold_202503, sold_202504,
    sold_202505, sold_202506, sold_202507, sold_202508,
    sold_202509, sold_202510, sold_202511, sold_202512,
    sold_202601, sold_202602, sold_202603, sold_202604,
], ignore_index=True)

listings = pd.concat([
    list_202401, list_202402, list_202403, list_202404,
    list_202405, list_202406, list_202407, list_202408,
    list_202409, list_202410, list_202411, list_202412,
    list_202501, list_202502, list_202503, list_202504,
    list_202505, list_202506, list_202507, list_202508,
    list_202509, list_202510, list_202511, list_202512,
    list_202601, list_202602, list_202603, list_202604,
], ignore_index=True)

# Row counts AFTER concatenation (should match the sums above)
print('Sold rows after concat:', len(sold))
print('Listing rows after concat:', len(listings))

# Check property types, then filter to Residential
print('Sold property types:', sold['PropertyType'].unique())
print('Listing property types:', listings['PropertyType'].unique())

# Row counts BEFORE the Residential filter
print('Sold rows before Residential filter:', len(sold))
print('Listing rows before Residential filter:', len(listings))

sold = sold[sold['PropertyType'] == 'Residential']
listings = listings[listings['PropertyType'] == 'Residential']

# Row counts AFTER the Residential filter
print('Sold rows after Residential filter:', len(sold))
print('Listing rows after Residential filter:', len(listings))

# Save the new CSVs
sold.to_csv('output/sold_residential.csv', index=False)
listings.to_csv('output/listings_residential.csv', index=False)
print('Done!')