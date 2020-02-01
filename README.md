# Chicago Python Algorithms Special Interest Group

## Development

This site is designed for [GitHub Pages](https://pages.github.com/), which is built with [Jekyll](https://jekyllrb.com/), a [Ruby Gem](https://jekyllrb.com/docs/ruby-101/#gems). *No local setup is required*. Simply create a [markdown file](https://guides.github.com/features/mastering-markdown/) in `./_posts/`, and that document will be rendered on the hosted website. See [Jekyll's documentation on Posts](https://jekyllrb.com/docs/posts/).

## Local Development

In order to make changes to the website design or archictecture and preview the website on a local server, you will need a local development evironment. Follow these steps.

### Local Jekyll Setup

Follow the [appropriate guide for your system](https://jekyllrb.com/docs/installation/). Specific notes for Windows are provided here.

#### Windows 10 with WSL

1. [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and Ubuntu from the Microsoft Store
2. Followed the [WSL Jekyll installation guide](https://jekyllrb.com/docs/installation/windows/#installation-via-bash-on-windows-10)
3. If you receive a permission error at `gem update` or `gem install jekyll bundler`, modify your `.bashrc`:
    ```bash
    nano ~/.bashrc
    ```

    `.bashrc` is located at `C:\Users\{USER}\AppData\Local\Packages\{UBUNTU_DIST}\LocalState\rootfs\home\{UBUNTU_USER}\.bashrc`

    Add the following lines (see: [Running Jekyll as Non-Superuser (no sudo!)](https://jekyllrb.com/docs/troubleshooting/#no-sudo):
    ```
    # Ruby exports

    export GEM_HOME=$HOME/gems
    export PATH=$HOME/gems/bin:$PATH
    ```

    Restart the terminal, or reload `.bashrc`:
    ```bash
    . ~/.bashrc
    ```

    Resume the [WSL Jekyll installation guide](https://jekyllrb.com/docs/installation/windows/#installation-via-bash-on-windows-10).

### Local GitHub Pages Setup

1. Prior to `bundle install` below, I had to issue these commands (see [this guide](https://garfbradaz.github.io/blog/2018/12/12/Setting-up-Github-Pages-Jekyll-and-using-Windows-Subsystem-for-Linux.html))
    ```
    sudo apt-get install libpng-dev
    sudo apt-get install --reinstall zlibc zlib1g zlib1g-dev
    ```
2. Install dependencies specified in this repo's [`GemFile`](GemFile)
    ```
    bundle install
    ```
3. Boot the local server
    ```
    bundle exec jekyll serve
    ```

### Miscellaneous

* Syntax styling/highlighting for code blocks was configured via:
    ```
    rougify style github > assets/css/syntax.css
    ```

## Theme Credits

Created from: [BlackrockDigital/startbootstrap-clean-blog](https://github.com/BlackrockDigital/startbootstrap-clean-blog)

Template link: [startbootstrap.com/template-overviews/clean-blog](https://startbootstrap.com/template-overviews/clean-blog)
