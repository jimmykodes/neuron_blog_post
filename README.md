# Neuron Blog Post Code
The code accompanying a series of blog posts written for CK Collab. Post one can be found 
[here](https://ckcollab.com/2019/07/15/neuron.html).

## Contents

- `generate_data.py` will create a `data.json` for the neuron to work with.
- `data.json` should be formatted as `{'X': [[int, int, ...],[int, int, ...], ...], 'y': [int, ...]}`
- `perceptron.py` contains the neuron app as created in the blog posts
- `app.py` contains the code to actually run the neuron against the generated data. 

### Caveats
This code can certainly be greatly improved on, especially in regards to the data visualization bits. My plan is to
preserve the state of this code as it was at time of writing the blog posts. Please feel free to fork the repo and
make the improvements yourself!