#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (_err, _res, body) {
	fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
		if (err) {
			console.log(err);
		}
	});
});
