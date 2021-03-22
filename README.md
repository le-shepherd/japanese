japanese
========

This is a simple python3 script that trains you on the Japanese kana. You can choose between all kana, just hiragana, or just katakana. Items you did not know are shown once you quit the program.

The script reads in two .csv files. 
"japanese_kana-tables.csv" is a kana-Romanji correspondence table, used in order to generate the quiz items and to generate the Romanji corresponding to the kana. 
The rows are the 5 vowels, with the columns for the different onsets. The columns alternate the hiragana and katakana, in the labels indicated with a trailing "H" for hiragana and "K" for katakana, respectively. 
In each row, the 20 chokuon (single sound kanas) are followed by 8 dakuten (the "゛" indicating voicing) and 2 handakuten (the "゜" turning *h* into *p* ) kana), followed by the 14 yooon kana, that is, the combinations of the kana of the *i* series with either *ya*, *yu*, or *yo* (incomplete at the moment, without the dakuten/handakuten versions). 
The two "n" kanas are added to the o-row. The resulting table dimensions are 6x47, including a header and the first column Romanji). 

"japanese_kana-examples.csv" is a table containing currently one example word per kana, along with its Kanji and an English and German translation. Each kana has its on row.
The columns are: 
"kana" (the kana character), "examplesKana" (an example word containing the kana character), "examplesKanji" (the example as Kanji (if it exists)), "examplesRomanji" (the example in Romanji), "examplesE" (the example in English), "examplesG" (the example in German).

Currently, examples for the yooon katakana are missing.


On first usage, the content of the .csv tables is saved in the directory where you run the script as a pickle files ("data.pickle"/"dataExamples.pickle"). Once this is done, the .csv table is no longer needed.

TODO:
1. make colorama library optional
2. complete examples
3. sort errors by kana type
4. add reverse training
5. remember the performance

