impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        if strs.len() == 0 {
            return String::from("");
        }
        strs.iter().fold(String::from(""), |acc, word| if acc == "" {format!("-{}", word)} else {format!("{}^*^-{}", acc, word)})
    }

    pub fn decode(s: String) -> Vec<String> {
        if s == "" {
            return Vec::new();
        }
        s.split("^*^").map(|word| String::from(word.strip_prefix("-").unwrap())).collect()
    }
}
