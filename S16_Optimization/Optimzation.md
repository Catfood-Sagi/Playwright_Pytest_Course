If i want to disable specific resources type i can do it using route handler

**Skipping JavaScript files** - if we want to skip over js files from being loaded we can add "scripts" to the aborted resource types
                                this will about and .js files 


**Disabling JavaScript** - if we want to disable JS altogther, we will need to pass a special argument to our browser context
                            using the java_script_enabled=False

-----
Running Tests in Parallel
-----

by default PyTest runs test 1 by 1
we can use the -n or -numprocesses to specify the numover of thread to use. (can use auto or give a number)
