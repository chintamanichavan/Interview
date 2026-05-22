#[derive(PartialEq, Eq, Debug)]
struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
}

impl ListNode {
    fn new(val: i32) -> Self {
        Self { val, next: None }
    }
}

fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut first = head?;
    let mut second = match first.next.take() {
        Some(s) => s,
        None => return Some(first),
    };
    first.next = swap_pairs(second.next.take());
    second.next = Some(first);
    Some(second)
}

fn build(vals: &[i32]) -> Option<Box<ListNode>> {
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {
        let mut node = Box::new(ListNode::new(v));
        node.next = head;
        head = Some(node);
    }
    head
}

fn to_vec(mut head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut out = Vec::new();
    while let Some(node) = head {
        out.push(node.val);
        head = node.next;
    }
    out
}

fn main() {
    println!("{:?}", to_vec(swap_pairs(build(&[1, 2, 3, 4])))); // [2, 1, 4, 3]
    println!("{:?}", to_vec(swap_pairs(build(&[]))));           // []
    println!("{:?}", to_vec(swap_pairs(build(&[1]))));          // [1]
    println!("{:?}", to_vec(swap_pairs(build(&[1, 2, 3]))));    // [2, 1, 3]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(to_vec(swap_pairs(build(&[1, 2, 3, 4]))), vec![2, 1, 4, 3]);
        assert_eq!(to_vec(swap_pairs(build(&[]))), Vec::<i32>::new());
        assert_eq!(to_vec(swap_pairs(build(&[1]))), vec![1]);
        assert_eq!(to_vec(swap_pairs(build(&[1, 2, 3]))), vec![2, 1, 3]);
    }
}
