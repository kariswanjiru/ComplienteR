const Twilio = require("twilio");

const client = new Twilio(
    "AC50e36926f48751d00b6677425dbcbdb4",
    "a6e98b38367fddaeb65447ff539e118a");

client.messages.list()
.then(messages => console.log(`The most recent message is ${messages[0].body}`)).catch(err => console.error(err));

console.log('Gathering your message loading');
