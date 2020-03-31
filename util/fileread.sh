line=$(head -n 1 'out.txt')
sqlite3 -header -csv  $line "select * from moz_places;" > track.csv
  
sqlite3 -header -csv $line "select * from moz_historyvisits" >track1.csv
