# Algosig

Algo SIG is Chipy's dedicated special interest group where we discuss and practice all things algorithms.

# How to add new content

1. Fork the repository and clone your fork to your local computer
1. Checkout to src branch `git checkout src`
1. Create a virtual environment `python -m venv venv`
1. Activate the virtual environment
    * Linux: `source venv/bin/activate`
    * Windows: `venv\Scripts\activate`
1. Ensure `pip` up to date `pip install --upgrade pip`
1. Install requirements `pip install -r requirements.txt`
1. Create a new page `nikola new_post -t "Longest Palindromic Substring"`
1. This creates a page under `posts` directory
1. Edit the file created
1. Build and verify locally `nikola build && nikola serve -b`
1. Send a pull-request against the `src` branch

# Deploy

1. Checkout to `src` branch
2. `nikola github_deplpy`
