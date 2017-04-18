package main

import (
  "fmt"
  "strings"
  "os"
)

func main() {
  target := strings.Split(os.Args[1], "")
  replaceables := os.Args[2]

  var stripped []string
  for _, char := range target {
    if !( strings.Contains(replaceables, char) ) {
      stripped = append(stripped, char)
    }
  }
  fmt.Println(strings.Join(stripped, ""))

}
