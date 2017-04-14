package main

import (
  "fmt"
  "math"
  "time"
)


// First 10 of the Go By Example programs in one - with comments!
// 13rd April 2017

func main() {
  fmt.Println("Hello World!") // Use the fmt library to print to the terminal.

  /*
    Go has various value types including strings, integers, floats, booleans,
    etc. Here are a few basic examples.
  */

  fmt.Println("go" + "lang") // Strings are concat'd with the + operator
  fmt.Println("1+1=", 1+1) // Integers
  fmt.Println("7.0 / 3.0 = ", 7.0 / 3.0) // Floats

  fmt.Println(true && false) // boolean AND
  fmt.Println(true || false) // boolean OR
  fmt.Println(!true) // boolean NOT

  /*
    In Go, variables are explicitly declared and used by the compiler to e.g.
    check type-correctness of function calls.
  */

  var strExample string = "initial" // var declares 1+ variables
  fmt.Println(strExample)

  var one, two int = 1, 2 // you can decalre multiple variables at once.
  fmt.Println(one, two)

  var boolExample = true // Go can infer the type of initialized variables.
  fmt.Println(boolExample)

  var empty int // vars without initializations are **zero-valued**
  fmt.Println(empty) // will print 0

  shortString := "short" // shorthand for declaring + initializing.
  fmt.Println(shortString)

  /*
    Go supports constants of character, string, boolean, and numeric values.
  */

  const strConstant string = "constant" // can appear anywhere a var can.
  const bigNumber = 500000000
  const arbitaryPrecision = 3e20 / bigNumber

  fmt.Println(strConstant)
  fmt.Println(arbitaryPrecision)

  // A numeric constant has no type until given one, such as an explict cast.
  fmt.Println(int64(arbitaryPrecision))
  fmt.Println(math.Sin(bigNumber)) // can also be given type by context used in.

  /*
    for is Go’s only looping construct. Here are three basic types of for loops.
  */

  i := 1
  for i <= 3 {   // most basic, single condition
    fmt.Println(i)
    i = i + 1
  }

  for j := 7; j <= 9; j ++ { // a classic initial/condition/after for loop.
    fmt.Println(j)
  }

  for { // will loop continously until you break out of loop or return from func.
    fmt.Println("loop")
    break
  }

  for n := 0; n <= 5; n++ { // you can also use continue to skip an iteration
    if n % 2 == 0 {
      continue // see?
    }
    fmt.Println(n)
  }

  /*
    Branching with if and else in Go is straight-forward.
  */

  if 7 % 2 == 0 { // typical example
    fmt.Println("7 is even")
  } else {
    fmt.Println("7 is odd")
  }

  if 8 % 4 == 0 { // else is optional
    fmt.Println("8 is divisible by 4")
  }

  if num := 9; num < 0 { // variables declared in if are in all branches.
    fmt.Println(num, "is negative")
  } else if num < 10 {
    fmt.Println(num, "has 1 digit")
  } else {
    fmt.Println(num, "has multoiple digits")
  }

  /*
    Switch statements express conditionals across many branches.
  */
  i = 2
  fmt.Print("Write ", i, " as ")
  switch i { // A simple switch statement
  case 1:
    fmt.Println("one")
  case 2:
    fmt.Println("two")
  case 3:
    fmt.Println("three")
  }

  // You can use commas to seperate multiple expressions in 1 case statement
  switch time.Now().Weekday() {
  case time.Saturday, time.Sunday:
    fmt.Println("It's a weekend")
  default: // optional
    fmt.Println("It's a weekday")
  }

  t := time.Now()
  // Switch without an expression is an alternate way to do if/else logic.
  switch {
  case t.Hour() < 12:
    fmt.Println("It's before noon")
  default:
    fmt.Println("It's after noon")
  }

   // Type switch compares types instead of values.
  whatAmI := func (i interface{}) {
    switch t := i.(type) {
    case bool:
      fmt.Println("I'm a bool")
    case int:
      fmt.Println("I'm an int")
    default:
      fmt.Printf("Don't know type %T\n", t)
    }
  }
  whatAmI(true)
  whatAmI(1)
  whatAmI("hey")

  /*
    In Go, an array is a numbered sequence of elements of a specific length.
  */

  var ary1 [5]int
  fmt.Println("empty:", ary1) // zero valued by default "empty: [0,0,0,0,0]"

  ary1[4] = 100 // You can set a value at index using array[index] = value
  fmt.Println("set:", ary1)
  fmt.Println("get:", ary1[4]) // You can get a value at index using ary[index]
  fmt.Println("len:", len(ary1)) // The builtin len() returns the length of ary.

  ary2 := [5]int{1, 2, 3, 4, 5} // Use to declare + init array in one line.
  fmt.Println("declared:", ary2)

  var ary3 [2][3]int
  for i := 0; i < 2; i++ {
    for j := 0; j < 3; j++ {
      ary3[i][j] = i + j
    }
  }
  fmt.Println("2d: ", ary3)

  /*
    Slices are a key data type in Go, giving a more powerful interface to
    sequences than arrays.
  */

  slice1 := make([]string, 3) // Zero values to "", "" ,""
  slice1[0] = "a"
  slice1[1] = "b"     // set just like arrays.
  slice1[2] = "c"
  fmt.Println("set:", slice1)
  fmt.Println("get:", slice1[2])    // get syntax is the same as arrays too.
  fmt.Println("len:", len(slice1))

  // slice can also be - GASP - appended!
  slice1 = append(slice1, "d")
  slice1 = append(slice1, "e", "f")
  fmt.Println("append:", slice1)

  // slices can also be copied
  slice2 := make([]string, len(slice1))
  copy(slice2, slice1)
  fmt.Println("copy:", slice2)

  // slices support a 'slice' operator with the syntax slice[low:high]
  slice3 := slice1[2:5] // excludes slice1[5]
  fmt.Println("sl1:", slice3)

  slice3 = slice1[:5] // up to but excluiding slice1[5]
  fmt.Println("sl2:", slice3)

  slice3 = slice1[2:] // up from and including slice1[2]
  fmt.Println("sl3:", slice3)

  slice4 := []string{"g", "h", "i"} // same as arrays.
  fmt.Println("declared:", slice4)

  slice5 := make([][]int, 3)
  for i := 0; i < 3; i ++ {
    innerLen := i + 1
    slice5[i] = make([]int, innerLen)
    for j := 0; j < innerLen; j++ {
      slice5[i][j] = i + j
    }
  }

  fmt.Println("2d: ", slice5)

  /*
    Maps are Go’s built-in associative data type (sometimes called hashes or
    dicts in other languages).
  */

  map1 := make(map[string]int) // map[key-type]val-type
  map1["k1"] = 7
  map1["k3"] = 15       // set keys
  map1["k2"] = 13
  fmt.Println("map:", map1)

  value1 := map1["k1"] // get value
  fmt.Println("v1: ", value1)

  fmt.Println("len:", len(map1)) // returns number of key/value pairs.

  delete(map1, "k2") // builtin *delete* removes key/value pair from map
  fmt.Println("map:", map1)

  _, prs := map1["k2"] // optional *prs* value indicates if key was present
  fmt.Println("prs:", prs)

  map2 := map[string]int{"foo": 1, "bar": 2} // declare + init in 1 line.
  fmt.Println("map:", map2)
}
