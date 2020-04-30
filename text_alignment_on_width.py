text = [
    "sdajdksa lksjad kja djkas djkasjd asjkd aksjkdajsd sad as das sdas s",
    "asdasd asdsad asdasd das ss d asdasd",
    "asdasd jkajs jjkk; csnsdan nasdnasd ksadjiksa jsado",
    "sdahdjash hasd asd jhajsdha sjdhsjahd sjd as jdhasdsh ajh h",
    "dsahjdsah jjh jh kasjd k u uk suk usku ksu",
    "sdasd sad ajksd jaksd jkadj kasjdk jaksdj aksjd kajsd kajsdk jaksj dakjsd kajs"
]


def text_alignment_on_width(text):
    max_len = max(list(map(len, text)))
    new_text = list()

    def add_whitespace(line):
        words = line.split()

        def alignment(n_words, max_len):
            new_line = list()
            for i in range(len(n_words)):
                l_words = len(''.join(n_words))

                if max_len > l_words:
                    if i - 1 != 0:
                        n_words[i-1] = f"{' '}{words[i-1]}"
                else:
                    new_line = ''.join(words)
                    new_text.append(new_line)
                    return new_line

            return alignment(n_words, max_len)

        new_line = alignment(words, max_len)  
        return new_line

    for line in text:
        if len(line) <= max_len: 
            add_whitespace(line)
                
    for i in new_text:
        print(i)

if __name__ == "__main__":
    text_alignment_on_width(text)

"""
example:
sdajdksa  lksjad  kja  djkas  djkasjd  asjkd  aksjkdajsd  sad  as  das sdas  s
asdasd        asdsad        asdasd        das        ss        d        asdasd
asdasd      jkajs      jjkk;     csnsdan     nasdnasd     ksadjiksa      jsado
sdahdjash   hasd   asd   jhajsdha   sjdhsjahd   sjd   as   jdhasdsh   ajh    h
dsahjdsah     jjh     jh     kasjd     k     u     uk     suk     usku     ksu
sdasd sad ajksd jaksd jkadj kasjdk jaksdj aksjd kajsd kajsdk jaksj dakjsd kajs
"""
