japanese
========

This is a simple python3 script that trains you on the Japanese kana. You can choose between all kana, just hiragana, or just katakana. Items you did not know are shown once you quit the program.

The script reads in two .csv tables. 
"japanese_kana-tables.csv" is a kana-Romanji correspondence table, used in order to generate the quiz items and to generate the Romanji corresponding to the kana. 
The rows are the 5 vowels, with the columns for the different onsets and endings. The columns alternate the hiragana and katakana, in the labels indicated with a trailing "H"/"K". 
In each row, the chokuon are followed by dakuten and hakuten kana, followed by the yooon kana (incomplete at the moment, without the dakuten/hakuten versions). 10/10 + 5/5 + 7/7 
The two "n" kana a added to the o-row (the table dimension are 6x47, including header and first column Romanji). 

"japanese_kana-examples.csv" is a table containing currently one example word per kana, along with its Kanji and an English and German translation. Each kana has its on row.
The columns are: 
kana: the kana character
examplesKana: an example word containing the kana character
examplesKanji: the example as Kanji (if it exists)
examplesRomanji: the example in Romanji
examplesE: the example in English
examplesG: the example in German

Currently, examples for the yooon katakana are missing.


On first usage, the content of the .csv tables is saved in the directory where you run the script as a pickle files ("data.pickle"/"dataExamples.pickle"). Once this is done, the .csv table is no longer needed.

TODO:
1. make colorama library optional
2. complete examples
3. sort errors by kana type
4. add reverse training
5. remember the performance

