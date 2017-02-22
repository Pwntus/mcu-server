const mqtt = require('mqtt')
const path = require('path')
const fs = require('fs')

const init = ({endpoint, thingName}) => {
	const shadowUpdate = `$aws/things/${thingName}/shadow/update`

	const KEY = fs.readFileSync(path.join(__dirname, '../things', thingName, 'privkey.pem'))
	const CERT = fs.readFileSync(path.join(__dirname, '../things', thingName, 'cert.pem'))

	var options = {
		// ca: readFile(join(__dirname, options.certDir, "root.pem")),
		port: 8883,
		protocol: 'mqtts',
		hostname: endpoint,
		cert: CERT,
		key: KEY,
		clientId: thingName
	};

	const client = mqtt.connect(options);
	console.log(options);

	client.on('connect', () => {
		console.log('-- connected');
		//sinPath(shadowUpdate, client);
	});

	client.on('message', (topic, message) => {
		console.log(`Rx - ${topic}:`, message.toString());
		// client.end();
	})

	return {
		client,
		shadowUpdate,
		thingName
	};
}

module.exports = {init};
