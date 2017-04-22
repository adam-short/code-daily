package main

import (
  "fmt"
  "strconv"
  "strings"
  "os"
)

// print triangle of user specified height

func triangleLayers(height int) []int {
  layers := []int{1}
  for i := 1; i <= height-1; i++ {
    layers = append(layers, i+i)
  }

  return layers
}

func printLayers(layers []int) []string {
  var triangle []string
  for _, l := range layers {
    triangle = append(triangle, strings.Repeat("@", l))
  }

  return triangle
}

func main() {
  height, _ := strconv.Atoi(os.Args[1])

  layers := triangleLayers(height)
  printable := printLayers(layers)

  for _, str := range printable {
    fmt.Println(str)
  }
}
