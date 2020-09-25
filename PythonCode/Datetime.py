from dateutil.parser import parse

date_array = [
    '2018-06-29 08:15:27.243860',
    'Jun 28 2018 7:40AM',
    'Jun 28 2018 at 7:40AM',
    'September 18, 2017, 22:19:55',
    'Sun, 05/12/1999, 12:30PM',
    'Mon, 21 March, 2015',
    '2018-03-12T10:12:45Z',
    '2018-06-29 17:08:00.586525+00:00',
    '2018-06-29 17:08:00.586525+05:00',
    'Tuesday , 6th September, 2017 at 4:30pm'
]

for date in date_array:
    #cls
    # print('Parsing: ' + date)
    dt = parse(date)
    #print(date)
    print(dt.date())
    #print(dt.time())
    #print(dt.tzinfo)
    #print('\n')