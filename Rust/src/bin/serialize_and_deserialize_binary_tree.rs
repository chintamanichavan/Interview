use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

type Link = Option<Rc<RefCell<TreeNode>>>;

struct TreeNode {
    val: i32,
    left: Link,
    right: Link,
}

impl TreeNode {
    fn new(val: i32) -> Rc<RefCell<TreeNode>> {
        Rc::new(RefCell::new(TreeNode {
            val,
            left: None,
            right: None,
        }))
    }
}

// Level-order encoding: node value, or '#' for a missing child.
fn serialize(root: Link) -> String {
    if root.is_none() {
        return String::new();
    }
    let mut out: Vec<String> = Vec::new();
    let mut q: VecDeque<Link> = VecDeque::new();
    q.push_back(root);
    while let Some(node) = q.pop_front() {
        match node {
            Some(n) => {
                out.push(n.borrow().val.to_string());
                q.push_back(n.borrow().left.clone());
                q.push_back(n.borrow().right.clone());
            }
            None => out.push("#".to_string()),
        }
    }
    out.join(",")
}

fn deserialize(data: String) -> Link {
    if data.is_empty() {
        return None;
    }
    let tokens: Vec<&str> = data.split(',').collect();
    let root = TreeNode::new(tokens[0].parse().unwrap());
    let mut q: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
    q.push_back(root.clone());
    let mut i = 1;
    while let Some(node) = q.pop_front() {
        if tokens[i] != "#" {
            let child = TreeNode::new(tokens[i].parse().unwrap());
            node.borrow_mut().left = Some(child.clone());
            q.push_back(child);
        }
        i += 1;
        if tokens[i] != "#" {
            let child = TreeNode::new(tokens[i].parse().unwrap());
            node.borrow_mut().right = Some(child.clone());
            q.push_back(child);
        }
        i += 1;
    }
    Some(root)
}

fn to_list(root: Link) -> Vec<Option<i32>> {
    let mut out: Vec<Option<i32>> = Vec::new();
    let mut q: VecDeque<Link> = VecDeque::new();
    q.push_back(root);
    while let Some(node) = q.pop_front() {
        match node {
            Some(n) => {
                out.push(Some(n.borrow().val));
                q.push_back(n.borrow().left.clone());
                q.push_back(n.borrow().right.clone());
            }
            None => out.push(None),
        }
    }
    while out.last() == Some(&None) {
        out.pop();
    }
    out
}

fn main() {
    let root = TreeNode::new(1);
    root.borrow_mut().left = Some(TreeNode::new(2));
    let r = TreeNode::new(3);
    r.borrow_mut().left = Some(TreeNode::new(4));
    r.borrow_mut().right = Some(TreeNode::new(5));
    root.borrow_mut().right = Some(r);

    let data = serialize(Some(root));
    println!("{}", data);
    println!("{:?}", to_list(deserialize(data))); // [Some(1), Some(2), Some(3), None, None, Some(4), Some(5)]
    println!("{:?}", serialize(deserialize(serialize(None)))); // ""
    println!(
        "{:?}",
        to_list(deserialize(serialize(Some(TreeNode::new(7)))))
    ); // [Some(7)]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn roundtrip() {
        let root = TreeNode::new(1);
        root.borrow_mut().left = Some(TreeNode::new(2));
        let r = TreeNode::new(3);
        r.borrow_mut().left = Some(TreeNode::new(4));
        r.borrow_mut().right = Some(TreeNode::new(5));
        root.borrow_mut().right = Some(r);
        let data = serialize(Some(root));
        assert_eq!(
            to_list(deserialize(data)),
            vec![Some(1), Some(2), Some(3), None, None, Some(4), Some(5)]
        );
        assert_eq!(serialize(deserialize(serialize(None))), "");
    }
}
