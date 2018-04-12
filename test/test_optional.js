var co = require('co');
var expect = require('expect');
var run = require('./lib.js').run;

describe('Creative Engineer Exam #1 (Open Tests)', () => {
	it('Case #11 should be caluculated', () => co(function*() {
		const input = [
			'2017/02'
		];
		const expected = [
			'0', '0', '0', '0', '0'
		];
		const actual = yield run('./run.sh', [], input.join('\n'));
		expect(actual).toEqual(expected);
	}));

	

	it('Case #12 should be caluculated', () => co(function*() {
		const input1 = [
			'2017/01',
			'2017/01/16 08:00-12:00 13:00-18:00',
			'2017/01/17 08:00-12:00 13:00-18:00',
			'2017/01/18 08:00-12:00 13:00-18:00',
			'2017/01/19 08:00-12:00 13:00-17:00'
		];
		const expected1 = [
			'4', '3', '0', '0', '0'
		];
		const actual1 = yield run('./run.sh', [], input1.join('\n'));
		expect(actual1).toEqual(expected1);

		
	}));
});
