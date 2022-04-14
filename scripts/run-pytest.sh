if [ -n "$1" ]
then
  while sleep 1 ; do find ./src ./tests -name '*.py' | entr -d nose2 $1; done
else
  while sleep 1 ; do find ./src ./tests -name '*.py' | entr -d nose2 ; done
fi
