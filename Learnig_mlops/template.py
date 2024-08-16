import os
from pathlib import Path

list_of_files=[

    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    
    "src/components/__inti.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evalutation.py",
    
    "src/pipeline/__inti__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/perdiction_pipeline.py",
    
    "src/utils/__init__.py",
    "src/utils/utils.py",
    
    "tests/unit/__inti__.py",
    "tests/integration/__init__.py",
    "experiment/experiments.ipynb",

    "init_setup.sh",
    "requirement.txt",
    "requirements_dev.txt",
    "setup.cfg",
    "pyproject.toml",
    "toX.ini",
    

]

# running th loop on filepath loop
for filepath in list_of_files: 
    #carring filepath in variable after passing it from "Path" function imported from "pathlib"
    filepath=Path(filepath)
    #sliping filepath as filedir with file name  and also  filename seperately
    filedir,filename=os.path.split(filepath)
    #check file is present if not make them
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
       # logging.info(f"Creating directiory: {filedir} for file: {filename}")

    if(not os.path.exists(filepath) )or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass # create an empty file