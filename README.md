# SwiftFileGenerator
This little python script generates Swift files with class and method declarations.

## Usage
Simply run this python file on terminal using python command or call related method in your class.

Below code create Product swift files associate with given prefix and amount. 
```python
# param1: Class prefix 
# param2: Amount of value you want to create
generate("Product", 15)
```
**Class output will be something like this below**

```swift
class Product0 {
    func say() {
        print("Say")
    }
    
    func hello() {
        print("Hello")
    }
}
```
**File output will be something like this below**

![alt text](https://raw.githubusercontent.com/serhatsezer/SwiftFileGenerator/master/output.png "Logo Title Text 1")
