import zipfile
file_zip = zipfile.ZipFile('voina-i-mir.zip')
file_zip.extractall()
text_file = open('voyna-i-mir.txt','r', encoding = 'utf-8')
text = text_file.read()
count = 0
let_dict = {}
for let in text:
    if let.isalpha():
        count += 1
        if let in let_dict:
            let_dict[let] += 1
        else:
            let_dict[let] = 1
text_file.close()
analys_file = open('analysis.txt', 'w')
sorted_let = sorted(let_dict.items(), key= lambda item: (-item[1], item[0]))
for tpl in sorted_let:
    analys_file.write(f'{tpl[0]} {round(tpl[1]/count, 3)}\n')
analys_file.close()