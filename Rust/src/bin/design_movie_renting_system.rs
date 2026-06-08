use std::collections::{BTreeSet, HashMap};

struct MovieRentingSystem {
    // available[movie] = set of (price, shop); rented = set of (price, shop, movie).
    available: HashMap<i32, BTreeSet<(i32, i32)>>,
    rented: BTreeSet<(i32, i32, i32)>,
    price: HashMap<(i32, i32), i32>,
}

impl MovieRentingSystem {
    fn new(_n: i32, entries: Vec<Vec<i32>>) -> Self {
        let mut s = Self {
            available: HashMap::new(),
            rented: BTreeSet::new(),
            price: HashMap::new(),
        };
        for e in &entries {
            let (shop, movie, price) = (e[0], e[1], e[2]);
            s.price.insert((shop, movie), price);
            s.available.entry(movie).or_default().insert((price, shop));
        }
        s
    }

    fn search(&self, movie: i32) -> Vec<i32> {
        match self.available.get(&movie) {
            Some(set) => set.iter().take(5).map(|&(_, shop)| shop).collect(),
            None => Vec::new(),
        }
    }

    fn rent(&mut self, shop: i32, movie: i32) {
        let p = self.price[&(shop, movie)];
        self.available.get_mut(&movie).unwrap().remove(&(p, shop));
        self.rented.insert((p, shop, movie));
    }

    fn drop(&mut self, shop: i32, movie: i32) {
        let p = self.price[&(shop, movie)];
        self.rented.remove(&(p, shop, movie));
        self.available.get_mut(&movie).unwrap().insert((p, shop));
    }

    fn report(&self) -> Vec<Vec<i32>> {
        self.rented.iter().take(5).map(|&(_, shop, movie)| vec![shop, movie]).collect()
    }
}

fn int_list(xs: &[i32]) -> String {
    format!("[{}]", xs.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(", "))
}

fn pair_list(xs: &[Vec<i32>]) -> String {
    format!("[{}]", xs.iter().map(|p| int_list(p)).collect::<Vec<_>>().join(", "))
}

fn main() {
    let mut m = MovieRentingSystem::new(
        3,
        vec![vec![0, 1, 5], vec![0, 2, 6], vec![0, 3, 7], vec![1, 1, 4], vec![1, 2, 7], vec![2, 1, 5]],
    );
    let mut out = vec!["null".to_string()];
    out.push(int_list(&m.search(1)));
    m.rent(0, 1);
    out.push("null".into());
    m.rent(1, 2);
    out.push("null".into());
    out.push(pair_list(&m.report()));
    m.drop(1, 2);
    out.push("null".into());
    out.push(int_list(&m.search(2)));
    println!("[{}]", out.join(", "));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        let mut m = MovieRentingSystem::new(
            3,
            vec![vec![0, 1, 5], vec![0, 2, 6], vec![0, 3, 7], vec![1, 1, 4], vec![1, 2, 7], vec![2, 1, 5]],
        );
        assert_eq!(m.search(1), vec![1, 0, 2]);
        m.rent(0, 1);
        m.rent(1, 2);
        assert_eq!(m.report(), vec![vec![0, 1], vec![1, 2]]);
        m.drop(1, 2);
        assert_eq!(m.search(2), vec![0, 1]);
    }
}
