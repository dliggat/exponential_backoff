# exponential_backoff

A sample repository for structuring Lambda functions for build/deploy


## Directory Structure

```bash
.
├── Makefile                           # Definition of `make` targets.
├── builds                             # Builds directory.
│   ├── deploy-2016-08-15_16-50.zip
│   └── deploy-2016-08-15_16-54.zip
├── index.py                           # Entry point for the Lambda function.
├── lambda_package                     # Python package `lambda_package`.
│   ├── __init__.py
│   ├── localcontext.py
│   ├── utility.py
├── requirements                       # External dependencies.
│   ├── common.txt
│   ├── dev.txt
│   └── lambda.txt
└── tests                              # Unit tests for the package.
    ├── __init__.py
    └── lambda_package
        ├── __init__.py
        ├── test_localcontext.py
        └── test_utility.py
```

## Initial Setup
In a [new virtualenv](https://github.com/yyuu/pyenv-virtualenv):

```bash
make init
```

## Run tests

```bash
make test
```

## Invoke the function locally

```bash
make invoke
```

## Build a package for Lambda

```bash
make build
```

## Deploy latest build to a Lambda ARN

```bash
ARN=arn:aws:lambda:us-west-2:111111111111:function:my-function-name make deploy
```
