use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct DinnerPlates {
    cap: usize,
    stacks: Vec<Vec<i32>>,
    avail: BinaryHeap<Reverse<usize>>, // min-heap of indices with room (may hold stale entries)
}

impl DinnerPlates {
    fn new(capacity: i32) -> Self {
        Self { cap: capacity as usize, stacks: Vec::new(), avail: BinaryHeap::new() }
    }

    fn push(&mut self, val: i32) {
        while let Some(&Reverse(i)) = self.avail.peek() {
            if i >= self.stacks.len() || self.stacks[i].len() >= self.cap {
                self.avail.pop();
            } else {
                break;
            }
        }
        if self.avail.is_empty() {
            self.avail.push(Reverse(self.stacks.len()));
            self.stacks.push(Vec::new());
        }
        let i = self.avail.peek().unwrap().0;
        self.stacks[i].push(val);
        if self.stacks[i].len() >= self.cap {
            self.avail.pop();
        }
    }

    fn pop(&mut self) -> i32 {
        while let Some(last) = self.stacks.last() {
            if last.is_empty() {
                self.stacks.pop();
            } else {
                break;
            }
        }
        if self.stacks.is_empty() {
            return -1;
        }
        let idx = self.stacks.len() - 1;
        self.pop_at_stack(idx as i32)
    }

    fn pop_at_stack(&mut self, index: i32) -> i32 {
        let index = index as usize;
        if index >= self.stacks.len() || self.stacks[index].is_empty() {
            return -1;
        }
        self.avail.push(Reverse(index));
        self.stacks[index].pop().unwrap()
    }
}

fn main() {
    let ops = [
        "DinnerPlates", "push", "push", "push", "push", "push", "popAtStack",
        "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop",
    ];
    let args: [i32; 16] = [2, 1, 2, 3, 4, 5, 0, 20, 21, 0, 2, 0, 0, 0, 0, 0];
    let mut d = DinnerPlates::new(0);
    let mut out: Vec<String> = Vec::new();
    for (op, &a) in ops.iter().zip(args.iter()) {
        match *op {
            "DinnerPlates" => { d = DinnerPlates::new(a); out.push("null".into()); }
            "push" => { d.push(a); out.push("null".into()); }
            "pop" => out.push(d.pop().to_string()),
            "popAtStack" => out.push(d.pop_at_stack(a).to_string()),
            _ => {}
        }
    }
    println!("[{}]", out.join(", "));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        let mut d = DinnerPlates::new(2);
        for v in [1, 2, 3, 4, 5] {
            d.push(v);
        }
        assert_eq!(d.pop_at_stack(0), 2);
        d.push(20);
        d.push(21);
        assert_eq!(d.pop_at_stack(0), 20);
        assert_eq!(d.pop_at_stack(2), 21);
        assert_eq!(d.pop(), 5);
        assert_eq!(d.pop(), 4);
        assert_eq!(d.pop(), 3);
        assert_eq!(d.pop(), 1);
        assert_eq!(d.pop(), -1);
    }
}
