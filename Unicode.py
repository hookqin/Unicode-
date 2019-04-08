#这个函数是把全文的Unicode编码转换成中文
def zhuanunicode(kkk):
    ds=""
    chang=len(kkk)
    d=0
    while d<chang:
        if kkk[d]=="\\" and kkk[d+1]=="u":
            try:
                asdf="\\"+kkk[d+1:d+6]
                zhuanyi=asdf.encode().decode('unicode-escape')
                ds=ds+zhuanyi.encode('UTF-8','ignore').decode('UTF-8')
                d=d+5
            except Exception as e:
                d=d+5
        else:
            ds=ds+kkk[d].encode('UTF-8','ignore').decode('UTF-8')
        d=d+1
    return ds



#正则实现
def add(temp):
    ds=''
    strNum = temp.group()
    zhuanyi=strNum.encode().decode('unicode-escape')
    ds=ds+zhuanyi.encode('UTF-8','ignore').decode('UTF-8')
    return ds

#调用这个函数把全文的Unicode编码转换成中文
def zhuanma(tex):
    ret = re.sub(r"\\u[\w]{4}", add, tex)
    return ret
