# Insert Pseudocode

"""
Insert 50
50 < 100, left child node doesn't exist, create a left child node with value 50 and depth 2

    ==> 100
       /
      50

Insert 125
125 > 100, right child node doesn't exist, create a right child node with value 125 and depth 2

    ==> 100
       /   \
      50    125

Insert 75
75 < 100, left child node with value 50 exists, recursively insert at left child

    ==> 100
       /   \
      50    125

75 > 50, right child node doesn't exist, create a right child node with value 75 and depth 3

        100
       /   \
  ==> 50    125
       \
       75

Insert 25
25 < 100, left child node with value 50 exists, recursively insert at left child

    ==> 100
       /   \
      50    125
        \
        75

25 < 50, left child node doesn't exist, create a left child node with value 25 and depth 3

        100
       /   \
  ==> 50    125
     /  \
    25  75

"""