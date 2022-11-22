# Pseudocode Retrieval

"""
At the root node, 75 < 100 so we recursively search on the left child if it exists

    ==> 100
       /   \
      50    125
     /  \
    25  75

At node 50, 75 > 50 and there is a right child so we recursively search on the right child

        100
       /   \
  ==> 50    125
     /  \
    25  75

At the node 75, the value matches 75 so return this node

        100
       /   \
      50    125
     /  \
    25  75 <==

"""