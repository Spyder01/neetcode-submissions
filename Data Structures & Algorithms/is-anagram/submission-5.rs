impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut sChar: Vec<char> = s.chars().collect();
        sChar.sort_unstable();
        let mut tChar: Vec<char> = t.chars().collect();
        tChar.sort_unstable();

        for (i, ch) in sChar.into_iter().enumerate() {
            if ch != tChar[i] {
                return false;
            }
        }

        true
    }
}
