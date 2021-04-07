"""accession_stats.py Creates standard accession stats from Airtable download"""

#This script takes a csv export of the "Accessioning Stats" view from Airtable
#and performs calculations to produce a standard set of statistics
#on accessioning activities. The export must include the same columns, in the same
#order, as this view to produce correct calculations. Born-digital extents are calculated
#in terabytes.

import csv

"""Replace this file with your export"""
my_file = 'completed_accessions_20_21.csv'

fh = open(my_file)
next(fh)

"""Counting and summing variables"""
count_complete_fales = 0
count_complete_tam = 0
count_complete_ua = 0

sum_complete_fales = 0
sum_complete_tam = 0
sum_complete_ua = 0

bd_sum_fales = 0
bd_sum_tam = 0
bd_sum_ua = 0

count_open_fales = 0
count_open_tam = 0
count_open_ua = 0

sum_open_fales = 0
sum_open_tam = 0
sum_open_ua = 0

"""Loop through csv file"""
for line in fh:
    items = line.split(',')
    accn_id = items[0]
    repo = items[1]
    post_extent = items[3]
    if post_extent == '':
        post_extent = 0
    post_extent = float(post_extent)
    bd_extent = items[4]
    if bd_extent == '':
        bd_extent = 0
    bd_extent = float(bd_extent)
    bd_measure = items[5]
    if bd_measure == 'KB':
        bd_extent = bd_extent / 1e9
    if bd_measure == 'MB':
        bd_extent = bd_extent / 1e6
    if bd_measure == 'GB':
        bd_extent = bd_extent / 1000
    resource_published = items[8]
    if repo == 'Fales':
        count_complete_fales = count_complete_fales + 1
        sum_complete_fales = sum_complete_fales + post_extent
        bd_sum_fales = bd_sum_fales + bd_extent
        if resource_published == 'Y':
            count_open_fales = count_open_fales + 1
            sum_open_fales = sum_open_fales + post_extent
    if repo == 'Tamiment':
        count_complete_tam = count_complete_tam + 1
        sum_complete_tam = sum_complete_tam + post_extent
        bd_sum_tam = bd_sum_tam + bd_extent
        if resource_published == 'Y':
            count_open_tam = count_open_tam + 1
            sum_open_tam = sum_open_tam + post_extent
    if repo == 'University Archives':
        count_complete_ua = count_complete_ua + 1
        sum_complete_ua = sum_complete_ua + post_extent
        bd_sum_ua = bd_sum_ua + bd_extent
        if resource_published == 'Y':
            count_open_ua = count_open_ua + 1
            sum_open_ua = sum_open_ua + post_extent

"""Uncomment this section if you want to print results to the console"""
# print(f'Completed Accessions(count) for Fales: {count_complete_fales}')
# print(f'Completed Accessions(count) for Tamiment: {count_complete_tam}')
# print(f'Completed Accessions(count) for UA: {count_complete_ua}')
# count_complete_all_repos = count_complete_fales + count_complete_tam + count_complete_ua
# print(f'Completed Accessions(count) for all repos: {count_complete_all_repos}')
# print('=' * 10)
# print(f'Completed Accessions(extent) for Fales: {sum_complete_fales}')
# print(f'Completed Accessions(extent) for Tamiment: {sum_complete_tam}')
# print(f'Completed Accessions(extent) for UA: {sum_complete_ua}')
# sum_complete_all_repos = sum_complete_fales + sum_complete_tam + sum_complete_ua
# print(f'Completed Accessions(extent) for all repos: {sum_complete_all_repos}')
# print('=' * 10)
# print(f'Born-digital extent accessioned for Fales: {round(bd_sum_fales, 2)} TB')
# print(f'Born-digital extent accessioned for Tamiment: {round(bd_sum_tam, 2)} TB')
# print(f'Born-digital extent accessioned for UA: {round(bd_sum_ua, 2)} TB')
# bd_sum_all_repos = bd_sum_fales + bd_sum_tam + bd_sum_ua
# print(f'Born-digital extent accessioned for all repos: {round(bd_sum_all_repos, 2)} TB')
# print('=' * 10)
# print(f'Opened Accessions(count) for Fales: {count_open_fales}')
# print(f'Opened Accessions(count) for Tamiment: {count_open_tam}')
# print(f'Opened Accessions(count) for UA: {count_open_ua}')
# count_open_all_repos = count_open_fales + count_open_tam + count_open_ua
# print(f'Opened Accessions(count) for all repos: {count_open_all_repos}')
# print('=' * 10)
# print(f'Opened Accessions(extent) for Fales: {sum_open_fales}')
# print(f'Opened Accessions(extent) for Tamiment: {sum_open_tam}')
# print(f'Opened Accessions(extent) for UA: {sum_open_ua}')
# sum_open_all_repos = sum_open_fales + sum_open_tam + sum_open_ua
# print(f'Opened Accessions(extent) for all repos: {sum_open_all_repos}')

#Write results to a new file (change file name as needed)
result_file = 'accession_results.txt'
wfh = open(result_file, 'w', newline='')
#writer = csv.writer(wfh)                       #uncomment and change file extention of result_file if you want a csv

wfh.write(f'Completed Accessions(count) for Fales: {count_complete_fales}\n')
wfh.write(f'Completed Accessions(count) for Tamiment: {count_complete_tam}\n')
wfh.write(f'Completed Accessions(count) for UA: {count_complete_ua}\n')
count_complete_all_repos = count_complete_fales + count_complete_tam + count_complete_ua
wfh.write(f'Completed Accessions(count) for all repos: {count_complete_all_repos}\n')
wfh.write(f'==========\n')
wfh.write(f'Completed Accessions(extent) for Fales: {sum_complete_fales}\n')
wfh.write(f'Completed Accessions(extent) for Tamiment: {sum_complete_tam}\n')
wfh.write(f'Completed Accessions(extent) for UA: {sum_complete_ua}\n')
sum_complete_all_repos = sum_complete_fales + sum_complete_tam + sum_complete_ua
wfh.write(f'Completed Accessions(extent) for all repos: {sum_complete_all_repos}\n')
wfh.write(f'==========\n')
wfh.write(f'Born-digital extent accessioned for Fales: {round(bd_sum_fales, 2)} TB\n')
wfh.write(f'Born-digital extent accessioned for Tamiment: {round(bd_sum_tam, 2)} TB\n')
wfh.write(f'Born-digital extent accessioned for UA: {round(bd_sum_ua, 2)} TB\n')
bd_sum_all_repos = bd_sum_fales + bd_sum_tam + bd_sum_ua
wfh.write(f'Born-digital extent accessioned for all repos: {round(bd_sum_all_repos, 2)} TB\n')
wfh.write(f'==========\n')
wfh.write(f'Opened Accessions(count) for Fales: {count_open_fales}\n')
wfh.write(f'Opened Accessions(count) for Tamiment: {count_open_tam}\n')
wfh.write(f'Opened Accessions(count) for UA: {count_open_ua}\n')
count_open_all_repos = count_open_fales + count_open_tam + count_open_ua
wfh.write(f'Opened Accessions(count) for all repos: {count_open_all_repos}\n')
wfh.write(f'==========\n')
wfh.write(f'Opened Accessions(extent) for Fales: {sum_open_fales}\n')
wfh.write(f'Opened Accessions(extent) for Tamiment: {sum_open_tam}\n')
wfh.write(f'Opened Accessions(extent) for UA: {sum_open_ua}\n')
sum_open_all_repos = sum_open_fales + sum_open_tam + sum_open_ua
wfh.write(f'Opened Accessions(extent) for all repos: {sum_open_all_repos}\n')

wfh.close()
fh.close()