const opts = require('./cc_options');
const cc = new (require('cloud-connect'))(opts);
const logger = require('winston');

cc.init().then(() => {
	
	cc.mqtt.on('message', (topic, message) => {
		logger.info('Message received: ', message.toString());
	});

	logger.info('--- subscribing to ', opts.topic);
	cc.mqtt.subscribe(opts.topic);
});
