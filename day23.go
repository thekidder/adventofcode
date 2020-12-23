package main

import "fmt"

func rotate(l []int, n int) []int {
  return append(l[n:], l[:n]...)
}

func contains(s []int, e int) bool {
	for _, a := range s {
    if a == e {
      return true
    }
  }
  return false
}

func index(s []int, e int) int {
  for p, v := range s {
    if (v == e) {
      return p
    }
  }
  return -1
}


func run(cups []int) {
	minCup := 1
	maxCup := len(cups)
	fmt.Println("run")
	pos := 0
	for i := 0; i < 10000000; i++ {
    cur := cups[pos]
    // # picked_up = [cups.pop(1) for i in range(3)]
    pickedUp := []int{}
    for j := 0; j < 3; j++ {
    	pickedUp = append(pickedUp, cups[(pos + j + 1)%len(cups)])
    }
    dest := cur - 1
    for ; contains(pickedUp, dest) || dest < minCup; {
    	dest -= 1
    	if dest < minCup {
	    	dest = maxCup
    	}
    }
    destIdx := index(cups, dest)
    pickupIdx := (pos + 1) % len(cups)
    pickupEndIdx := (pos + 4) % len(cups)
    newCups := []int{}
    if pickupEndIdx < pickupIdx || pickupIdx == 0 {
      newCups = append(newCups, cups[pickupEndIdx:destIdx+1]...)
      newCups = append(newCups, pickedUp...)
      newCups = append(newCups, cups[destIdx+1:pos+1]...)
    } else if destIdx > pos {
      newCups = append(newCups, cups[:pos+1]...)
      newCups = append(newCups, cups[pos+4:destIdx+1]...)
      newCups = append(newCups, pickedUp...)
      newCups = append(newCups, cups[destIdx+1:]...)
    } else {
      newCups = append(newCups, cups[:destIdx+1]...)
      newCups = append(newCups, pickedUp...)
      newCups = append(newCups, cups[destIdx+1:pos+1]...)
      newCups = append(newCups, cups[pos+4:]...)
    }
    cups = newCups
    pos = (index(cups, cur) + 1) % len(cups)

    if (i+1) % 10000 == 0 {
      fmt.Printf("iteration %d\n", i+1)
    }

  }
  // fmt.Println("Final cups:")
  // for i := 0; i < len(cups); i++ {
  // 	fmt.Printf("%d, ", cups[i])
  // }
  fmt.Println("\n\nAfter 1:")
  fmt.Println(cups[(index(cups, 1) + 1) % len(cups)])
  fmt.Println(cups[(index(cups, 1) + 2) % len(cups)])
}

func main() {
	// input := []int{3,8,9,1,2,5,4,6,7}
	input := []int{6,4,3,7,1,9,2,5,8}

	for i := len(input)+1; i <= 1000000; i++ {
		input = append(input, i)
	}

  run(input)
}
