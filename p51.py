a=input("Enter text:").strip()
c=a.count(" ") + 1
d = a.replace(" ","")
z = len(d)
print("We have {} words".format(c), 'and {} letters'.format(z))
