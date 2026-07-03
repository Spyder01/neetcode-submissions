impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let cleaned: String = s.chars()
            .filter(|c| c.is_alphanumeric())
            .map(|c| c.to_ascii_lowercase())
            .collect();

        cleaned.chars().eq(cleaned.chars().rev())
    }
}