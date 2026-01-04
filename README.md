# CP-Problems

Here, you'll find an array of problems sourced from platforms like `Leetcode`, `GeeksForGeeks`, `CodeForces`, and `CodeStudio`. Additionally, I've included some handy scripts to streamline your coding experience, such as automatic templating and code prettifying.

## Handy Scripts 

### Automatic Templating

To simplify your workflow, I've provided a script for automatic templating. You can create a new `Python` or `C++` file based on templated provided in `Templates` folder. You can either set it up as a VSCode task or run it standalone using Python. 

#### Setting up as a VSCode task:

**Setup task**

1. Press `Ctrl+Shift+P`.
2. Select `Configure Tasks`.
3. Choose `Create template`.
4. Copy and paste the provided JSON from `Scripts/tasks.json` into the task configuration.

**Run task**

1. Press `Ctrl+Shift+P`.
2. Type `Create template`.
3. Pass the reqiured `cstr` (for more info, see below) without the quotes. For example : `cf/123a/cpp`, `lc/223/py`, etc.

#### Running as a standalone Python script:

```bash
cd Scripts
python create.py --cstr="{platform_shortform}/{problem_number}/{language}"
```

For example:

```bash
python create.py --cstr="cf/1234a/cpp"
```

### Code Prettify + Caching Output

I've created a simple `prettified.py` script to not only format your `Python` and `C++` code but also intelligently caches the output. This means that if a file hasn't been modified since the last prettifying operation, it won't be reformatted unnecessarily. 

> [!NOTE]
> It requires `clang-format` for formatting C++ files though.

Simply run:

```bash
cd Scripts
python prettified.py
```

> [!NOTE]  
> This script also functions as a `pre-commit` hook, ensuring that your code is formatted before any commits.

## Just a Few More Ideas

Here are some future enhancements I'm considering:

- Automatically generating `README.md` files for every problem based on a template.
- Implementing a tiny database using SQLite to map problems with details like name, tags, difficulty, etc.
- Developing a CLI or a simple static web app for displaying stats, such as the number of problems solved, difficulty split, etc.

