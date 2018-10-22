# BIOCADE

This is an attempt to create a simulation of cell interactions during the [DinaCon Hacknight](https://hacknight.dinacon.ch/). 
We started with a simple physics simulation trying to emulate brownian motion, heavily based on [arcade's example code](http://arcade.academy/examples/pymunk_box_stacks.html#pymunk-box-stacks). 

## Environment

- [arcade](http://arcade.academy/) - python game framework
- [pymunk](http://www.pymunk.org) -python physics engine based on chipmunk

To get started, you should be able to: 

```
pip install -r requirements.txt
python3 main.py
```

# Things to do

This being a hackathon project, there's a lot of things to still do:

- parameterize
- break out common properties of shapes & sprites into a class hierarchy
- hook into pymunk's collision detection logic and actually apply molecular properties (e.g. different interaction based on an instance's properties).

