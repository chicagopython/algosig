# Algosig
Algo SIG is Chipy's dedicated special interest group where we discuss and practice all things algorithms.

# How to add new content

1. Clone the repository from
2. Checkout to src branch `git checkout src`
3. Install requirements `pip install -r requirements.txt`
4. Create a new page `nikola new_post -t "Longest Palindromic Substring"`
5. This creates a page under `posts` directory
6. Edit the file created
7. Build and verify locally `nikola build && nikola serve -b`
8. Send a pull-request against the `src` branch

# Deploy

1. Checkout to `src` branch
2. `nikola github_deplpy`

