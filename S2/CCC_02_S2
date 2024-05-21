nemu = int(input())
deno = int(input())


Max = nemu
Min = deno

gcf = ''

Rem = 0

what = ''

while True:
  Rem = Max % Min
  if Rem == 0:
    gcf = Min
    break
  else: Max = Min; Min = Rem

deno = deno/gcf
nemu = nemu/gcf


if nemu % deno == 0:
  print(int(nemu/deno))
elif nemu > deno:
  num = nemu // deno
  print(int(num), str(int(nemu - num*deno)) + "/" + str(int(deno)))
else: print(str(int(nemu)) + "/" + str(int(deno)))
