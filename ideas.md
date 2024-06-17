# ideas
 Ideas for the programming language

- **Iterative applyer**: use 'obj->name(args)' to call the 'name' attribute on *each* element of obj (obj must be an iterable like a string or array). For example:
```
x = string{"hey", "how", "are", "you"}
print(x->upper()) // {'HEY', 'HOW', 'ARE', 'YOU'}
```
- **String concatenation**: easier string concatenation
```
x = 7
print($"My luckiest number is {x}")
```
- **Function expressions**: anonymous functions that can be created as an expression
```
print((int a) => {
    print(a)
}(6 + 4))
```
- **Events**: events for when an object changed
```
i = 5
i.changed((int new) => {
    print($"New value is {new}")
})

SLEEP 5 // pseudo-code for making the program sleep for 5 seconds
i = 1
SLEEP 1
```
- **thread keyword**: the simplest way to create a thread there could *possibly* be.
```
func test(int a, int b) -> int {
    i = a
    while i < b {
        i++
    }

    return i - a
}

t = thread test(1, ONE_BILLION) // thread automatically starts
print(t)

t.finished(() => {
    print(t.result)
})
```
- **User-defined Classes**: Define custom objects
```
class Person {
    string name
    int age

    func init(string name, int age) {
        self.name = name
        self.age = age
    }
}

class Employee <- Person {
    int pay
    
    func init(string name, int age, int pay) {
        super.init(name, age)

        self.pay = pay
    }

    func take_holiday() {
        print($"{name} is on a holiday now!")
    }

    func work() {
        print($"{name} is working...")
    }
}

class Programmer <- Employee {
    string language

    func init(string name, int age, int pay, string language) {
        super.init(name, age, pay)

        self.language = language
    }

    func override repr() -> string {
        return $"Programmer(name={name}, language={language})"
    }

    func override work() {
        print($"{name} is programming in {language}")
    }
}
```
