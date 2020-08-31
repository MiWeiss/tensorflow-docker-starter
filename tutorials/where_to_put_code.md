## Where to put my code?

The tutorials and scripts in this repo expect a repo structure as follows:

* Source code goes into `my_project`
 
* Test modules go into `tests` (note that they must contain a `from .context import my_project` statement).

* Static resources (which are not extremely large) belong in `resources`.
Note: Treat this folder as read-only in your application. 
When building your container for deployment, we will copy these resources in the container.

* Write outputs of your codes (such as results) to `/shared`. 


## Overview of whole starter repository



### Folder Structure
```
tf-docker-starter 
├── my_project           # Sources. Rename it to name of project.
├── tests                # Python tests for your project
│   ├── context.py       # Utility to import `my_project` into tests. Replace `my_project` ref! 
│   └── test_example.py  # An example test module
├── docker               # Generated Folder!
│   ├── cpu              # Dockerfiles for cpu-based tensorflow
│   │   ├── env          # Dockerfiles with only dependencies and resources (for development)
│   │   └── full         # Dockerfiles including sources and tests (for deployment)
│   └── gpu              # Dockerfiles for gpu-based tensorflow. Useable on Linux only.
│   │   └── ...          # (same as for 'cpu')
│   └── ...              
├── scripts 
│   ├── gen_dockerf.py   # Generates the `docker` folder based on requirements.txt
│   └── docker_build.py  # Simple wrapper to build images from previously generated dockerfiles   
├── resources            # Resources that will be copied into docker container
├── tutorials            # Instructions on how to use this template
├── requirements.txt     # The pip dependencies of your project
└── ...                  
```

