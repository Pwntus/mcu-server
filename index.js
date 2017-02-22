const mqttClient = require('./lib/client');

const opts = mqttClient.init({
  thingName: '00000273',
  endpoint: 'a3k7odshaiipe8.iot.eu-west-1.amazonaws.com'
});
