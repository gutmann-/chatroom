# chatroom #
## How to run it ##

```in shell:
python run.py```

...and open this [hyperlink](http://localhost:5000/).
Since I did not implement an authorization/authentication and easy room creatinon
you must set username and new room in URL like this: `http://localhost:5000/static/index.html?user=user&room=room`
where `user` means... hm... user and `room` means room name (will created if not exists).

## Ptotocol description ##

As far as this application build on top of [socket.io](http://socket.io/) protocol you'll need
client library for interacting with it.

#### So this is a list of supported messages: ####

1. For join to the room emit `join` event with following payload:

  ```
  {
    "room": $ROOM_NAME,
    "username": $USERNAME
  }
  ```
Where `$ROOM_NAME` - name of room (it will be created if not exists) and `$USERNAME` - name of user.

2. For send message to the current room emit `message` message with following payload:

  ```
  {
    "username": $USERNAME,
    "room": $ROOM_NAME,
    "text": $TEXT_OF_MESSAGE
  }
  ```
Where `$TEXT_OF_MESSAGE` - text of message.

3. For leaving room emit `leave` message with following payload:
  
  ```
  {
    "room": $ROOM_NAME,
    "username": $USERNAME
  }
  ```
