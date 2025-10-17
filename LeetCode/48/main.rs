impl Solution {
    pub fn rotate(mat: &mut Vec<Vec<i32>>) {
        let n = mat.len();

        for i in 0..n {
            for j in i+1..n {
                let temp = mat[i][j];
                mat[i][j] = mat[j][i];
                mat[j][i] = temp;
            }
        }

        for row in mat.iter_mut() {
            row.reverse();
        }
        
    }
}