use std::collections::HashMap;

fn top_tokens(s: &str) -> Vec<String> {
    let mut res = Vec::new();
    let mut depth = 0;
    let mut cur = String::new();
    for ch in s.chars() {
        if ch == '(' {
            depth += 1;
        } else if ch == ')' {
            depth -= 1;
        }
        if ch == ' ' && depth == 0 {
            if !cur.is_empty() {
                res.push(std::mem::take(&mut cur));
            }
        } else {
            cur.push(ch);
        }
    }
    if !cur.is_empty() {
        res.push(cur);
    }
    res
}

fn ev(expr: &str, scope: &mut HashMap<String, Vec<i64>>) -> i64 {
    let bytes = expr.as_bytes();
    if bytes[0] != b'(' {
        if let Ok(v) = expr.parse::<i64>() {
            return v;
        }
        return *scope[expr].last().unwrap();
    }
    let inner = &expr[1..expr.len() - 1];
    let parts = top_tokens(inner);
    match parts[0].as_str() {
        "add" => ev(&parts[1], scope) + ev(&parts[2], scope),
        "mult" => ev(&parts[1], scope) * ev(&parts[2], scope),
        _ => {
            // let
            let mut assigned: Vec<String> = Vec::new();
            let mut i = 1;
            while i + 1 < parts.len() {
                let val = ev(&parts[i + 1], scope);
                scope.entry(parts[i].clone()).or_default().push(val);
                assigned.push(parts[i].clone());
                i += 2;
            }
            let result = ev(&parts[i], scope);
            for v in assigned {
                scope.get_mut(&v).unwrap().pop();
            }
            result
        }
    }
}

fn evaluate(expression: String) -> i32 {
    let mut scope: HashMap<String, Vec<i64>> = HashMap::new();
    ev(&expression, &mut scope) as i32
}

fn main() {
    println!(
        "{}",
        evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))".into())
    ); // 14
    println!("{}", evaluate("(let x 3 x 2 x)".into())); // 2
    println!("{}", evaluate("(let x 1 y 2 x (add x y) (add x y))".into())); // 5
    println!("{}", evaluate("(add 1 2)".into())); // 3
    println!("{}", evaluate("(let x 7 -12)".into())); // -12
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(
            evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))".into()),
            14
        );
        assert_eq!(evaluate("(let x 3 x 2 x)".into()), 2);
        assert_eq!(evaluate("(let x 1 y 2 x (add x y) (add x y))".into()), 5);
        assert_eq!(evaluate("(add 1 2)".into()), 3);
        assert_eq!(evaluate("(let x 7 -12)".into()), -12);
    }
}
