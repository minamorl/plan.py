# plan.py

Task Runner for Python 3.

```python
% cat .plans.py
from plan import plan

@plan("A")
def plan_A(args):
    print("Hi!")

% plan A
Hi!
% cd ..
% cat .plans.py
No such file or directory
% plan A
No rule was found. [FAIL]
```

## How to use

**plan.py** provides `plan` command that detects a `.plans.py` file inside your directory, and runs tasks which you defined in a `.plans.py` file.
You must import plan.plan decorrator inside your .plans.py files:
```python
from plan import plan
```
And then, you can define your task by this way:

```python
@plan("YOUR_PLAN_NAME")
def task_your_plan_name():
    print("Hi!")
```


## Installation

```
% pip install plan-py
```



## Utils

**plan.py** provides `shell` for convenience.

`shell` function is a wrapper, compatible with `submodule.Popen`.

```python
from plan import shell, plan

@plan("A")
def plan_A():
    yield shell(["gulp"], on=your_repository)
```

By default, `shell` function runs executable asynchronously. If a plan function yields shell objects, plan.py takes care those Popen object will be sucessfully terminated.
