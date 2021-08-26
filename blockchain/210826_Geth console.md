# Metamask, Geth

## Geth console의 account를 metamask로 가져가기

1. Geth console을 키고
2. personal.newAccount(Password)입력
3. 생성된 Json File을 metamask-계정가져오기에서 불러들인다.



## Metamask의 계정을 geth로 import

1. metamask 우측상단에 계정선택

2. 더보기 - 계정상세

3. export private key

4. metamask의 비밀번호를 작성하고 private key를 받는다

5. ```
   web3.personal.importRawKey("개인키","사용할 비밀번호")
   ```

   를 통해서 geth console에 계정추가하면 끝

