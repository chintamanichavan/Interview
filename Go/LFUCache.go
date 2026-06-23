//go:build ignore

package main

import (
	"container/list"
	"fmt"
	"strconv"
	"strings"
)

type LFUCache struct {
	cap      int
	keyVal   map[int]int
	keyFreq  map[int]int
	freqList map[int]*list.List    // freq -> keys (front = oldest)
	keyNode  map[int]*list.Element // key -> its element in freqList[freq]
	minFreq  int
}

func Constructor(capacity int) LFUCache {
	return LFUCache{
		cap:      capacity,
		keyVal:   map[int]int{},
		keyFreq:  map[int]int{},
		freqList: map[int]*list.List{},
		keyNode:  map[int]*list.Element{},
	}
}

func (c *LFUCache) bump(key int) {
	f := c.keyFreq[key]
	c.freqList[f].Remove(c.keyNode[key])
	if c.freqList[f].Len() == 0 {
		delete(c.freqList, f)
		if c.minFreq == f {
			c.minFreq++
		}
	}
	c.keyFreq[key] = f + 1
	if c.freqList[f+1] == nil {
		c.freqList[f+1] = list.New()
	}
	c.keyNode[key] = c.freqList[f+1].PushBack(key)
}

func (c *LFUCache) Get(key int) int {
	v, ok := c.keyVal[key]
	if !ok {
		return -1
	}
	c.bump(key)
	return v
}

func (c *LFUCache) Put(key, value int) {
	if c.cap <= 0 {
		return
	}
	if _, ok := c.keyVal[key]; ok {
		c.keyVal[key] = value
		c.bump(key)
		return
	}
	if len(c.keyVal) >= c.cap {
		oldest := c.freqList[c.minFreq].Front()
		ek := oldest.Value.(int)
		c.freqList[c.minFreq].Remove(oldest)
		delete(c.keyVal, ek)
		delete(c.keyFreq, ek)
		delete(c.keyNode, ek)
	}
	c.keyVal[key] = value
	c.keyFreq[key] = 1
	if c.freqList[1] == nil {
		c.freqList[1] = list.New()
	}
	c.keyNode[key] = c.freqList[1].PushBack(key)
	c.minFreq = 1
}

func main() {
	ops := []string{"LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"}
	args := [][]int{{2}, {1, 1}, {2, 2}, {1}, {3, 3}, {2}, {3}, {4, 4}, {1}, {3}, {4}}
	var c LFUCache
	out := []string{}
	for i, op := range ops {
		switch op {
		case "LFUCache":
			c = Constructor(args[i][0])
			out = append(out, "null")
		case "get":
			out = append(out, strconv.Itoa(c.Get(args[i][0])))
		case "put":
			c.Put(args[i][0], args[i][1])
			out = append(out, "null")
		}
	}
	fmt.Println("[" + strings.Join(out, ", ") + "]")
}
