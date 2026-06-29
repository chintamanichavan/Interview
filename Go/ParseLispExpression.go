//go:build ignore

package main

import (
	"fmt"
	"strconv"
)

type Evaluator struct {
	scope map[string][]int
}

// split a (...) body into top-level tokens, respecting nested parens
func topTokens(s string) []string {
	res := []string{}
	depth := 0
	cur := []byte{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch == '(' {
			depth++
		} else if ch == ')' {
			depth--
		}
		if ch == ' ' && depth == 0 {
			if len(cur) > 0 {
				res = append(res, string(cur))
				cur = cur[:0]
			}
		} else {
			cur = append(cur, ch)
		}
	}
	if len(cur) > 0 {
		res = append(res, string(cur))
	}
	return res
}

func isIntLiteral(s string) bool {
	if s == "" {
		return false
	}
	if v, err := strconv.Atoi(s); err == nil {
		_ = v
		return true
	}
	return false
}

func (e *Evaluator) ev(expr string) int {
	if expr[0] != '(' {
		if isIntLiteral(expr) {
			v, _ := strconv.Atoi(expr)
			return v
		}
		st := e.scope[expr]
		return st[len(st)-1]
	}
	parts := topTokens(expr[1 : len(expr)-1])
	switch parts[0] {
	case "add":
		return e.ev(parts[1]) + e.ev(parts[2])
	case "mult":
		return e.ev(parts[1]) * e.ev(parts[2])
	}
	// let
	assigned := []string{}
	i := 1
	for i+1 < len(parts) {
		v := e.ev(parts[i+1])
		e.scope[parts[i]] = append(e.scope[parts[i]], v)
		assigned = append(assigned, parts[i])
		i += 2
	}
	result := e.ev(parts[i])
	for _, v := range assigned {
		e.scope[v] = e.scope[v][:len(e.scope[v])-1]
	}
	return result
}

func evaluate(expression string) int {
	e := &Evaluator{scope: map[string][]int{}}
	return e.ev(expression)
}

func main() {
	fmt.Println(evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))")) // 14
	fmt.Println(evaluate("(let x 3 x 2 x)"))                            // 2
	fmt.Println(evaluate("(let x 1 y 2 x (add x y) (add x y))"))        // 5
	fmt.Println(evaluate("(add 1 2)"))                                  // 3
	fmt.Println(evaluate("(let x 7 -12)"))                              // -12
}
