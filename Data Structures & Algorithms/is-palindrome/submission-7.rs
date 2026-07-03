impl Solution {
    pub fn is_palindrome(s: String) -> bool {
    let chars: Vec<char> = s.chars()
    .filter(|x| x.is_alphanumeric())
    .map(|x| x.to_ascii_lowercase())
    .collect();

    let mut left = 0;
    let mut right = chars.len().saturating_sub(1);

    while left < right {
        if chars[left] != chars[right] {
            return false;
        }

        left += 1;
        right -= 1;
    }

    true
}
}
