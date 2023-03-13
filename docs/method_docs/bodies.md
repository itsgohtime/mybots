### Creation of Bodies
- A random link excluding the first one is chosen and the direction it attaches to the previous link is changed
- Following links's direction are also changed to ensure that there is no overlap and if there is any links that would collide with a previous link then the dimensions are changed
![alt text](https://github.com/itsgohtime/mybots/blob/Asn-8/mutated_body.jpg)

### Mutation of Bodies
- Based on the number of links, a direction for each joint is randomly chosen
- The first direction connects the second link to the first link and then links are added like a binary tree
    - third and fourth link join to second link
    - fifth and sixth link join to third link
    - seventh and eight link join to fourth link
- The sizes of the links are checked to ensure they don't collide with previous links
    - If there is a collision, the dimensions are chosen again and this continues until there isn't a collision
![alt text](https://github.com/itsgohtime/mybots/blob/final-project/docs/body_diagram.jpg)
s