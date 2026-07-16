impl Solution {
    pub fn count_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let nu = n as usize;
        let mut visited = vec![false; nu];
        let mut graph = vec![Vec::with_capacity(nu); nu];

        for edge in edges.into_iter() {
            graph[edge[0] as usize].push(edge[1]);
            graph[edge[1] as usize].push(edge[0]);
        }

        let mut stack = Vec::with_capacity(nu);

        let mut count = 0_i32;
        for i in 0..nu {
            if visited[i] {
                continue;
            }

            stack.push(i);
            visited[i] = true;
            count += 1;
            while let Some(idx) = stack.pop() {
                for &node in graph[idx].iter() {
                    if visited[node as usize] {
                        continue;
                    }

                    stack.push(node as usize);
                    visited[node as usize] = true; 
                }
            }
        }

        count

    }
}
