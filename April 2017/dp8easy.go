package main

import (
	"fmt"
	"strconv"
)

func recursebottles(n int, start string) string {
	beers := strconv.Itoa(n)

	poem := start
	if n > 0 {
		poem = poem + beers + " bottles of beer on the wall. "
		poem = poem + beers + " bottles of beer on the wall. "
		poem = poem + "take one down, pass it around, "
		if n == 1 {
			poem = poem + "no more bottles of beer on the wall."
		} else {
			poem = poem + recursebottles(n-1, "")
		}
	}

	return poem
}

// daily programmer # 8 - easy
func main() {
	fmt.Println(recursebottles(100, ""))
}
