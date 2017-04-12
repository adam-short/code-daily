package main

import "fmt"

// I just started learning go, so this is just a review/practise of functions.
          // 12th April 2017

func main() {
  fmt.Println("Hello!")

  fmt.Println(addXY(5, 3))
  fmt.Println(mulXY(5, 3))
  fmt.Println(subYFromX(5, 3))

  add10 := addXThenY(10)
  mul2 := mulXThenY(2)
  subFrom3 := subYFromXPartial(3)

  fmt.Println(add10(5))
  fmt.Println(mul2(10))
  fmt.Println(subFrom3(5))

  fmt.Println(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
  fmt.Println(sentence("Go", "Is", "An", "Easy", "Language."))

  simpleSlice := []string{"The", "simplicity", "comes from", "the limited syntax."}
  fmt.Println(sentence(simpleSlice...))
}


  // Standard functions
func addXY(x, y int) int {
  return x + y
}

func mulXY(x int, y int) int {
  return x * y
}

func subYFromX(x, y int) (z int) {
  z = x - y
  return
}


  // Curried functions
func addXThenY(x int) func(int) int {
  return func (y int) int {
    return x + y
  }
}

func mulXThenY(x int) func(int) int {
  return func (y int) int {
    return x * y
  }
}

func subYFromXPartial(x int) func(int) (z int) { // wow, long function signature.
  return func (y int) (z int) {
    z = x - y
    return
  }
}

  // Varidac Arguments
func sum(numbers ...int) (total int) {
  total = 0
  for _, number := range numbers {
    total += number
  }

  return
}

func sentence(words ...string) string {
  end := ""
  for _, word := range words {
    end += " " + word
  }

  return end
}
