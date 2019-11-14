# Tech To Protect

## Thoughts
  - Issue is finding the route to each point with distances and weights for hazards
  - Potentially use the maze solving algorithim to solve each maze 
    - A maze would be a starting point of the door to first room, first room to second, etc.
  - The biggest problem is figuring out which room to hit first
  - Possibly calculate the "distance" to each room using the maze algorithim and then use the distances to each room to solve the TSP problem
    - How to measure distance though - need some numerical representation of the difficulty of solving the maze equation
    - Possibly the overall "reward" given to the agent at the end of each maze
      - Subtractions come from moves into open spaces and hazards
      - Agent shouldn't try to move into walls due to large penalty
      - Overall score should represent the difficulty (number of moves and hazards) in order to solve it
    - Possibly solve each room from entrance
    - Once quickest route is found, solve all rooms from next point
      - Example - door, room 1, room 2, room 3
        - door to room 1 is fastest after calculating all 3 options
        - solve door to 1
        - room 1 to room 3 is fastest after calculating room 1 to room 2 and 3
        - solve room 1 to 3
        - solve room 3 to 2
        - solve room 2 to door
    - How to add in stairs?
      - Some large penalty
      - Will take some work to turn into maze
      - Start second maze from entry/exit point of stairs
## 2D Mapping of Point Cloud
  - Take slices of the point cloud file
    - First calculate max and min
    - Iterate in .3-.4 sized slices (maybe smaller if range is smaller?)
    - Generate/save new photo for each slice
    - Use Docker copy/mount to make files accessible to user
