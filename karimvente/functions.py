from .settings import MEDIA_ROOT

def handle_upload_file(folder, file_name, f):
    
    file = "%s/%s/%s" % (MEDIA_ROOT, folder, file_name)
    with open(file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Fonction qui va parser le resultat du forms.CharField
# avec le widget SelectMultipleField en liste au lieu d'une chaine
# de caractère
def parse_select_multiple(string):

    datas = []

    begin = False
    value = ""

    for s in string:
        
        if s == '\'':
            begin = not begin
        
        if begin:
            if s not in "'[], ":
                value += s
        else:
            datas.append(value)
            value = ""

    datas = list(filter(lambda x: len(x) > 1, datas))
    return datas