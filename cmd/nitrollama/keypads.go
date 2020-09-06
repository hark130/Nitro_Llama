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

var solution1 = []int{28, 13, 30, 12,  7,  9, 23}
var solution2 = []int{16, 28, 23, 26,  3,  9, 20}
var solution3 = []int{ 1,  8, 26,  5, 15, 30,  3}
var solution4 = []int{11, 21, 31,  7,  5, 20,  4}
var solution5 = []int{24,  4, 31, 22, 21, 19,  2}
var solution6 = []int{11, 16, 27, 14, 24, 18,  6}

func main() {
    // LOCAL VARIABLES
    var input1 int
    var input2 int
    var input3 int
    var input4 int

    // PRINT MENU
    print_map(symbolMap, true)

    // TAKE USER INPUT
    fmt.Println("Enter the symbols by number:")
    fmt.Scan(&input1)
    fmt.Scan(&input2)
    fmt.Scan(&input3)
    fmt.Scan(&input4)

    // fmt.Printf("%d %d %d %d\n", input1, input2, input3, input4)  // DEBUGGING

    // SOLVE
    solve_keypad(input1, input2, input3, input4)
}

func print_map(symbolMap map[int]string, printNumOrder bool) {
    // Hash order(?)
    // for k, v := range symbolMap {
    //  fmt.Printf("%02d: %s\n", k, v)
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
    // var solution = []int{}   // Store solution here
    var success = true     // Indicates all symbols are present in the map

    // INPUT VALIDATION
    success = validate_input(symbol1, symbol2, symbol3, symbol4)

    // FIND SOLUTION


    fmt.Printf("%t\n", success) // DEBUGGING
}

func validate_input(symbol1 int, symbol2 int, symbol3 int, symbol4 int) bool {
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

    return success
}
