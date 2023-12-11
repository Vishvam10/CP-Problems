# CP-Problems

This repo currently has problems from `Leetcode`, `GeeksForGeeks`, `CodeForces`
and `CodeStudio`

## Automatic Templating 

- Run this as a VSCode task (`Ctrl+Shift+P` > `Configure Tasks` > `Create template`)

    ```json
    // workspaceFolder : CP-Problems

    {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "Create template",
                "type": "shell",
                "command": [
                    "python3"
                ],
                "args": [
                    "./Scripts/create.py",
                    "--lang=${input:lang}",
                    "--file=${file}"
                ],
                "problemMatcher": [],
                "group": {
                    "kind": "build",
                    "isDefault": true
                },
                "presentation": {
                    "reveal": "silent",
                    "revealProblems": "onProblem",
                    "close": true
                }
            }
        ],
        "inputs": [
            {
                "type": "promptString",
                "id": "lang",
                "description": "Programming language",
                "default": "py"
            }
        ]
    }`/`

    ```


- Run this as a standalone Python script :

    ```bash
        python3 Scripts/create.py \
        --lang=py --file="path_of_new_file"
    ```

## Todo

- `refactor.py` :
    - [ ] Add CLI options 
    - [x] Selective refactor of files wrt extension (like `.py`, `.cpp`, etc.)
    - [ ] Better CLI and prettify

- `get-commit-message.py` :
    - [x] Make changes to adapt to the new refactor
    - [ ] Modify existing CLI options 
    - [ ] Better CLI and prettify

- Add semantic commit messages

## In Future

- Linter setup for various languages
- Write a pre-commit hook to trigger refactor, linting, etc.
- Automatically generate `README.md` file based on a template for every problem

## Just a Few More Ideas

- Create a tiny database (using SQLite) to map these problems to its name, tags, difficulty, etc
- Create a CLI (prettified) (or a webapp maybe) for showing stats (like number of problems solved, difficulty split, etc) 


