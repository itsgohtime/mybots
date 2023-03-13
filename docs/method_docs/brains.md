### Creation of Brains
- The number of links that are sensors are stored and each is made to be a sensor neuron
- There are 4 hidden neurons but it can be changed in constants.py
- Each joint (number of links - 1) is made to be a motor neuron
- Each sensor neuron is connected to every hidden neuron and every hidden neuron is connected to every motor neuron

![brain](https://user-images.githubusercontent.com/61445107/224828585-c555a3ce-b2c6-4ae6-bde8-f9d7585485af.jpeg)

### Mutation of Brains
- A random synapse either connecting a sensor neuron to a hidden neuron or a motor neuron is chosen and then the weight is changed within the range of [-1, 1]
- The diagram belows shows two possible mutations

<div align=center>
  
<img width="718" alt="image" src="https://user-images.githubusercontent.com/61445107/224828153-d2367fc1-aa7b-4959-988d-5e78d1892a80.png">
</div>
