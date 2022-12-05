package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func stringtoint(strVar string) int {
	intVar, err := strconv.Atoi(strVar)

	if err != nil {
		fmt.Println(err)
		return 0
	}
	return intVar
}

func main() {

	score := 0
	file, err := os.Open("input4.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		elves := strings.Split(scanner.Text(), ",")
		//fmt.Println(elves, "\n")
		left := strings.Split(elves[0], "-")
		l1 := stringtoint(left[0])
		l2 := stringtoint(left[1])
		right := strings.Split(elves[1], "-")
		r1 := stringtoint(right[0])
		r2 := stringtoint(right[1])

		if (l1 > r1 && l2 > r2 && l1 > r2 && l2 > r1) || (l1 < r1 && l2 < r2 && l1 < r2 && l2 < r1) {
			score++
			fmt.Println(elves)
			fmt.Println("Score: ", score)
		}
	}

	fmt.Println(1000 - score)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
