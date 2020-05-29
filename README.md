# SORSE20 Website repository

This repository contains the source code for the Series of Online Research Software Events 2020. It is based on the [Minimal Mistakes Jekyll theme](https://github.com/mmistakes/minimal-mistakes) and hosted with Github Pages. The static website is build automatically on Github but you can also build it locally.

The documentation how to contribute is in the [Wiki](wiki) of this repository. There you find, how to add new members, new national chapters, how to assign someone to a specific team, etc.

## How to contribute
Unless you know exactly what you are doing, please always

- do not push directly to the master branch (usually you are anyway not allowed to do so). You must contribute via pull request
- we always require a review from another person (four-eye-principle)
- assign issues and pull request to applicable milestones, labels and projects.

New to Github? Don't worry, you'll figure it out fast and it's no problem if it does not immediately work. If you have a problem, ask in slack or create an issue. You should have a look into the [Projects](https://github.com/DE-RSE/SORSE20/projects) tab (see above), that gives you an overview on the current tasks.

## Important facts

- if you have are lacking a link and nevertheless want to add the text as a placeholder, mark it with `{: .missing}`. The link will then be highlighted in red (example: `[some important document](){: .missing}`)
- when referencing internal link, e.g. `{{ site.data.committee.national_chapters.deRSE.internal }}`, use prepend it with a `{{ site.baseurl }}`, otherwise it will not resolve correctly on github. In otherwords

  - `[Software demos]({{ site.data.committee.programme_teams.software_demo }})` :-1: :angry:
  - `[Software demos]({{ site.baseurl }}{{ site.data.committee.programme_teams.software_demo }})` :+1: :green_heart:
  
## Local installation
As we cannot host one version of this site with github pages (generated from the master branch), you should build the website locally and test the implemented changes (or the reviewer in the pull request does it, this is fine as well). To build this site locally:

1. Install ruby for you platform
2. Install `bundle` via `gem install bundler`
3. `cd` to the clone of this repository
4. Run `bundle install`
5. Serve the site locally via `bundle exec jekyll serve`
6. Visit the site in the browser via http://localhost:4000
