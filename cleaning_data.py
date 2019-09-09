import hdf5_getters as yay
import glob, os

'All rows are inputted to a list and hence written to a file'
os.chdir("F:/sem4/ml/project/MillionSongSubset/data/A")
file=[]
for data in glob.glob('*.h5'):
    file.append(data)

'Out of 57 predictors unwanted columns are removed and we now have 11 columns'

duration=[]
artist_familiarity=[]
artist_hotttnesss=[]
tempo=[]
loudness=[]
key=[]
time_signature=[]
end_of_fade_in=[]
mode=[]
start_of_fade_out=[]
song_hotttnesss=[]

for i in range(0,len(file)):
    h5 = yay.open_h5_file_read('F:\sem4\ml\project\MillionSongSubset\data\A\{}'.format(file[i]))
    duration.append(yay.get_duration(h5))
    artist_familiarity.append(yay.get_artist_familiarity(h5))
    artist_hotttnesss.append(yay.get_artist_hotttnesss(h5))
    tempo.append(yay.get_tempo(h5))
    loudness.append(yay.get_loudness(h5))
    key.append(yay.get_key(h5))
    time_signature.append(yay.get_time_signature(h5))
    end_of_fade_in.append(yay.get_end_of_fade_in(h5))
    mode.append(yay.get_mode(h5))
    start_of_fade_out.append(yay.get_start_of_fade_out(h5))
    song_hotttnesss.append(yay.get_song_hotttnesss(h5))

rows = zip(duration,artist_familiarity,artist_hotttnesss,tempo,loudness,key,time_signature,
           end_of_fade_in,mode,start_of_fade_out,song_hotttnesss)

import csv

with open('training_data.csv', "w", encoding="ISO-8859-1", newline='') as f:
    fieldnames = ['duration','artist_familiarity','artist_hotttnesss','tempo','loudness','key','time_signature',
                  'end_of_fade_in','mode','start_of_fade_out','song_hotttnesss']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

with open('training_data.csv','a',encoding="ISO-8859-1", newline='') as fd:
    writer = csv.writer(fd)
    for row in rows:
        writer.writerow(row)
