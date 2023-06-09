# https://ppg.paiza.jp/code_review_bingo/python/8/answers/new

k = ['123', '147', '159', '258', '357', '369', '456', '789']

s="123\n456\n789\n"
xs=[s[i//4::(i%4-1)%5-5][:3]for i in range(44)]
xs=[s[i%9::[1,3,4,5][i//9]][:3]for i in range(36)]
xs=[s[i%9::5-i//9-i//27][:3]for i in range(36)]
ys=sorted(["".join(sorted(x)) for x in xs if len(x)>=3 and ("\n" not in x)])

print(ys, ys==k)

#B=open(0).read();print(sum([x==x&int(B.translate(str.maketrans('#.','10','\n')),2)for x in[73,146,292,7,56,448,273,84]]))
#a=''.join(open(0));print((a+' '.join(a[i::5-i]+' '+a[i*2::4]for i in(0,1,2))).count('###'))
#a=open(0).read();print((a+' '.join(a[i::5-i]+' '+a[i*2::4]for i in(0,1,2))).count('###'))
#t,i='###',input;*a,=i(),i(),i();b=a[0]+a[1]+a[2];i(a.count(t)+[*zip(*a)].count(tuple(t))+(b[0::4]==t)+(b[2:-1:2]==t))

#y="###";s=open(0).read();print(s.count(y)+sum(y==s[i%3::i//3+3][:3]for i in range(9)))
#y,s="###",open(0).read();print(s.count(y)+sum(y==s[i%3::i//3+3][:3]for i in range(9)))
#s=open(0).read();print(s.count("###")+sum("###"==s[i%3::i//3+3][:3]for i in range(9)))
#s=open(0).read();print(s.count("###")+sum("###"==s[i%3+8::i//3-5]for i in range(9)))
#s=open(0).read();print(sum("###"==s[i//4::(i%4-1)%5-5][:3]for i in range(44)))
s=open(0).read();print(sum("###"==s[i%9::5-i//9-i//27][:3]for i in range(36)))
