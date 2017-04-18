package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

func Shuffle(a []string) {
	for i := range a {
		j := rand.Intn(i + 1)
		a[i], a[j] = a[j], a[i]
	}
}

func ShuffleString(str string) []string {
	ary := strings.Split(str, ";")
	Shuffle(ary)
	return ary
}

func lotto(kidstr string, n int) {
	kids := ShuffleString(kidstr)
	originalLength := len(kids)
	kids = append(kids, kids[:n]...)
	for i := 0; i < originalLength; i++ {
		nextFew := kids[i+1 : i+1+n]
		fmt.Println(kids[i], ":", strings.Join(nextFew, "; "))
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())
	input := `Rebbeca Gann;Latosha Caraveo;Jim Bench;Carmelina Biles;Oda Wilhite;Arletha Eason`
	lotto(input, 3)
}
