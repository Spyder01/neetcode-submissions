use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, mut k: i32) -> Vec<i32> {
        let mut counter = HashMap::<i32, usize>::new();

        for num in nums {
            *counter
            .entry(num)
            .or_default() += 1
        }

        let mut heap: BinaryHeap<(usize, i32)> = counter
                                            .iter()
                                            .map(|(&num, &count)| (count, num))
                                            .collect();
        
        let mut res = Vec::<i32>::new();
        while k > 0 {
            if let Some((_, num)) = heap.pop() {
                res.push(num);
                k -= 1;
            }
        }

        res
    }
}
