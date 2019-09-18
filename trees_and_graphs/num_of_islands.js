let {PI, sin, cos, round} = Math;

function traverseGrid(grid, cell) {
  let [row, col] = cell;
  grid[row][col] = "0";  
    
  for (var rad = 0; rad < 2*PI; rad += PI/2) {
    next_row = row + round(cos(rad));
    next_col = col + round(sin(rad));
    
    if (next_row < 0 || next_row>= grid.length) {
      continue;
    }
    if (next_col < 0 || next_col >= grid[0].length) {
      continue;
    }
    if (grid[next_row][next_col] == "1") {
      traverseGrid(grid, [next_row, next_col]);
    }
  }
}
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
  let num = 0;
  for (var row = 0; row < grid.length; row++) {
    for (var col = 0; col < grid[0].length; col++) {
      if (grid[row][col] == "1") {
         traverseGrid(grid, [row, col]);
         num++;
      }
    }
  }
  return num;
};