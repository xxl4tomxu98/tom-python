# video 1
# commands:
    # `docker version`
    #   => gets version info
    # `docker container run --name banana -p 80:80 nginx`
    #   => start up container named 'banana'
    # docker container ls -a
    #   => shows ALL containers (running + stopped)
    # docker container run --name banana -d -p 80:80 nginx
    #   => running banana container detached
    # docker container stop banana
    #    => stop container
    # docker container inspect banana
    #   => more container info
    # docker container top banana
    #       => processes running INSIDE container
    # docker container rm -f banana
    #   => stop & remove container
