from itertools import product
import sys
sys.path.append('d:\\ws\\AoC2025\\02')
import day2

ranges = day2.load_data('input.txt')
invalid_ids = set()
for start,end in ranges:
    istart=int(start); iend=int(end)
    startlen=len(start); endlen=len(end)
    if startlen%2==1: startlen+=1
    for length in range(startlen, endlen+1,2):
        for half in product('0123456789', repeat=length//2):
            fullid = int(''.join(half+half))
            if istart <= fullid <= iend:
                invalid_ids.add(fullid)

print('unique invalid ids:', len(invalid_ids))
print('sum:', sum(invalid_ids))
print('min,max:', min(invalid_ids) if invalid_ids else None, max(invalid_ids) if invalid_ids else None)
ss = sorted(invalid_ids)
print('first 10:', ss[:10])
print('last 10:', ss[-10:])
for i,(start,end) in enumerate(ranges[:10]):
    istart=int(start); iend=int(end)
    cnt=sum(1 for x in invalid_ids if istart<=x<=iend)
    print(f'range {i} {start}-{end}: {cnt} matches')
