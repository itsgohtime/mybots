# Results 

The bodies and brains of the best robot from each seed is stored in the file "best_robots" with the number indicating which seed the robot is from. 

### Seed Data
<div align="center">
 
| Seed | Starting Fitness Avg. | Final Fitness |
| :---: | :---: | :---: |
| 0 | 0.0 | 5.66 |
| 1 | 0.0 | 6.09 | 
| 2 | 0.0 | 5.75 | 
| 3 | 0.0 | 5.96 | 
| 4 | 0.0 | 5.73 | 
| 5 | 0.0 | 6.70 | 
| 6 | 0.0 | 5.35 | 
| 7 | 0.0 | 5.07 | 
| 8 | 0.0 | 4.38 | 
| 9 | 0.0 | 4.72 | 
 
</div>

### Fitness Curves
 ![alt text](https://github.com/itsgohtime/mybots/blob/final-project/docs/fitness%20curves.png)
### [Seed Evolutions](evolution_images.md)

### Discussion
For 8 out of the 10 final bodies, the robot had 5 links; The robots all had similar phenotypes with their body plan resembling a totem pole of three link with the last two remaining links protruding from the three stacked links. The other two links seemed to help balance the robot since as it moved, it would consistently tilt to one direction. The 8 robots all moved using a motion resembling hopping; the one link touching the ground would be the main driver of the hopping motion. The protruding links would sometimes oscillate back and forth, which seemed to slightly tilt the robot, but it still had a net balance in that direction. For example, the robot was moving in the x direction, there may be a link that is oscilatting back and forth in the y direction which caused the robot to sway back and forth in the y direction, but was ultimately stable in the y direction. 

The two bodies that did not have 5 links had 6 links (seed 4) and 8 links (seed 8). The body with 6 links still strongly resembled the 8 bodies with 5 links with a upright position and moved using a hopping motion; the sixth link was really small and did not seem to little to no influence on the body compared to the robots with 6 links. On the other hand, the robot with 8 links was drastically different. The robot moved by falling over and then it used one of the links to push itself forward along the ground. While it was able to get pretty far, looking at the fitness curves, it was seen that it had the lowest fitness of the 10 seeds. 

In fact, the best robots with a lower number of generations tend to actually resemble the robot from seed 8. Their bodies were more complicated and often off balanced so they would fall over and thus seem to have moved the furthest since their block would be displaced the most compared to other robots that would just move around on the same spot. Additionally, they would often fall forward and then one of their links would move causing it to roll forward, which is what really made these types of robots dominate the population at lower generations. However, the simpler bodies once they had learnt how to hop because they had more range of motion and had the ability to perform a central pattern generator. The larger bodies ended up getting stuck in evolution since they would fall and roll a little, but it was often really hard for them to move a link in a way that helped them move forward. In seed 8, the robot was able to get unstuck because it was able to create a link that protruding from its main body that could move to push itself forward, but often the body plans were too complicated that it was not able to do that. One thing that they were lacking was the ability to remove links, since they could have evolved to have a simpler body plan and potentially create a central pattern generator. 
