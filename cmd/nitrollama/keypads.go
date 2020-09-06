// go build keypads.go
// ./keypads

package main

import (
	"fmt"
)

var symbolMap = map[int]string{
	1:  "Copyright",
	2:  "Filled Star",
	3:  "Hollow Star",
	4:  "Smiley Face",
	5:  "Double K",
	6:  "Omega",
	7:  "Squid Knife",
	8:  "Pumpkin",
	9:  "Hook N",
	10: "Teepee",
	11: "Six",
	12: "Squiggly N",
	13: "AT",
	14: "ae",
	15: "Melted Three",
	16: "Euro",
	17: "Circle",
	18: "N With Hat",
	19: "Dragon",
	20: "Question Mark",
	21: "Paragraph",
	22: "Right C",
	23: "Left C",
	24: "Pitchfork",
	25: "Tripod",
	26: "Cursive",
	27: "Tracks",
	28: "Balloon",
	29: "Weird Nose",
	30: "Upside Down Y",
	31: "bt",
}

func main() {
	// PRINT MENU
	print_map(symbolMap, true)

	// TAKE USER INPUT
	// one
	// two
	// three
	// four

	// SOLVE
	solve_keypad(1, 2, 3, 4)
}

func print_map(symbolMap map[int]string, printNumOrder bool) {
	// Hash order(?)
	// for k, v := range symbolMap {
	// 	fmt.Printf("%02d: %s\n", k, v)
	// }
	if printNumOrder {
		// Key order
		for i := 1; i < 32; i++ {
			fmt.Printf("%02d: %s\n", i, symbolMap[i])
		}
	} else {
		fmt.Println("UNSUPPORTED!")
	}
}

func solve_keypad(symbol1 int, symbol2 int, symbol3 int, symbol4 int) {
	// LOCAL VARIABLES
	var symMap = symbolMap // Local copy of the global symbol mapping
	var success = true     // Indicates all symbols are present in the map

	// INPUT VALIDATION
	// symbol1
	if _, present := symMap[symbol1]; !present {
		success = false
	}
	// symbol2
	if _, present := symMap[symbol2]; !present {
		success = false
	}
	// symbol3
	if _, present := symMap[symbol3]; !present {
		success = false
	}
	// symbol4
	if _, present := symMap[symbol4]; !present {
		success = false
	}

	fmt.Printf("%t\n", success) // DEBUGGING
}
