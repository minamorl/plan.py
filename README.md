# plan.py

Task Runner for Python 3.

```
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

## installation

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
