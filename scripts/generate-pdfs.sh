cd ..
docker run --env-file ci/env.txt -v `pwd`:/github/workspace --rm -it rseng/pdf-generator
