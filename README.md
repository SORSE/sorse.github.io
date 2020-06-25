# SORSE Website repository

This repository contains the source code for the Series of Online Research Software
Events 2020. It is based on the [Minimal Mistakes Jekyll theme](https://github.com/mmistakes/minimal-mistakes)
and hosted with Github Pages. The static website is build automatically on Github
but you can also build it locally.

The documentation how to contribute is in the [Wiki](https://github.com/SORSE/sorse.github.io/wiki) of this repository.
There you find, how to add new members, new national chapters, how to assign
someone to a specific team, etc.

## How to contribute
Unless you know exactly what you are doing, please always

- do not push directly to the master branch (usually you are anyway not allowed
  to do so). You must contribute via pull request
- we always require a review from another person (the four eyes principle)
- assign issues and pull request to applicable milestones, labels and projects.
- if you're working on an issue or PR, assign it to yourself! If you are not working on
  it anymore, remove your assignment from the PR, either because you are finished
  or because you don't have the time to do more, unassign yourself and ideally
  leave a message that someone else should take over.

New to GitHub? Don't worry, you'll figure it out fast and it's no problem if it
does not immediately work. If you have a problem, ask in slack or create an issue.
You should have a look into the [Projects](https://github.com/SORSE/sorse.github.io/projects)
tab (see above), that gives you an overview on the current tasks.

## Important facts

- if you are lacking a link and nevertheless want to add the text as a
  placeholder, mark it with `{: .missing}`. The link will then be highlighted in
  red (example: `[some important document](){: .missing}`)
- when referencing an internal link, e.g. `{{ site.data.committee.national_chapters.deRSE.internal }}`,
  use prepend it with a `{{ site.baseurl }}`, otherwise it will not resolve
  correctly on GitHub. In other words

  - `[Software demos]({{ site.data.committee.programme_teams.software_demo.internal }})` :-1: :angry:
  - `[Software demos]({% include fix-link.html link=site.data.committee.programme_teams.software_demo.internal %}` :+1: :green_heart:


## Local installation
As we cannot host one version of this site with GitHub Pages (generated from the
master branch), you should build the website locally and test the implemented
changes (or the reviewer in the pull request does it, this is fine as well).
To build this site locally, you need to use the command line:

1. Install ruby for your platform
2. Install `bundle` via `gem install bundler`
3. `cd` to the clone of this repository
4. Run `bundle install`
5. Serve the site locally via `bundle exec jekyll serve`
6. Visit the site in the browser via http://localhost:4000

## Preview the Site on CircleCI

We use CircleCI to preview the site for pull requests, and this is controlled by the files
in the [.circleci](.circleci) folder. To use CircleCI, you will need to
make sure you are logged in to the service and following the repository. When you select a build
associated with a pull request, click on the "Artifacts" tab, and select a static file to open
and preview in your browser.

## Testing the installation

We use the [html-proofer](https://github.com/gjtorikian/html-proofer/) to test for
broken links, etc. To run the tests locally, you need to install it (see
[Local installation](#local-installation)) and run the tests via executing
`bundle exec rake`

## License

The contents of the SORSE website and its source code repository is published
under the Creative Commons Attribution 4.0 International Public License (CC BY 4.0).
See the [LICENSE](LICENSE) file for more details.

Copyright (c) 2020, the SORSE committee.

The original software for creating this website, the Minimal Mistakes Jekyll
Theme, is distributed under the MIT license, see
https://github.com/mmistakes/minimal-mistakes#license.

The [MIT license](http://opensource.org/licenses/MIT) also applies for the
`_includes` and `_layouts` folder in this repository.
