use std::collections::HashSet;

fn is_rectangle_cover(rectangles: Vec<Vec<i32>>) -> bool {
    let mut area: i64 = 0;
    let (mut minx, mut miny) = (i32::MAX, i32::MAX);
    let (mut maxx, mut maxy) = (i32::MIN, i32::MIN);
    let mut corners: HashSet<(i32, i32)> = HashSet::new();

    for r in &rectangles {
        let (x1, y1, x2, y2) = (r[0], r[1], r[2], r[3]);
        area += (x2 - x1) as i64 * (y2 - y1) as i64;
        minx = minx.min(x1);
        miny = miny.min(y1);
        maxx = maxx.max(x2);
        maxy = maxy.max(y2);
        for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)] {
            if !corners.insert(p) {
                corners.remove(&p);
            }
        }
    }

    let expected: HashSet<(i32, i32)> = [(minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)]
        .into_iter()
        .collect();
    if corners != expected {
        return false;
    }
    area == (maxx - minx) as i64 * (maxy - miny) as i64
}

fn main() {
    println!(
        "{}",
        is_rectangle_cover(vec![
            vec![1, 1, 3, 3],
            vec![3, 1, 4, 2],
            vec![3, 2, 4, 4],
            vec![1, 3, 2, 4],
            vec![2, 3, 3, 4]
        ])
    ); // true
    println!(
        "{}",
        is_rectangle_cover(vec![
            vec![1, 1, 2, 3],
            vec![1, 3, 2, 4],
            vec![3, 1, 4, 2],
            vec![3, 2, 4, 4]
        ])
    ); // false
    println!(
        "{}",
        is_rectangle_cover(vec![
            vec![1, 1, 3, 3],
            vec![3, 1, 4, 2],
            vec![1, 3, 2, 4],
            vec![2, 2, 4, 4]
        ])
    ); // false
    println!("{}", is_rectangle_cover(vec![vec![0, 0, 1, 1]])); // true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert!(is_rectangle_cover(vec![
            vec![1, 1, 3, 3],
            vec![3, 1, 4, 2],
            vec![3, 2, 4, 4],
            vec![1, 3, 2, 4],
            vec![2, 3, 3, 4]
        ]));
        assert!(!is_rectangle_cover(vec![
            vec![1, 1, 2, 3],
            vec![1, 3, 2, 4],
            vec![3, 1, 4, 2],
            vec![3, 2, 4, 4]
        ]));
        assert!(!is_rectangle_cover(vec![
            vec![1, 1, 3, 3],
            vec![3, 1, 4, 2],
            vec![1, 3, 2, 4],
            vec![2, 2, 4, 4]
        ]));
        assert!(is_rectangle_cover(vec![vec![0, 0, 1, 1]]));
    }
}
