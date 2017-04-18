package main

import (
	"fmt"
	"os"
	"strconv"
  "sort"
)

func main() {
	strList := os.Args[1:]
	numberList := make([]int, 0)

	for _, str := range strList {
		num, _ := strconv.Atoi(str)
		numberList = append(numberList, num)
	}

  sort.Ints(numberList)

	fmt.Println(numberList)
}
