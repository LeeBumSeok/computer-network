# Function block description

##### 20171664 소프트웨어학부 이범석



### How to Run

------

압축된 파일 안의 `start.bat`파일을 실행한다.



파일이 실행되지 않으면 Scenario의 역순으로

  1. `receiver_Application_layer.py`

  2. `receiver_Transport_layer.py`

  3. `receiver_Network_layer.py`

  4. `receiver_Datalink_layer.py`

  5. `receiver_Physical_layer.py`

  6. `sender_Physical_layer.py`

  7. `sender_Datalink_layer.py`

  8. `sender_Network_layer.py`

  9. `sender_Transport_layer.py`

   10. `sender_Application_layer.py`

10개의 파일을 실행시킨다.



`Enter the message to send:`의 문구가 나오면 20자리 미만의 이진수를 입력한다.



### 각 코드 block의 구조 및 기능설명
-----

1. `sender_Application_layer.py`

   ```python
   def receiver():
         # Enter a message to be delivered to the user.
         # Send data to Sender Trnasport Layer
   ```

​       `sender()`: 사용자에게 전달할 메세지를 입력받아 Sender의 Transport에게 전송합니다.

  

2. `sender_Transport_layer.py`

   ```python
   def sender():
         # Receive data from Sender Application Layer
         # Encapsulation Data
         # Send data to Sender Network Layer
   ```

​        `sender()`: Sender의 Application Layer에서 전송받은 데이터를 Encapsulation해서 

  						  Sender의 Network Layer에게 전송합니다.

  

3. `sender_Network_layer.py`

   ```python
   def sender():
       # Receive data from Sender Transport Layer
       # Send data to Sender Datalink Layer
   ```

   

  `sender()`: Sender의 Transport에서 전송받은 데이터를 Sender의 Datalink Layer에게 전송합니다.

  

4. `sender_Datalink_layer.py`

   ```python
   def bitStuffing(frame):
       # Bit-stuffing the received message
   
   def sender():
       # Receive data from Sender Network Layer
       # Send data to Sender Physical Layer
   ```

   `bitStuffing(frame)`:  Sender의 Network Layer에서 전송받은 데이터를 Bit-Stuffing합니다.

    `sender()`: Bit-Stuffing된 데이터를 Sender의 Physical Layer에게 전송합니다.

   

5. `sender_Physical_layer.py`

   ```python
   def mlt_3
       _scheme(bitStream):
         # Mlt-3-scheme the received message
     
     def sender():
         # Receive data from Sender Application Layer
         # Send data to Receiver Physical Layer
   ```

​      `mlt_3_scheme(bitStream)`: Sender의 Datalink Layer에서 전송받은 데이터를 

​														 mlt-3-scheme합니다.

​      `sender()`: mlt-3-scheme된 데이터를 Receiver의 Physical Layer에게 전송합니다.

  

6. `receiver_application_layer.py`

   ```python
   def receiver():
       # Receive data from Receiver Transport Layer
   ```

   `receiver()`: Receiver의 Transport Layer에서 전송받은 데이터를 출력합니다.

   

7. `receiver_Transport_layer.py`

   ```python
   def receiver():
       # Receive data from Receiver Network Layer
       # Decapsulation Data
       # Send data to Receiver Application Layer
   ```

   `receiver()`: Receiver의 Network Layer에서 전송받은 데이터를 Decapsulation하여 

   ​						Application Layer에게 전송합니다.

   

8. `receiver_Network_layer.py`

   ```python
   def receiver():
       # Receive data from Receiver Datalink Layer
       # Send data to Receiver Transport Layer
   ```

   `receiver()`: Receiver의 Datalink Layer에서 전송받은 데이터를 Transport Layer에게 전송합니다.

   

9. `receiver_Datalink_layer.py`

   ```python
   def bitUnstuffing(frame):
       # Bit-unstuffing the received message
   
   def receiver():
       # Receive data from Receiver Physical Layer
       # Send data to Receiver Network Layer
   ```

   `bitUnstuffing(frame)`: Receiver의 Physical Layer에서 전송받은 데이터를 

   ​											 Bit-unstuffing 합니다.

   `receiver()`: Bit-unstuffing된 데이터를 Network Layer에게 전송합니다.

   

10. `receiver_Physical_layer.py`

    ```python
    def mlt_3_scheme_reverse(bitStream):
        # Reverse the received mlt-3-scheme
    
    def receiver():
        # Receive data from Sender Physical Layer
        # Send data to Receiver Datalink Layer
    ```

    

    `mlt_3_scheme_reverse(bitStream)`:  Sender의 Physical Layer에서 전송받은 mlt-3-scheme 

    ​																	 데이터를 Reverse합니다.

    `receiver()`: mlt-3-scheme된 데이터를Receiver의 Datalink Layer에게 전송합니다.
    
    

### 실행 결과

------

![실행결과](C:\Users\qpwoe\OneDrive - 국민대학교\이범석\수업\3학년 1학기 (2021)\컴퓨터네트워크\코딩과제\기말대체과제\컴네-기말고사-20171664-이범석\실행결과.png)

위에 소개한 순서대로 작동되는 모습이다.



------

한 학기동안 어려운 내용 독려해주시며 가르쳐주셔서 감사합니다.

많은 내용을 배워서 뿌듯합니다.

어려운 상황에서 건강 유의하셔서 다음 학기에는 강의실에서 뵙고 싶습니다.

감사합니다.



------

이범석

국민대학교 소프트웨어학부, 20171664

Mobile 010-6401-6042

[qpwoeiru6486@gmail.com](mailto:qpwoeiru6486@gmail.com)

[ijkoo16@kookmin.ac.kr](