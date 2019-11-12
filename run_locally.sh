if [ $((1 + RANDOM % 10)) -eq 1 ]
then
  bundle update;
fi

bundle exec jekyll serve -w --incremental --port=4010
