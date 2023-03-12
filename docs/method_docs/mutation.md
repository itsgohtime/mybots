### Bodies
- How bodies are mutated
    - A random link excluding the first one is chosen and the direction it attaches to the previous link is changed
    - Following links's direction are also changed to ensure that there is no overlap and if there is any links that would collide with a previous link then the dimensions are changed
![alt text](https://github.com/itsgohtime/mybots/blob/Asn-8/mutated_body.jpg)

### Brains
- How brains are mutated
    - A random synapse (arrow in the diagram above) either connecting a sensor neuron to a hidden neuron or a motor neuron is chosen and then the weight is changed within the range of [-1, 1]