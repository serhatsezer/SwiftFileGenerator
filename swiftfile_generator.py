class SwiftFile:
   
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
    def anoter_method():
        print("hello")

    def generate(class_name_prefix, amount):
        for x in range(0, amount):
            generateClass(class_name_prefix + "%d" % (x))


SwiftFile().generate("sample", 1)
