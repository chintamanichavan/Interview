//go:build ignore

package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

// entry sorts by (price, shop) for available, and (price, shop, movie) for rented.
type entry struct{ price, shop, movie int }

func lessAvail(a, b entry) bool {
	if a.price != b.price {
		return a.price < b.price
	}
	return a.shop < b.shop
}

func lessRented(a, b entry) bool {
	if a.price != b.price {
		return a.price < b.price
	}
	if a.shop != b.shop {
		return a.shop < b.shop
	}
	return a.movie < b.movie
}

// insertSorted / removeSorted keep a slice ordered via binary search.
func insertSorted(s []entry, e entry, less func(a, b entry) bool) []entry {
	i := sort.Search(len(s), func(i int) bool { return !less(s[i], e) })
	s = append(s, entry{})
	copy(s[i+1:], s[i:])
	s[i] = e
	return s
}

func removeSorted(s []entry, e entry, less func(a, b entry) bool) []entry {
	i := sort.Search(len(s), func(i int) bool { return !less(s[i], e) })
	return append(s[:i], s[i+1:]...)
}

type MovieRentingSystem struct {
	available map[int][]entry
	rented    []entry
	price     map[[2]int]int
}

func Constructor(n int, entries [][]int) MovieRentingSystem {
	m := MovieRentingSystem{available: map[int][]entry{}, price: map[[2]int]int{}}
	for _, e := range entries {
		shop, movie, price := e[0], e[1], e[2]
		m.price[[2]int{shop, movie}] = price
		m.available[movie] = insertSorted(m.available[movie], entry{price, shop, movie}, lessAvail)
	}
	return m
}

func (m *MovieRentingSystem) Search(movie int) []int {
	s := m.available[movie]
	res := []int{}
	for i := 0; i < len(s) && i < 5; i++ {
		res = append(res, s[i].shop)
	}
	return res
}

func (m *MovieRentingSystem) Rent(shop, movie int) {
	p := m.price[[2]int{shop, movie}]
	e := entry{p, shop, movie}
	m.available[movie] = removeSorted(m.available[movie], e, lessAvail)
	m.rented = insertSorted(m.rented, e, lessRented)
}

func (m *MovieRentingSystem) Drop(shop, movie int) {
	p := m.price[[2]int{shop, movie}]
	e := entry{p, shop, movie}
	m.rented = removeSorted(m.rented, e, lessRented)
	m.available[movie] = insertSorted(m.available[movie], e, lessAvail)
}

func (m *MovieRentingSystem) Report() [][]int {
	res := [][]int{}
	for i := 0; i < len(m.rented) && i < 5; i++ {
		res = append(res, []int{m.rented[i].shop, m.rented[i].movie})
	}
	return res
}

func intList(xs []int) string {
	parts := make([]string, len(xs))
	for i, x := range xs {
		parts[i] = strconv.Itoa(x)
	}
	return "[" + strings.Join(parts, ", ") + "]"
}

func pairList(xs [][]int) string {
	parts := make([]string, len(xs))
	for i, p := range xs {
		parts[i] = intList(p)
	}
	return "[" + strings.Join(parts, ", ") + "]"
}

func main() {
	m := Constructor(3, [][]int{{0, 1, 5}, {0, 2, 6}, {0, 3, 7}, {1, 1, 4}, {1, 2, 7}, {2, 1, 5}})
	out := []string{"null"}
	out = append(out, intList(m.Search(1)))
	m.Rent(0, 1)
	out = append(out, "null")
	m.Rent(1, 2)
	out = append(out, "null")
	out = append(out, pairList(m.Report()))
	m.Drop(1, 2)
	out = append(out, "null")
	out = append(out, intList(m.Search(2)))
	fmt.Println("[" + strings.Join(out, ", ") + "]")
}
