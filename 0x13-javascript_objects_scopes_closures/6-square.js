#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
	charPrint (C) {
		if (C === undefined) {
			C = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			let S = '';
			for (let j = 0; j < this.height; i++) {
				S += C;
			}
			console.log(S);
		}
	}
}
module.exports = Square;
