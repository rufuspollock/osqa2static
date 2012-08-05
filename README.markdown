## Archiving an OSQA site

Wanted to exclude vast number of query string pages (these would not work on s3 anyway and *huge* amount of duplication:

    wget -mpc -R "*?*=*,?*=*" --user-agent="" -e robots=off ideas.okfn.org

Note that this did have one problem which is we don't get the full listing of questions since that has links like:

    http://ideas.okfn.org/ideas/?sort=active&page=2

Ultimately not a lot we can do about this (hope you can get to questions via user's page ...)

Further cleaning:

    # for ideas.okfn.org
    rm -Rf vote accept_answer answer_link ideas/asked-by mark_favorite markdown_help
    # for getthedata.org
    rm -Rf vote accept_answer answer_link questions/asked-by mark_favorite markdown_help

Also:

* Discovered that archive process had borked the main idea/question page links. Used attached tmp.py script to clean up
* Updated login page and questions/ideas submit page to say site was now archived and read-only
  * would like a header on every page but that is too much hassle atm!

