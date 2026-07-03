use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut mp = HashMap::<[u8; 26], Vec<String>>::new();


        for word in strs {
            let mut freqArr = [0; 26];
            for c in word.chars() {
                freqArr[(c as u8 - b'a') as usize] += 1
            }

            mp.entry(freqArr)
                .or_default()
                .push(word);
        }

        let res: Vec<Vec<String>> = mp.into_values().collect();

        res
    }
}
