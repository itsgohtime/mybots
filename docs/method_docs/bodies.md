### Creation of Bodies
- Based on the number of links, a direction for each joint is randomly chosen
- The first direction connects the second link to the first link and then links are added like a binary tree
    - third and fourth link join to second link
    - fifth and sixth link join to third link
    - seventh and eight link join to fourth link
- The sizes of the links are checked to ensure they don't collide with previous links
    - If there is a collision, the dimensions are chosen again and this continues until there isn't a collision
- Directions are set between 0 and 6 where 0 = +x, 1 = -x, 2 = +y, 3 = -y, 4 = +z, 5 = -z
    - The directions for the body diagram below is [4, 0, 2, 3, 5, 1, 0]

<div align=center>
    
<img width="638" alt="body" src="https://user-images.githubusercontent.com/61445107/224882730-eedca7f6-4ab4-4c88-901d-d24be2bc5199.png">
    
</div>


### Mutation of Bodies
- A random link excluding the first one is chosen and the direction it attaches to the previous link is changed
    - For the first diagram below, the direction that link 5 attaches to link 2 changes from 5 to 4, so the subsequent joints of 3_6 and 3_7 change as well
        - The resulting directions for the body diagram is   [4, 0, 2, 3, 4, 5, 1]
- Following links's direction are also changed to ensure that there is no overlap and if there is any links that would collide with a previous link then the dimensions are changed


<div align=center>
    
<img width="369" alt="body mutation" src="https://user-images.githubusercontent.com/61445107/224882737-7fd6f3b3-41d2-48e0-92de-32c16bf3ea38.png">
<img width="810" alt="image" src="https://user-images.githubusercontent.com/61445107/224773841-ca274292-445b-4958-a5b2-a98e55cc56c8.png">
  
</div>
