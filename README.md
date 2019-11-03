# Tech To Protect Traveling Salesman

## Thoughts
  - Issue is finding the route to each point with distances and weights for hazards
  - Potentially use the maze solving algorithim to solve each maze 
    - A maze would be a starting point of the door to first room, first room to second, etc.
  - The biggest problem is figuring out which room to hit first
  - Possibly calculate the "distance" to each room using the maze algorithim and then use the distances to each room to solve the TSP problem
    - How to measure distance though - need some numerical representation of the difficulty of solving the maze equation
