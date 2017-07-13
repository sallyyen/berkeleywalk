var firebaseRef = firebase.database().ref("firechat");
var chat = new Firechat(firebaseRef);
chat.setUser(userId, userName, function(user) {
  chat.resumeSession();
  chat.createRoom('Connect and Walk!', 'private', callback(roomId));
  chat.sendMessage(roomId, messageContent, messageType='default', callback);
  
});