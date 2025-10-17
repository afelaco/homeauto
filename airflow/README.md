# airflow

# pre-commit

> The full set of options for the configuration are listed [here](https://pre-commit.com/#plugins).


```bash
uv pip install pre-commit
```

Add a `pre-commit` configuration by generating a basic `.pre-commit-config.yaml` file using:

```bash
pre-commit sample-config
```
Set up the git hook scripts:

```bash
pre-commit install
```

Now `pre-commit` will run automatically on git commit. To uninstall the git hook scripts, run:

```bash
pre-commit uninstall
```
