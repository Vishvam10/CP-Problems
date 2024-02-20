# CP-Problems

This repo currently has problems from `Leetcode`, `GeeksForGeeks`, `CodeForces`
and `CodeStudio`

## Automatic Templating 

- Run this as a VSCode task (`Ctrl+Shift+P` > `Configure Tasks` > `Create template`)

    ```json

    // workspaceFolder is CP-Problems

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
                    "create.py",
                    "--cstr=${input:cstr}",
                ],
                "group": {
                    "kind": "build",
                    "isDefault": true
                },
                "options": {
                    "cwd": "${workspaceFolder}/Scripts"
                },
                "presentation": {
                    "reveal": "silent",
                    "revealProblems": "onProblem",
                    "close": true
                }
            },

        ],
        "inputs": [
            {
                "type": "promptString",
                "id": "cstr",
                "description": "Output file"
            }
        ]
    }


    ```


- **OR** Run this as a standalone Python script :

    ```bash
        python3 Scripts/create.py \
        --cstr="{platform_shortform}/{problem_number}/{language}"

        For example :

        python3 Scripts/create.py --cstr="cf/1234a/cpp"

    ```

## Todo

- `refactor.py` :
    - [ ] Add CLI options 
    - [x] Selective refactor of files wrt extension (like `.py`, `.cpp`, etc.)
    - [ ] Better CLI and prettify

- `get-commit-message.py` :
    - [x] Make changes to adapt to the new refactor
    - [x] Modify existing CLI options 
    - [ ] Better CLI and prettify

- Add semantic commit messages

## In Future

- Linter setup for various languages
- Write a pre-commit hook to trigger refactor, linting, etc.
- Automatically generate `README.md` file based on a template for every problem

## Just a Few More Ideas

- Create a tiny database (using SQLite) to map these problems to its name, tags, difficulty, etc
- Create a CLI (prettified) (or a webapp maybe) for showing stats (like number of problems solved, difficulty split, etc) 


