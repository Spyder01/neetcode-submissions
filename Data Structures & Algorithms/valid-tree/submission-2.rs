impl Solution {
    pub fn valid_tree(n: i32, edges: Vec<Vec<i32>>) -> bool {
        let nu = n as usize;
        if edges.len() != nu - 1 {
            return false;
        }

        let mut graph = vec![Vec::<i32>::new(); nu];
        for edge in edges.into_iter() {
            graph[edge[0] as usize].push(edge[1]);
            graph[edge[1] as usize].push(edge[0]);
        }

        let mut count = nu;
        let mut visited = vec![false; nu];

        let mut stack = Vec::with_capacity(nu);
        stack.push((0_usize, usize::MAX));
        visited[0] = true;
        count -= 1;

        while let Some((idx, parent)) = stack.pop() {
            for &i in graph[idx].iter() {
                let u = i as usize;
                if parent == u {
                    continue;
                }

                if visited[u] {
                    return false;
                }

                visited[u] = true;
                stack.push((u, idx));
                count -= 1
            }
        }

        count == 0
    }
}
