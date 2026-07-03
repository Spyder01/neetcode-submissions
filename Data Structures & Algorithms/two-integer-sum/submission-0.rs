use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut mp = HashMap::<i32, i32>::new();

        for (i, x) in nums.into_iter().enumerate() {
            if let Some(&idx) = mp.get(&x) {
                return vec![idx, i as i32];
            } 

            mp.insert(target - x, i as i32);
        }

        Vec::<i32>::new()
    }
}
