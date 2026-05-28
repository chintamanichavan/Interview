use std::collections::VecDeque;

const DRAW: i32 = 0;
const MOUSE: i32 = 1;
const CAT: i32 = 2;

fn cat_mouse_game(graph: Vec<Vec<i32>>) -> i32 {
    let n = graph.len();
    let mut color = vec![vec![[DRAW; 3]; n]; n];
    let mut degree = vec![vec![[0i32; 3]; n]; n];
    let has_zero: Vec<bool> = graph.iter().map(|adj| adj.contains(&0)).collect();
    for m in 0..n {
        for c in 0..n {
            degree[m][c][MOUSE as usize] = graph[m].len() as i32;
            degree[m][c][CAT as usize] = graph[c].len() as i32 - if has_zero[c] { 1 } else { 0 };
        }
    }

    let mut queue: VecDeque<(usize, usize, i32, i32)> = VecDeque::new();
    for i in 0..n {
        for &t in &[MOUSE, CAT] {
            color[0][i][t as usize] = MOUSE;
            queue.push_back((0, i, t, MOUSE));
            if i > 0 {
                color[i][i][t as usize] = CAT;
                queue.push_back((i, i, t, CAT));
            }
        }
    }

    while let Some((m, c, turn, result)) = queue.pop_front() {
        if turn == MOUSE {
            for &pc_i in &graph[c] {
                let pc = pc_i as usize;
                if pc_i == 0 || color[m][pc][CAT as usize] != DRAW {
                    continue;
                }
                if result == CAT {
                    color[m][pc][CAT as usize] = CAT;
                    queue.push_back((m, pc, CAT, CAT));
                } else {
                    degree[m][pc][CAT as usize] -= 1;
                    if degree[m][pc][CAT as usize] == 0 {
                        color[m][pc][CAT as usize] = result;
                        queue.push_back((m, pc, CAT, result));
                    }
                }
            }
        } else {
            for &pm_i in &graph[m] {
                let pm = pm_i as usize;
                if color[pm][c][MOUSE as usize] != DRAW {
                    continue;
                }
                if result == MOUSE {
                    color[pm][c][MOUSE as usize] = MOUSE;
                    queue.push_back((pm, c, MOUSE, MOUSE));
                } else {
                    degree[pm][c][MOUSE as usize] -= 1;
                    if degree[pm][c][MOUSE as usize] == 0 {
                        color[pm][c][MOUSE as usize] = result;
                        queue.push_back((pm, c, MOUSE, result));
                    }
                }
            }
        }
    }

    color[1][2][MOUSE as usize]
}

fn main() {
    println!("{}", cat_mouse_game(vec![vec![2, 5], vec![3], vec![0, 4, 5], vec![1, 4, 5], vec![2, 3], vec![0, 2, 3]])); // 0
    println!("{}", cat_mouse_game(vec![vec![1, 3], vec![0], vec![3], vec![0, 2]])); // 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(cat_mouse_game(vec![vec![2, 5], vec![3], vec![0, 4, 5], vec![1, 4, 5], vec![2, 3], vec![0, 2, 3]]), 0);
        assert_eq!(cat_mouse_game(vec![vec![1, 3], vec![0], vec![3], vec![0, 2]]), 1);
    }
}
