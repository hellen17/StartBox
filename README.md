# StartBx-MVP
StartBox MVP template

## Steps to set up the code locally
1. Clone this repository `git clone https://github.com/hellen17/StartBox.git`
2. `cd StartBx` directory
3. Add `.env` file with the environment variables
4. Add ian_cart and ian_account submodules by running this command in the root folder
`git submodule update --init --recursive`
5. Activate virtual environment `pipenv shell`
6. Install dependencies by running the command `pipenv install`
7. Run `python src/manage.py runserver`
8. Navigate to browser at `http://127.0.0.1:8000`
