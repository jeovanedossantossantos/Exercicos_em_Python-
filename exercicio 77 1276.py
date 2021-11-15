while True:
    try:
        lista=[]
        ac=[]
        df=[]
        gi=[]
        jk=[]
        m=''
        np=[]
        qs=[]
        tv=[]
        wz=[]
        soma=''
        st=input()
        st=st.strip()
        vetor=str(st)
        vetor=list(set(vetor))
        letras_alfabeto=0
        for i in range(len(vetor)):
            if ord(vetor[i]) != 32:
                letras_alfabeto+=1
        if letras_alfabeto == 26:
            print('a:z')
        elif letras_alfabeto != 26:
            mat=[]
            letra=''
            rep=0
            for i in range(len(st)):
                
                letra+=str(st[i])
                if ord(st[i]) != 32:
                    ler=str(st[i])
                    mat.append(ord(ler))
            mat=list(set(mat))
            if (97 in mat) or (98 in mat) or (99 in mat): 
                for i in range(len(mat)):
                    nr=int(mat[i])
                    if nr >= 97 and nr <= 99:
                        rep+=1
                        ac.append(chr(nr))
                        a=min(ac)
                        c=max(ac)
                if (rep == 3) or (a == 'b') or (c == 'b'):
                    soma+= a + ':' + c +','+' '
                elif rep != 0:
                    if a == c:
                        soma+= a+':'+a+','+' '
                    else:
                        soma+=a+':'+a+','+' '+c+':'+c+','+' '
            rep=0
            if (100 in mat) or (101 in mat) or (102 in mat):
                for i in range(len(mat)):
                    nr=int(mat[i])
                    if nr >= 100 and nr <= 102:
                        rep+=1
                        df.append(chr(nr))
                        d=min(df)
                        f=max(df)
                if (rep == 3) or (d == 'e') or (f == 'e'):
                    soma+= d + ':' + f +','+' '
                elif rep != 0:
                    if d == f:
                        soma+= d+':'+d+','+' '
                    else:
                        soma+=d+':'+d+','+' '+f+':'+f+','+' '
            rep=0
            if (103 in mat) or (104 in mat) or (105 in mat):
                for i in range(len(mat)):
                    nr=int(mat[i])
                    if nr >= 103 and nr <= 105:
                        rep+=1
                        gi.append(chr(nr))
                        g=min(gi)
                        ig=max(gi)
                if (rep == 3) or (g == 'h') or (ig == 'h'):
                    soma+= g + ':' + ig +','+' '
                elif rep != 0:
                    if g == ig:
                        soma+= g+':'+g+','+' '
                    else:
                        soma+=g+':'+g+','+' '+ig+':'+ig+','+' '
            rep=0
            if (106 in mat) or (107 in mat) or (108 in mat):
                for i in range(len(mat)):
                    nr=int(mat[i])
                    if nr >= 106 and nr <= 108:
                        rep+=1
                        jk.append(chr(nr))
                        j=min(jk)
                        k=max(jk)
                if (rep == 3) or (j == 'k') or (k == 'k'):
                    soma+= j + ':' + k +','+' '
                elif rep != 0:
                    if j == k:
                        soma+= j+':'+j+','+' '
                    else:
                        soma+=j+':'+j+','+' '+k+':'+k+','+' '
            rep=0

            for i in range(len(mat)):
                nr=int(mat[i])
                if chr(nr) == 'm':
                    m=chr(nr)
                    soma+=m+':'+m+','+' '
            if (110 in mat) or (111 in mat) or (112 in mat):        
                for i in range(len(mat)):
                    nr=int(mat[i])
                    if nr >= 110 and nr <= 112:
                        rep+=1
                        np.append(chr(nr))
                        n=min(np)
                        p=max(np)
                if (rep == 3) or (n == 'o') or (p == 'o'):
                    soma+= n + ':' + p +','+' '
                elif rep != 0:
                    if n == p:
                        soma+= n+':'+n+','+' '
                    else:
                        soma+=n+':'+n+','+' '+p+':'+p+','+' '
            rep=0
            if (113 in mat) or (114 in mat) or (115 in mat):
                for i in range(len(mat)):
                    nr=int(mat[i])
                    if nr >= 113 and nr <= 115:
                        rep+=1
                        qs.append(chr(nr))
                        q=min(qs)
                        s=max(qs)
                if (rep == 3) or (q == 'r') or (s == 'r'):
                    soma+= q + ':' + s +','+' '
                elif rep != 0:
                    if a == c:
                        soma+= q+':'+q+','+' '
                    else:
                        soma+=q+':'+q+','+' '+s+':'+s+','+' '
            rep=0
            if (116 in mat) or (117 in mat) or (118 in mat):
                for i in range(len(mat)):
                    nr=int(mat[i])
                    if nr >= 116 and nr <= 118:
                        rep+=1
                        tv.append(chr(nr))
                        t=min(tv)
                        v=max(tv)
                if (rep == 3) or (t == 'u') or (v == 'u'):
                    soma+= t + ':' + v +','+' '
                elif rep != 0:
                    if t == v:
                        soma+= t+':'+v+','+' '
                    else:
                        soma+=t+':'+t+','+' '+v+':'+v+','+' '
            rep=0
            rep=0
            if (119 in mat) or (120 in mat) or (121 in mat) or (122 in mat):
                for i in range(len(mat)):
                    nr=int(mat[i])
                    if nr >= 119 and nr <= 122:
                        rep+=1
                        wz.append(chr(nr))
                        w=min(wz)
                        z=max(wz)
                total=len(wz)
                bre=chr(ord(w)+1) == chr(ord(z)-1)
                if (total == 4) or ((bre == True) and (total != 2)):
                    soma+= w + ':' + z +','+' '
                elif total == 2:
                    soma+=w+':'+w+','+' '+z+':'+z+','+' '
                elif total == 1:
                    soma+= w+':'+w+','+' '
                else:
                    soma+= w+':'+w+','+' '+ str(wz[0]) +':'+str(wz[0])+','+' '+z+':'+z+','+' '
            tempo=0
            outro=len(soma)
            s=''
            for i in range(outro):
                tempo+=1
                s+=soma[i]
                if tempo==40:
                    s=(s[:-1])
                    s+='\n'
            print(s[:-2])
        else:
            print()
    except EOFError:
        break
