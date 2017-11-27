def generateClass(name):
        f = open("%s.swift" % (name), 'w')
        f.write("class %s {\n" % (name))
        f.write("func say() {\n")
        f.write("       print(\"Say\")\n")
        f.write("}\n")
        f.write("\n")
        f.write("func hello() {\n")
        f.write("       print(\"Hello\")\n")
        f.write("}\n")
        f.write("}")
        f.close()

def generate(amount):
  for x in range(0, amount):
        generateClass("Class%d" % (x))
        
                           
