# Getting Started

Create venv:
`python3 -m venv venv`

Activate venv:
`source venv/bin/activate`

Install requirements:
`pip install -r requirements.txt`

Compile the pyx:
`python setup.py build_ext --inplace`

Run a profile script:
`python profile_scripts/profile_sum.py`


# Additional Notes

launch.json:
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
```

Makes a debug option. But you can also set the PYTHONPATH to workspaceFolder by default: