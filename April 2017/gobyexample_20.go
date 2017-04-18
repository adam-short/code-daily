package main

import (
	"fmt"
	"math"
)

func plus(a int, b int) int { // takes two ints and returns sum as an int.
	return a + b
}

// when you have multiple consec. params of same type, you can omit type name.
func plusPlus(a, b, c int) int {
	return a + b + c
}

// go has support for multiple return values. It's very idiomatic.
func vals() (int, int) {
	return 3, 7
}

func printSum(nums ...int) { // a function that takes an arb. number of ints.
	fmt.Print(nums, " ")
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func intSeq() func() int { // go supports anonymous/first class functions
	i := 0
	return func() int {
		i += 1 // closures!!
		return i
	}
}

// recursion! fuck YES!
func fact(n int) int {
	if n == 0 {
		return 1
	}

	return n * fact(n-1)
}

func zeroval(ival int) { // classical value function
	ival = 0
}

func zeroptr(iptr *int) { // same function as zeroval, but using pointers.
	*iptr = 0
}

// structs are typed collections of fields.
type person struct {
	name string
	age  int
}

type rect struct {
	width, height float64
}

// go supports methods defined on struct types.
func (r rect) area() float64 {
	return r.width * r.height
}

func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// interfaces are named collections of method signatures.
type geometry interface {
	area() float64
	perim() float64
}

type circle struct {
	radius float64
}

// to implement an interface, just implement all methods in the interface.
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	/*
	   range iterates over elements in a variety of data structures. Let’s see
	   how to use range with some of the data structures we’ve already learned.
	*/
	numbers := []int{2, 3, 4}
	sum := 0

	for _, num := range numbers {
		sum += num
	}
	fmt.Println("sum:", sum)

	//range on arrays + slices provides both index and value for each entry.
	for i, num := range numbers {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	mp1 := map[string]string{"a": "apple", "b": "banana"}

	for k, v := range mp1 { // iterates over the maps key/value pairs.
		fmt.Printf("%s -> %s\n", k, v)
	}

	for k := range mp1 { // you can iterate with just keys.
		fmt.Println("key:", k)
	}

	for i, c := range "go" { // range on strings iterates over Unicode points.
		fmt.Println(i, c)
	}

	/*
	   Functions are central in Go. We’ll learn about functions with a few
	   different examples.
	*/

	result1 := plus(1, 2)
	fmt.Println("1+1=", result1)

	result1 = plusPlus(1, 2, 3)
	fmt.Println("1+2+3=", result1)

	/*
	   Go has built-in support for multiple return values. This feature is used
	   often in idiomatic Go, for example to return both result and error values
	   from a function.
	*/

	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	_, c := vals()
	fmt.Println(c)

	/*
	   Variadic functions can be called with any number of trailing arguments.
	   For example, fmt.Println is a common variadic function.
	*/

	printSum(1, 2)
	printSum(1, 2, 3)

	nums := []int{1, 2, 3, 4} // slice can be passed as multiple args with ...
	printSum(nums...)

	/*
	   Go supports anonymous functions, which can form closures. Anonymous
	   functions are useful when you want to define a function inline without
	   having to name it.
	*/

	nextInt := intSeq()

	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	newInts := intSeq()
	fmt.Println(newInts())

	/*
	   Go supports recursive functions. Here’s a classic factorial example.
	*/

	fmt.Println(fact(7))

	/*
	   Go supports pointers, allowing you to pass references to values and
	   records within your program.
	*/

	point1 := 1
	fmt.Println("initial:", point1) // ====> 1

	zeroval(point1)
	fmt.Println("zeroval:", point1) // ====> 1

	zeroptr(&point1)                // & gets memory addres of i.
	fmt.Println("zeroptr:", point1) // ====> 0

	fmt.Println("pointer:", &point1) // prints the memory address.

	/*
	   Go’s structs are typed collections of fields. They’re useful for grouping
	   data together to form records.
	*/

	fmt.Println(person{"Bob", 20})              // creates a new struct
	fmt.Println(person{name: "Alice", age: 30}) // fields can also be named.
	fmt.Println(person{name: "Fred"})           // omitted fields are zero-valued.
	fmt.Println(&person{name: "Ann", age: 40})  // & yields pointer to struct.

	smplPerson := person{name: "Sean", age: 50}
	fmt.Println(smplPerson.name) // access struct fields with a dot ( . )

	smplPersonPointer := &smplPerson
	fmt.Println(smplPersonPointer.age) // pointer automatically dereferenced.

	smplPersonPointer.age = 51 // structs are mutable.
	fmt.Println(smplPersonPointer.age)

	/*
	   Go supports methods defined on struct types.
	*/

	rectangle := rect{width: 10, height: 5}
	fmt.Println("area: ", rectangle.area())
	fmt.Println("perim:", rectangle.perim()) // method call.

	// go automatically handles conversion between values/pntrs for method calls.
	// you may want to use a pointer receiever type to avoid copying on method
	// calls or to allow the method to mutate the receiving struct.
	rectanglePntr := &rectangle
	fmt.Println("area: ", rectanglePntr.area())
	fmt.Println("permi:", rectanglePntr.perim())

	/*
	   Interfaces are named collections of method signatures.
	*/

	// if a variable has an interface type then we can call methods that are in
	// the named interface.
	circle := circle{radius: 5}

	measure(rectangle)
	measure(circle)

}
