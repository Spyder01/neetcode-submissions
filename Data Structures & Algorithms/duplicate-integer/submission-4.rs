use std::collections::HashSet;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut numSet = HashSet::<i32>::new();

        for num in nums {
            if numSet.contains(&num) {
                return true;
            }

            numSet.insert(num);
        }

        false

    }
}
