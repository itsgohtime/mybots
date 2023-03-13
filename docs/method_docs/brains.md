### Creation of Brains
- The number of links that are sensors are stored and each is made to be a sensor neuron
- There are 4 hidden neurons but it can be changed in constants.py
- Each joint (number of links - 1) is made to be a motor neuron
- Each sensor neuron is connected to every hidden neuron and every hidden neuron is connected to every motor neuron
![alt text](https://github.com/itsgohtime/mybots/blob/final-project/docs/brain_diagram.jpg)

### Mutation of Brains
- A random synapse (arrow in the diagram above) either connecting a sensor neuron to a hidden neuron or a motor neuron is chosen and then the weight is changed within the range of [-1, 1]