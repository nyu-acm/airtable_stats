"""bd_sum Summing born-digital measurements when unit of measurement is different"""

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