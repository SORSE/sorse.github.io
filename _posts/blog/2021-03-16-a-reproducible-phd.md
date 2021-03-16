---
title: "Four pillars of a reproducible PhD"
category: blog
permalink: /blog/a-reproducible-phd/
tags:
  - posters
  - reproducibility
sidebar:
  nav: programme
classes: wide
last_modified_at: 2021-03-16
id: 1
excerpt: |
  As the academic community continues to embrace open science and reproducible research, it is increasingly important for an academic to understand the tools which can make research easier, more accessible and more sustainable. It can be challenging to absorb so many different good practices while still getting research done. However, I would argue that *anything helps*. While all good practices in open science are important, even just incorporating one example is good for the community, and provides a solid personal foundation for gradually incorporating more good practices.
affiliations:
  - index: 1
    name: University College London, UK
author: &id001
  affiliation: 1
  name: Jamie Quinn
  orcid: 0000-0002-0268-7032
authors:
- *id001
---

<div>
  {% include event-authors.html event=page %}
</div>

*Note: this blog has previously been published on [Jamie Quinn's blog](http://blog.jamiejquinn.com/a-reproducible-phd)*

As the academic community continues to embrace open science and reproducible research, it is increasingly important for an academic to understand the tools which can make research easier, more accessible and more sustainable. It can be challenging to absorb so many different good practices while still getting research done. However, I would argue that *anything helps*. While all good practices in open science are important, even just incorporating one example is good for the community, and provides a solid personal foundation for gradually incorporating more good practices.

> Raise your quality standards as high as you can live with, avoid wasting your time on routine problems, and always try to work as closely as possible at the boundary of your abilities. Do this, because it is the only way of discovering how that boundary should be moved forward.
>
>Edsger Wybe Dijkstra

In this blog post I'll be presenting my experience trying to produce an open, reproducible PhD thesis by describing what I think are the four pillars of reproducible research and how I incorporated them into my own research. Most of the good practices I detail here I've picked up by attending talks or reading blog posts by the [Open Science Foundation](https://osf.io/) and the [Software Sustainability Institute](https://www.software.ac.uk/). This post is not meant to teach you *how* to use any of the tools I've used, only to give you an idea of *what* is possible and *why* I chose these particular tools. My final caveat, although I describe writing a thesis in science using these tools, I believe many of these tools can be used for any kind of research in any field.

## Who am I?

Currently I'm a research software engineer at UCL but in a very recent past life I was a PhD student at the University of Glasgow researching viscosity in the solar atmosphere (i.e. asking how runny is the sun?). As with many applied mathematics PhDs the research involved a great deal of high-performance computing, large data files, complex codes and analysis pipelines. Without the tools I describe here my life would have been hell.

Considering my PhD research with hindsight, I can identify four principles which I now think are the foundation of a reproducible thesis. In no order these are:

1. Version control
2. Automation
3. Open publication
4. Sustainable software

## The first pillar: Version control

> Anyone who has never made a mistake has never tried anything new.
>
> Albert Einstein

Version control is a way to record the history of a project by "committing" changes as you work. This has many advantages (see [Why Use Version Control](https://www.git-tower.com/learn/git/ebook/en/desktop-gui/basics/why-use-version-control/)) but for a PhD student it is primarily a good way to store revisions to your code and thesis. With version control, you can jump back in time to a point when you hadn't deleted that one paragraph, or a moment when your code actually worked. Most modern versions of Microsoft tools have some kind of version control and many cloud services also automatically store histories of files, however, I would recommend learning the basics of git, an extremely popular version control tool. It is also the entire basis for [GitHub](https://github.com/), a platform for storing git "repositories" online and if you choose, publicly. For writing a thesis stored on Github all you need to know about git can be learned from [Learn the Basics of Git in Under 10 Minutes](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/). If you want to go deeper I highly recommend [Seth Robertson's Git Best Practices](http://sethrobertson.github.io/GitBestPractices/). You may also end up needing [Git LFS](https://git-lfs.github.com/) to version larger, binary files like images and videos. It's very easy to set up and can help prevent your git repository becoming too large.

The simulations I tended to run involved running the same code but with slightly different configurations. Using git branches provides an easy way to track multiple different versions of the same code and to jump between them as needed. This prevents the typical issue of having slightly different copies of the code spread over multiple folders (`simulation_final_v1.3_1_test` anyone?). In my work, if I wanted to develop a new simulation, I could start on the "main" branch, containing the basic code, then create a new branch and make the required changes. This had the additional advantage that when it came to citing all these different versions, I used [Zenodo](https://zenodo.org/) to generate DOIs for each branch in git without much faff.

While most kinds of files can simply be stored in either git or git LFS, if you use jupyter notebooks, versioning can be a thorny issue. The raw notebooks can be large and although they are technically plain text, they are not particularly suitable for git. Tools like [ReviewNB](https://towardsdatascience.com/introducing-reviewnb-visual-diff-for-jupyter-notebooks-6797e6dfa20c) do allow notebooks to be compared (similar to `git diff`) however it's not perfect and still doesn't solve the size issue. This is essentially because jupyter notebooks stores both the code and cell outputs (including images). This blog post on [Git Version Control with Jupyter Notebooks](https://towardsdatascience.com/version-control-with-jupyter-notebooks-f096f4d7035a) details how you can set up jupyter to save every notebook as a `.Rmd` R-markdown file (which gets saved by git), along with the regular `.ipynb` notebook file (which does not). The Rmd format does not save any outputs and represents purely the *code* contained within a notebook and, as a result, can be handled by git in a much cleaner way.

## The second pillar: Automation

>Automation is cost cutting by tightening the corners and not cutting them.
>
>Haresh Sippy

The more pieces of your research you can automate, the better. Doing the same task over and over again *manually* is not only boring and time-consuming, but prone to human error. In my case, when I was running many simulations I had to edit a number of files ever so slightly but in a very predictable way. Were I to mistype just once, it could take weeks for my long-running simulations to display any issues. This kind of repeatable, mundane task is where computers shine.

For automating many tasks bash is a quick-to-learn scripting language which looks horrible and confusing but is really quite simple and extremely versatile. I personally used bash "scripts" to automatically copy, edit and run entire simulations which, otherwise, would have taken hours to do manually. For a quick introduction, check out this [Introduction to the Bash Command Line](https://programminghistorian.org/en/lessons/intro-to-bash) or try and attend your local [Software Carpentry](https://software-carpentry.org/).

Another incredibly useful tool is `make` and its corresponding makefile, a file which describes the recipe for performing a number of interdependent tasks. By interdependent I mean you can describe one process (say producing a figure from a dataset) which depends on another (say processing that dataset from raw data) which may depend on any other number of processes. If you're half way through the analysis and you've already processed some data, `make` will recognise that and only run the missing pieces of the pipeline. Additionally, you can tell make to run in parallel, running many pipelines at once. For example when I was processing hundreds of files, I could use `make -j4` to tell make to run 4 pipelines at once (on my 4-core computer). Because I'd already described all the dependencies in my makefile, `make` understood which processes could be run independently and which could not. Make allows the simple description of complex pipelines which can dramatically speed up analysis. Check out this [Introduction to Make](http://matt.might.net/articles/intro-to-make/) for a great introduction.

The final piece of automation I used heavily in my thesis writing involved moving large amounts of data usually to and from computing clusters. The command `rsync` is an alternative to `sftp`, `ftp` and `scp` (if you've ever used any of those tools) but shines in one simple way: it knows which files have already been downloaded. This was extremely important to my workflow since I could run `rsync` to automatically download only the files which had been created by my long-running simulations since the last time I ran `rsync`.

## The third pillar: Open publication

> Publishing research without data is simply advertising, not science

Open science necessarily requires open publication of papers, code and data. While you may not have much control over whether your paper is published as open access (budget depending) you still have options for ensuring your research is widely and freely accessible. Theses are almost always publishable as open access through a university's library (assuming there are not issues with confidentiality) but for releasing papers, I recommend using a preprint service such as

- [arXiv](https://arxiv.org/) mainly for physics, mathematics and computer science
- [EarthArXiv](https://eartharxiv.org/) for earth sciences
- [bioRxiv](https://www.biorxiv.org/) and [medRxiv](https://www.medrxiv.org/) for life and health sciences

These services allow the *legal* sharing of papers both before and after journal publication, although they are not strictly peer-reviewed.

Publishing code can be done simply by hosting it publicly on Github or any other platform. This has the additional benefit of encouraging collaboration. When citing specific versions of code on Github, I recommend Zenodo for generating DOIs. Zenodo will take a full copy of the code, ensuring the citation is not lost if your code is removed from Github for any reason. It's important to consider both the licensing you want for your own code and any licences inherited from code you've used. I recommend [Choose A Licence](https://choosealicense.com/licenses/) for an overview of the various open source licenses available and their implications and this article on [Choosing an open-source licence](https://www.software.ac.uk/resources/guides/choosing-open-source-licence) for broader information.

If your code is sufficiently large, well-used or solves a novel problem in a novel way, you might consider publishing it in a journal specifically for software, for example in the [Journal of Open Source Software](https://joss.theoj.org/). Alternatively check out [In which journals should I publish my software?](https://www.software.ac.uk/which-journals-should-i-publish-my-software#node-782) for a list of potential journals for publishing software.

The publication of data can be trickier and I won't attempt to give advice on this because I wasn't particularly happy with the way I shared data from my own thesis. In my case, the data files produced by the simulations were too large to store anywhere (they were over 10 TeraBytes!) so I opted to unambiguously share the specific versions of the code used to run the simulations and all associated parameters, along with all analysis scripts and instructions for running everything. This way, although the data was not itself available, the results could be reproduced.

## The fourth pillar: Sustainable software

If you've used version control, automated most of your processes and analysis, and published your code and data appropriately, you've already produced some very sustainable software. From my experience, to make software even more maintainable, you should develop good habits of documenting your code (see [The value of code documentation](https://www.olioapps.com/blog/the-value-of-code-documentation/)) as well as regularly refactoring your code (see [The benefits and pitfalls of code refactoring](https://softwarebrothers.co/blog/the-benefits-and-pitfalls-of-code-refactoring/)) particularly if you're working in notebooks. I'd also encourage you to get into the habit of testing your code, perhaps through a unit test framework (there's one for *every* language) or self-written integration tests. For extra points you could even automate testing through Github. For projects of any size, regularly running a variety of tests imbues trust in your results. Once again, the Software Sustainability Institute has a great guide on [Testing your software](https://software.ac.uk/resources/guides/testing-your-software).

For more information on making your software more sustainable, check out the Software Sustainability Institute's [guide to getting up to speed with good software practices](https://www.software.ac.uk/resources/get-speed).

## Conclusion

By leveraging version control to stored revisions and backups, automation tools to make my workflow faster and more reliable, open publication to ensure my research could be accessed and reproduced by anyone, and good coding habits to improve my software's reproducibility, I was able to create what I believe to be a reproducible thesis.

I encourage you to consider how you might make your research more reproducible, perhaps using some of the tools I've described here, or perhaps others. I'd love to hear about your journey and I am always open to hearing about new practices and tools for making research more sustainable so please get in touch on [Twitter](https://twitter.com/jimjonquinn) or by [email](mailto:jamiejquinn@jamiejquinn.com).
