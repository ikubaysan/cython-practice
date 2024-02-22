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