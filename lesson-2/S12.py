words=input("So'zlarni vergul biln ajratib yozing")
if ',' in words:
    words=words.split(',')
else:
    words=words.split()
words=[word.strip() for word in words]
separator=input("So'zlarni qanday belgi bilan ajratishni xohlaysiz?")
joined_string=separator.join(words)
print("yakuniy matn:", joined_string)