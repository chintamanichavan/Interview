# LeetCode Solutions

My solutions to problems from [LeetCode](https://leetcode.com/). The older corpus is
Python-only; recent problems are solved in five languages.

## Structure

Solutions are organized flat, by language. Each file is named by the problem title
(e.g. `JumpGameIII`) and is self-contained.

| Directory | Language | Layout |
|-----------|----------|--------|
| `Python/` | Python   | One `.py` per problem; `class Solution` + an `if __name__` demo block |
| `Go/`     | Go       | One `.go` per problem, each `//go:build ignore` so they don't collide on `main` |
| `Rust/`   | Rust     | Cargo project; solutions in `src/bin/<snake_case>.rs` with `#[cfg(test)]` tests |
| `CPP/`    | C++      | One `.cpp` per problem; `class Solution` + a `main()` demo |
| `Java/`   | Java     | One `.java` per problem; `public class <Name>` + a `main()` demo |

## Running a solution

```bash
python3 Python/JumpGameIII.py
go run Go/JumpGameIII.go
cargo run --bin jump_game_iii        # from Rust/
g++ -std=c++17 -O2 CPP/JumpGameIII.cpp -o /tmp/sol && /tmp/sol
javac -d /tmp Java/JumpGameIII.java && java -cp /tmp JumpGameIII
```

## Tests

A local, stdlib-only regression pipeline lives under `tests/` (untracked — kept local).
It golden-diffs the stdout of every printing solution, runs `cargo test` for Rust, and
syntax-smokes the rest:

```bash
python3 tests/run_tests.py          # check everything
python3 tests/run_tests.py --bless  # regenerate goldens after intentional changes
```

See `tests/README.md` for details.
