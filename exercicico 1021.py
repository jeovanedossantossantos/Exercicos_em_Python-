valor=float(input())
c100=valor//100
r100=valor%100

c50=r100//50
r50=r100%50

c20=r50//20
r20=r50%20

c5=r20//5
r5=r20%5

c10=r20//10
r10=r20%10

c2=r5//2
r2=r5%2

c1=r2//1
r1=r2%1

c51=r1//0.5
r51=r1%0.5

c25=r51//0.25
r25=r51%0.25

c11=r25//0.10
r11=r25%0.10


c05=r11//0.05
r05=r11%0.05

c01=r05//0.01
r01=r05%0.01

resposta = "NOTAS:\n" + str(int(c100)) + " nota(s) de R$ 100.00\n"+str(int(c50)) + " nota(s) de R$ 50.00\n" + str(int(c20)) + " nota(s) de R$ 20.00\n" + str(int(c10)) + " nota(s) de R$ 10.00\n"

resposta += str(int(c5)) + " nota(s) de R$ 5.00\n" + str(int(c2)) + " nota(s) de R$ 2.00\n" + "MOEDAS:\n" + str(int(c1)) + " moeda(s) de R$ 1.00\n" + str(int(c51)) + " moeda(s) de R$ 0.50\n"
resposta += str(int(c25)) + " moeda(s) de R$ 0.25\n" + str(int(c11)) + " moeda(s) de R$ 0.10\n" + str(int(c05)) + " moeda(s) de R$ 0.05\n" + str(int(c01)) + " moeda(s) de R$ 0.01\n"
print(resposta)
