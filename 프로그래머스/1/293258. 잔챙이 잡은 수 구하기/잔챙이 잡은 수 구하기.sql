select count(*) as FISH_COUNT
from fish_info
where length < 10 or length is NULL;