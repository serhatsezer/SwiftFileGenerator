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
    
    # I'm not sure what im doing
    def anoter_method():
        print("hello")

    def yet_another():
        print("yet another")

    def some_mandotry_method():
        print("hey im important")

    def generate(class_name_prefix, amount):
        for x in range(0, amount):
            generateClass(class_name_prefix + "%d" % (x))


SwiftFile().generate("sample", 1)
