import split_wiki

assert split_wiki.sanitize_articletitle('Appolo 2/3') == 'Appolo_2_3'
print(split_wiki.sanitize_articletitle('Alger of Liège'))
