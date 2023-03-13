### Bodies
- A random link excluding the first one is chosen and the direction it attaches to the previous link is changed
- Following links's direction are also changed to ensure that there is no overlap and if there is any links that would collide with a previous link then the dimensions are changed
![alt text](https://github.com/itsgohtime/mybots/blob/Asn-8/mutated_body.jpg)

<center>
  
<img width="810" alt="image" src="https://user-images.githubusercontent.com/61445107/224773841-ca274292-445b-4958-a5b2-a98e55cc56c8.png">
  
</center>

### Brains
- A random synapse (arrow in the diagram above) either connecting a sensor neuron to a hidden neuron or a motor neuron is chosen and then the weight is changed within the range of [-1, 1]
