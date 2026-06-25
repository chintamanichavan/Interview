use std::collections::{HashSet, VecDeque};

fn racecar(target: i32) -> i32 {
    let bound = 2 * target;
    let mut seen: HashSet<(i32, i32)> = HashSet::new();
    seen.insert((0, 1));
    let mut queue: VecDeque<(i32, i32, i32)> = VecDeque::new();
    queue.push_back((0, 1, 0));
    while let Some((pos, speed, steps)) = queue.pop_front() {
        if pos == target {
            return steps;
        }
        // 'A'
        let (npos, nspeed) = (pos + speed, speed * 2);
        if npos >= -bound && npos <= bound && seen.insert((npos, nspeed)) {
            queue.push_back((npos, nspeed, steps + 1));
        }
        // 'R'
        let rspeed = if speed > 0 { -1 } else { 1 };
        if seen.insert((pos, rspeed)) {
            queue.push_back((pos, rspeed, steps + 1));
        }
    }
    -1
}

fn main() {
    println!("{}", racecar(3)); // 2
    println!("{}", racecar(6)); // 5
    println!("{}", racecar(1)); // 1
    println!("{}", racecar(4)); // 5
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(racecar(3), 2);
        assert_eq!(racecar(6), 5);
        assert_eq!(racecar(1), 1);
        assert_eq!(racecar(4), 5);
    }
}
