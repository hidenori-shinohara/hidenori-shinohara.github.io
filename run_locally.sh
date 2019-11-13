if [ $((1 + RANDOM % 10)) -eq 1 ]
then
  bundle update;
fi

# It is necessary to build first because Jekyll's incremental feature is not very smart.
# More specifically, when a new post is added, Jekyll doesn't regenerate index.html.
jekyll build;
bundle exec jekyll serve -w --incremental --port=4010;
