use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut mp = HashMap::<String, Vec<String>>::new();

        for word in strs {
            let mut chVec: Vec<char> = word.chars().collect();
            chVec.sort_unstable();

            let sortedWord: String = chVec.into_iter().collect();

            mp.entry(sortedWord)
                .or_default()
                .push(word);
        }

        let res: Vec<Vec<String>> = mp.into_values().collect();

        res
    }
}
