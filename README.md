# p1-fork.py


**Processes: each indent means a child process is created**

- 77597 parent python process: `python p1-fork.py`
    - 77598 child python process: `python p1-fork.py`
        - 77599 `bash delay-10-seconds.curl`
            - 77600 `curl ...`

Note that all the processes has state S, meaning they are all sleeping.

<img width="2342" height="1788" alt="image" src="https://github.com/user-attachments/assets/377f2a87-aa7a-4107-a418-26129b7934cf" />

# See Also

- [`man ps`](https://man7.org/linux/man-pages/man1/ps.1.html)


