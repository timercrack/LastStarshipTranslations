import csv
import opencc
import os

file_path = r'd:\Github\LastStarshipTranslations\latest\data\language\chinese_traditional\language.csv'
temp_file_path = file_path + '.tmp'

converter = opencc.OpenCC('s2t')

with open(file_path, 'r', encoding='utf-8', newline='') as infile, \
     open(temp_file_path, 'w', encoding='utf-8', newline='') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    try:
        header = next(reader)
        writer.writerow(header)
        
        # Find the index of 'translation' column
        try:
            translation_idx = header.index('translation')
        except ValueError:
            print("Error: 'translation' column not found.")
            exit(1)

        for row in reader:
            if len(row) > translation_idx:
                row[translation_idx] = converter.convert(row[translation_idx])
            writer.writerow(row)
            
    except StopIteration:
        pass

os.replace(temp_file_path, file_path)
print("Conversion complete.")
