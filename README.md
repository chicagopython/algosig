# Chicago Python Algorithms Special Interest Group

Algo SIG is a subgroup of [ChiPy](https://www.chipy.org/), the Chicago Python Users Group.

## How to add new content

This site is designed for [GitHub Pages](https://pages.github.com/), which is built with [Jekyll](https://jekyllrb.com/). *No local setup is required*. Simply create a new [markdown file](https://guides.github.com/features/mastering-markdown/) in `./_posts/`, and submit a pull request. Upon approval, it will be rendered on the hosted website. See existing posts for header variables to include.

## Local Development

In order to make changes to the website design or archictecture and preview the website on a local server, you will need a local development evironment. Follow these steps.

### Install Jekyll and Ruby

Follow the [appropriate guide for your system](https://jekyllrb.com/docs/installation/). Specific notes for Windows are provided here.

#### Windows 10 with WSL

1. [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and Ubuntu from the Microsoft Store
2. Follow the [WSL Jekyll installation guide](https://jekyllrb.com/docs/installation/windows/#installation-via-bash-on-windows-10)
    * If you receive a permission error at `gem update` or `gem install jekyll bundler`, read [Running Jekyll as Non-Superuser (no sudo!)](https://jekyllrb.com/docs/troubleshooting/#no-sudo)
    * Modify your `.bashrc` in your Ubuntu user directory:
        ```bash
        nano ~/.bashrc
        ```
    * Add the following lines :
        ```
        # Ruby exports

        export GEM_HOME=$HOME/gems
        export PATH=$HOME/gems/bin:$PATH
        ```

        Restart the terminal, or reload `.bashrc`:
        ```bash
        . ~/.bashrc
        ```
    * Resume the [WSL Jekyll installation guide](https://jekyllrb.com/docs/installation/windows/#installation-via-bash-on-windows-10).

### Install Jekyll Dependencies

With Jekyll installed, you now need to install the dependencies for this particular website.

Install dependencies specified in this repo's [`Gemfile`](Gemfile) and [`Gemfile.lock`](Gemfile.lock)
```
bundle install
```

* On WSL, you may need to issue the following commands prior to `bundle install`. See [this guide](https://garfbradaz.github.io/blog/2018/12/12/Setting-up-Github-Pages-Jekyll-and-using-Windows-Subsystem-for-Linux.html).
    ```
    sudo apt-get install libpng-dev
    sudo apt-get install --reinstall zlibc zlib1g zlib1g-dev
    ```

### Run the Server
```
bundle exec jekyll serve
```

## Miscellaneous
* Syntax styling/highlighting theme for code blocks was set via:
    ```
    rougify style github > assets/syntax.css
    ```

## Theme Credits
[Boostrap](https://getbootstrap.com/) with [Bootswatch](https://bootswatch.com/) theme.
