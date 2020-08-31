# tf-docker-starter
```diff
- This is currently still under development and not yet complete. 
- Feel free to contact me with suggestions and feedback. 
```

This is a template repository allowing to quickly set up a tensorflow project
with docker support. This is primarily useful in the following two usecases:

- You need to bundle / pack your project or its environment for easy execution by a third party.
- Its the best way to use tensorflow with GPUs on Linux systems.


Folder structure of this repo: 
Loosely based on https://docs.python-guide.org/writing/structure/#test-suite

## How to use this template

0. **System Prerequisites**
    1. Install Docker [Download Page](https://docs.docker.com/get-docker/)
    2. Only on linux with gpu:  Install nvidia-docker ([Instructions](https://github.com/NVIDIA/nvidia-docker)).
    There is no need to install CUDA.
    
1. **Get this template**

    Recommended: Click [here](https://github.com/MiWeiss/tf-docker-starter/generate) to get the template.
    
    You can also fork this repository to get started or copy the `scripts` folder into an existing project.
    
2. **[Optional] Name your project**
    
    Rename the folder `my_project` with the name for your project 
    (must be a [valid python package](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html#packages) 
    name). 
    Also replace the name on line 5 of `tests/context.py` and on all future occasions where
    this tutorial mentions `my_project`. 
    
3. **[Optional] Write some code**

    There's already some sample code in the starter repository:
    If you want you can go straight to the next point to try out the docker environment.

    Otherwise, make sure to put your code at [the right place](./tutorials/where_to_put_code.md).
    
    
4. **Run in a docker container**

    Instructions based you want to set this up using pycharm or the command line: 
    1. Instructions for the Command Line *(coming soon)*
    2. [Instructions for PyCharm](./tutorials/building-with-pycharm.md)
    
    Everything works? Great. Go back to step 3 and continue.
    

    
Once your project is completed, you may want to build a replication package: 
[Instruction to bundle replication package](./tutorials/build-replication-package.md)
    
    

