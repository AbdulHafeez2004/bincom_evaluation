import numpy as np
import statistics

colours = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN',    'ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE',    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE',  'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN',    'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

new = [9, 6, 9, 3, 5, 12, 5, 6, 7, 1, 7, 2, 8, 5, 8, 5, 5, 5, 9, 4, 3, 9, 3, 5, 5, 10, 12, 12, 7, 7, 2, 8, 5, 8, 8, 5, 5, 5, 9, 6, 9, 3, 5, 12, 2, 6, 7, 2, 7, 2, 5, 5, 8, 5, 5, 8, 8, 5, 5, 9, 8, 5, 3, 12, 6, 7, 1, 7, 2, 8, 5, 8, 5, 5, 5, 9, 9, 8, 9, 3, 5, 5, 11, 8, 7, 2, 2, 2, 8, 5, 8, 5, 5, 5, 8]


new_mean = sum(new)/len(new)

if 0.5 < int(new_mean) < 1.5:
    print( 'Mean: CREAM')
if 1.5 < int(new_mean) < 2.5:
    print( 'Mean: RED')
if 2.5 < int(new_mean) < 3.5:
    print( 'Mean: BROWN')
if 3.5 < int(new_mean) < 4.5:
    print( 'Mean: ARSH')
if 4.5 < int(new_mean) < 5.5:
    print( 'Mean: BLUE')
if 5.5 < int(new_mean) < 6.5:
    print( 'Mean: YELLOW')
if 6.5 < int(new_mean) < 7.5:
    print( 'Mean: ORANGE')
if 7.5 < int(new_mean) < 8.5:
    print( 'Mean: WHITE')
if 8.5 < int(new_mean) < 9.5:
    print( 'Mean: GREEN')
if 9.5 < int(new_mean) < 10.5:
    print( 'Mean: BLEW')
if 10.5 < int(new_mean) < 11.5:
    print( 'Mean: BLACK')
if 11.5 < int(new_mean) < 12.5:
    print( 'Mean: PINK')

mode = statistics.mode(new)
if 0.5 < mode < 1.5:
    print( 'Mode: CREAM')
if 1.5 < mode < 2.5:
    print( 'Mode: RED')
if 2.5 < mode < 3.5:
    print( 'Mode: BROWN')
if 3.5 < mode < 4.5:
    print( 'Mode: ARSH')
if 4.5 < mode < 5.5:
    print( 'Mode: BLUE')
if 5.5 < mode < 6.5:
    print( 'Mode: YELLOW')
if 6.5 < mode < 7.5:
    print( 'Mode: ORANGE')
if 7.5 < mode < 8.5:
    print( 'Mode: WHITE')
if 8.5 < mode < 9.5:
    print( 'Mode: GREEN')
if 9.5 < mode < 10.5:
    print( 'Mode: BLEW')
if 10.5 < mode < 11.5:
    print( 'Mode: BLACK')
if 11.5 < mode < 12.5:
    print( 'Mode: PINK')

median = np.median(new)

if 0.5 < median < 1.5:
    print( 'Median: CREAM')
if 1.5 < median < 2.5:
    print( 'Median: RED')
if 2.5 < median < 3.5:
    print( 'Median: BROWN')
if 3.5 < median < 4.5:
    print( 'Median: ARSH')
if 4.5 < median < 5.5:
    print( 'Median: BLUE')
if 5.5 < median < 6.5:
    print( 'Median: YELLOW')
if 6.5 < median < 7.5:
    print( 'Median: ORANGE')
if 7.5 < median < 8.5:
    print( 'Median: WHITE')
if 8.5 < median < 9.5:
    print( 'Median: GREEN')
if 9.5 < median < 10.5:
    print( 'Median: BLEW')
if 10.5 < median < 11.5:
    print( 'Median: BLACK')
if 11.5 < median < 12.5:
    print( 'Median: PINK')


variance = np.var(new)
if 0.5 < variance < 1.5:
    print( 'Variance: CREAM')
if 1.5 < variance < 2.5:
    print( 'Variance: RED')
if 2.5 < variance < 3.5:
    print( 'Variance: BROWN')
if 3.5 < variance < 4.5:
    print( 'Variance: ARSH')
if 4.5 < variance < 5.5:
    print( 'Variance: BLUE')
if 5.5 < variance < 6.5:
    print( 'Variance: YELLOW')
if 6.5 < variance < 7.5:
    print( 'Variance: ORANGE')
if 7.5 < variance < 8.5:
    print( 'Variance: WHITE')
if 8.5 < variance < 9.5:
    print( 'Variance: GREEN')
if 9.5 < variance < 10.5:
    print( 'Variance: BLEW')
if 10.5 < variance < 11.5:
    print( 'Variance: BLACK')
if 11.5 < variance < 12.5:
    print( 'Variance: PINK')



number_red = new.count(3)
probability = number_red/len(new)
print(f'Probability of choosing red at random is: {probability}')






