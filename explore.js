const Twilio = require("twilio");

const client = new Twilio(
    "AC50e36926f48751d00b6677425dbcbdb4",
    "0d82e35026d59277e893bcce7195ad29");

client.messages.list().them(messages => console.log(`The most recent message is ${messages[0].body}`));

console.log('Gathering your message loading');
