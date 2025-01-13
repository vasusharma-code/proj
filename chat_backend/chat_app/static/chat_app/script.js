// chat_app/script.js
new Vue({
    el: '#app',
    data: {
      users: window.users,  // The users passed from the backend
      selectedUser: null,
      messages: [],
      messageText: ''
    },
    methods: {
      startChat(user) {
        this.selectedUser = user;
        this.messages = [];  // Clear previous messages when a new chat starts
      },
      sendMessage() {
        if (this.messageText.trim() === '') return;  // Prevent sending empty messages
  
        // Add the message to the conversation
        this.messages.push({
          sender: 'You',
          text: this.messageText
        });
  
        // Simulate a response from the selected user
        this.messages.push({
          sender: this.selectedUser.username,
          text: 'Response: ' + this.messageText
        });
  
        this.messageText = '';  // Clear the input field after sending
      }
    }
  });
  