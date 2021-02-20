# Backend status [![Build Status](https://jenkins.squared.cf/job/build%20API/badge/icon)](https://jenkins.squared.cf/job/build%20API/)

Use [this](https://www.conventionalcommits.org/en/v1.0.0/#summary) guideline when commiting.

<!--
# Backend assignment [![Build Status](http://34.123.0.188:8080/job/Api%20Grechka/badge/icon)](http://34.123.0.188:8080/job/Api%20Grechka/)

This is our solution to the test assignment of `int20h` hackathon. The task description is [here](https://mcusercontent.com/a90be75a5d6a2bb92a394e975/files/58c87f07-4fd7-4ec9-9119-456d8558f0b3/web_task.pdf) 

* [api server](https://api.squared.cf/)
* [api docs(swagger)](https://api.squared.cf/docs)
* [api docs(redoc)](https://api.squared.cf/redoc)

# HOWTO run

```
# insert your frontend addresses into .env_exmpl file
# and rename it to '.env' file
cp .env_exmpl .env

# build and run the server
./scripts/build.sh 

# runs tests(you don't need to have '.env' to run tests)
# (works only if previous step was done at least once)
# (e.g. the container was build)
./scripts/test.sh
```

# HOWTO query

It's very simple API consisting of one endpoint `/buckwheat`. 
There are three optional parameters:

```
# minimal acceptable weight of the buckwheat in kg
wmin: float = 0.0 

# maxmal  acceptable weight of the buckwheat in kg
wmax: float = inf

# should we display ALL RESults sorted by smallest price/kg?
# if default, returns only one cheapest option from each shop
# in according weight ranges
allres: float = False 
```

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - high performance, easy to learn, fast to code, ready for production framework
- [Nginx](https://www.nginx.com/) - high performance load balancer, webserver, reverse proxy
- [Docker](https://www.docker.com/) - Open platform for developing, shipping, and running applications

## Authors

-   **Vladyslav Stepaniuk** - [VladosK0k0s](https://github.com/VladosK0k0s)
-   **Anna Kryva** - [anna-kryva](https://github.com/anna-kryva)
-   **Nikolay Fedurko** - [B1Z0N](https://github.com/B1Z0N)
-   **Anton Osetrov** - [osetr](https://github.com/osetr)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Кожному українцю по гречці!

-->
