package main

import (
	"fmt"
	"log"
)

func main() {
	body, err := iotuil.ReadFile("file.txt")
	if err != nil {
		log.Fatalf("unable to read file: %v", err)
	}
	fmt.Println(string(body))
}
