def formata(palavra):
    res = palavra.replace("á",'a')
    res = res.replace("é",'e')
    res = res.replace("í",'i')
    res = res.replace("ó",'o')
    res = res.replace("ú",'u')

    res = res.replace("â",'a')
    res = res.replace("ê",'e')
    res = res.replace("î",'i')
    res = res.replace("ô",'o')
    res = res.replace("û",'u')

    res = res.replace("ã",'a')
    res = res.replace("õ",'o')

    res = res.replace("à",'a')

    return res

    