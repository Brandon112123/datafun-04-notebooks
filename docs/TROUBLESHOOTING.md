# Troubleshooting

If you've created the .venv virtual environment,  installed the necessary packages,
and selected a Kernel for your Jupyter Notebook, it should run -
even if the code shows a missing package error. See the image below.

Check Kernel and .venv. VS Code may show an issue, but may still work.
Sometimes closing and reopening the notebook file is helpful.
Make sure your .venv is active and the kernel is selected.

Why Your Notebook May Still Not See a Package

If the Jupyter notebook kernel is not set to the same environment where you installed the package, the package won't be found. This can happen if:

- The terminal in VS Code is pointed to one virtual environment, but the Jupyter kernel is using another. This can occur if you have multiple virtual environments and accidentally select the wrong one for your Jupyter notebook.
- Even if you try to manually point the kernel to the right environment, there might be path conflicts or misconfigurations that prevent the notebook from recognizing the installed packages.

## Recommendations

### Recommendation 1: Keep Virtual Environment and Kernel Aligned

The environment where the Jupyter server runs (where a !pip install in your notebook would install packages) might differ from the environment where the notebook kernel runs.
This can lead to scenarios where a package appears installed in the terminal but isn't accessible within the notebook.
Whenever you create a new virtual environment and want to use it with Jupyter notebooks, you need to install ipykernel and your necessary packages in that environment.

### Recommendation 2: Use Magic Commands (Jupyter commands use %)

Once your project virtual environment and kernel are aligned, if you still have issues, then use magic commands.
Magic commands are interpreted by the IPython kernel and provide a way to interact with the underlying Python environment directly.
Using %pip install ensures that the package is installed in the same environment as the notebook kernel.
To use a magic command, in your Jupyter Notebook, add a Python cell with the install command, for example:

```python
%pip install pandas
```

Note that we don't use the leading py -m that we do when running Python utility commands (pip, venv, etc.) in the terminal.

Virtual environments are recommended to ensure isolation and reproducibility of your project's dependencies.
If you encounter issues with virtual environments and need to install packages directly within a notebook, using magic commands is a reliable alternative.

### Avoid: Shell Commands for Installs (Shell Commands use !)

Don't use !pip install (with an exclamation instead of percent).
This is a shell command, which means it runs in the shell environment of the system where the Jupyter server is running.
While it can work, it might not install the package in the same environment that the notebook kernel is using, especially in environments with multiple Python installations or virtual environments.
