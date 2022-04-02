T=int(input())
while -273<=T<6000:
  if T>100:
    print("Steam")
  if T<0:
    print("Ice")
  if not T<0 and not T>100:
    print("Water")
  break
