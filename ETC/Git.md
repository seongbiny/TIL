# 지옥에서 온 Git

1. version
2. backup
3. collaborate

* 로그에서 출력되는 버전 간의 차이점을 출력하고 싶을 때

  * ``` 
    git log -p

* 버전 간의 차이점을 비교할 때 

  * ``` 
    git diff '버전 id'..'버전 id2'
    ```

* git add 하기 전과 add한 후의 파일 내용을 비교할 때

  * ```
    git diff
    ```

* 버전 id로 돌아가는 명령

  * ```
    git reset --hard "버전id"
    ```

* 버전 id의 커밋을 취소한 내용을 새로운 버전으로 만드는 명령

  * ```
    git revert "버전 id"
    ```

* git branch 생성

  * ``` 
    git branch 브랜치이름
    ```

* git branch 전환

  * ```
    git checkout 브랜치이름
    ```

    전환하면 마지막 커밋상태로 바뀐다.





 