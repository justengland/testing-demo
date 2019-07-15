# Error handling demo project

## Build and Launch Docker Container
```bash
docker build -t jengland/python-tests:latest .
docker run -it --env-file .env --rm -w /usr/src/project -v ${PWD}:/usr/src/project jengland/python-tests bash
```

## Run tests
```bash
python3 -m nose 
```

## Run coverage
```bash
python3 -m nose --with-coverage --cover-html --cover-erase 
```

## Run Linter
```bash
pylint **/*.py
```
