#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
	charPrint (c) {
		if (c === undefined) {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			lets s = '';
			for (let j = 0; j < this.height; i++) {
				s += c;
			}
			console.log(s);
		}
	}
}
module.exports = Square;
