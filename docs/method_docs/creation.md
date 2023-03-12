### Bodies
- How bodies are formed
    - Based on the number of links, a direction for each joint is randomly chosen
    - The first direction connects the second link to the first link and then links are added like a binary tree
        - third and fourth link join to second link
        - fifth and sixth link join to third link
        - seventh and eight link join to fourth link
    - The sizes of the links are checked to ensure they don't collid with previous links
        - If there is a collision, the dimensions are chosen again and this continues until there isn't a collision
![alt text](https://github.com/itsgohtime/mybots/blob/Asn-8/body_diagram.jpg)

### Brains
- How brains are formed
    - The number of links that are sensors are stored and each is made to be a sensor neuron
    - There are 4 hidden neurons but it can be changed in constants.py
    - Each joint (number of links - 1) is made to be a motor neuron
    - Each sensor neuron is connected to every hidden neuron and every hidden neuron is connected to every motor neuron
    ![alt text](https://github.com/itsgohtime/mybots/blob/Asn-8/brain_diagram.jpg)
