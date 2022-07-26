# Python Packaging

##### Goal: Publish your movie recommender as a `pip` installable Python package on GitHub

##### Why?

 - Orthogonality in Software Engineering (https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/):
   	- 1st Department works on the Flask Application, Mobile Application
   	- 2nd Department (Data Science) works on the Recommender Algorithms
   	- The web developers are not interested in which algorithm is used
   	- The Data Scientist are not interested in how their method is used
   	- The two teams only share the common interface, which is the function `recommend_nmf(query, ratings, model, k=10)`

 - Increase visibility and usability of your work
   	- everyone is able to download and use the package with `pip`!
   	- even simple code (just a single function) can be put into a python package!
  
____
 	
- How to structure python code: functions -> classes -> modules (a single .py script) -> package (a folder with modules) -> library (several folders)

- Where are packages located on your computer?

  ```python
  import pandas as pd
  pd.__file__
  ```

#### Python Package Project Structure

```
./project-name
|- README.md
|- LICENSE.txt
|- .gitignore
|- requirements.txt
|- package-name
	|- __init__.py
	|- other_module.py
|- setup.py
```

#### How to install a package

##### Locally

```python
pip install ./project-name
```

or if you are allready inside the project folder

```python
pip install ./
```



#### From GitHub

```python
pip install git+https://github.com/<github-username>/<project-name>
```


#### How to add package dependencies?

add the following argument to your `setup.py`:

```python
install_requires=[
        'pandas',
        'scikit-learn'
]
```


#### How to add external data files?

add the following argument to your `setup.py`:

```python
package_data= {
    '<package-name>': ['data/*.csv', 'trained_models/*.pickle']
}
```


#### How to read in packaged data files?

```Python
import pandas as pd
import os

package_dir = os.path.dirname(__file__)

df = pd.read_csv(package_dir + '/data/my_data.csv')
```


#### How to upload your package to (Test-)PyPi

1. Register an account on https://test.pypi.org/  
2. Build and upload your package:

```shell
pip install --upgrade build
pip install --upgrade twine


python -m build
twine upload --repository testpypi dist/*
```







