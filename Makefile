#!/usr/bin/make -f

RUN_COMMAND=docker-compose run --rm

ifeq (test,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
  TEST_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(TEST_ARGS):;@:)
endif

UID := $(shell id -u)
GID := $(shell id -g)

export UID
export GID

help:          	   ## show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

tests:         	   ## make test [arguments] == pytest [arguments]  
	$(RUN_COMMAND) builder pytest $(TEST_ARGS)

app_run:           ## run the app in a container
	$(RUN_COMMAND) -d app 

app_logs: app  	   ## run the app and the log files      
	$(RUN_COMMAND) -d kibana&& $(RUN_COMMAND) -d filebeat && $(RUN_COMMAND) -d elasticsearch

stop:              ## stop all running containers   
	docker container stop $$(docker ps -aq) && docker container rm $$(docker ps -aq)
