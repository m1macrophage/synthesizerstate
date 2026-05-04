# license:BSD-3-Clause
# copyright-holders:m1macrophage

# This script generates an NVRAM file for the factory patches of the prophet5
# rev 3.0. These should also be the same for revs 3.1, 3.2 and "file 1" patches
# of rev 3.3.
#
# The patch data was obtained from the operation manual. The switch states are
# unambiguous. However, the resolution of the knobs in the diagram is ~20
# positions, which is lower than the 121 possible stored values. In other words,
# the knob settings will not match the factory patches exactly.
#
#
# Each patch occupies 24 bytes of NVRAM.
#
# The positions for each of the 24 black knobs is stored at a 7 bit resolution,
# in the addresses below. The position of the grey knobs (Master Tune, Volume)
# is not stored.
#
# 0x00 - filt attack
# 0x01 - filt decay
# 0x02 - filt sustain
# 0x03 - filt release
# 0x04 - amp attack
# 0x05 - amp decay
# 0x06 - amp sustain
# 0x07 - amp release
# 0x08 - filt cutoff
# 0x09 - filt env amt
# 0x0A - osc b mix
# 0x0B - osc b pw
# 0x0C - osc a mix
# 0x0D - osc a pw
# 0x0E - noise mix
# 0x0F - filt res
# 0x10 - glide
# 0x11 - lfo freq
# 0x12 - wmod src mix
# 0x13 - pmod osc b amt
# 0x14 - pmod filt env amt
# 0x15 - osc a freq
# 0x16 - osc b freq
# 0x17 - osc b fine
#
# The state of each of the 22 black buttons is stored in the most significant
# bit of the patch addresses below. The state of the grey buttons is not stored.
#
# 0x00 - osc a pulse
# 0x01 - osc a ramp
# 0x02 - osc a sync
# 0x03 - osc b ramp
# 0x04 - osc b tri
# 0x05 - osc b pulse
# 0x06 - osc b kbd
# 0x07 - unison
# 0x08 - pmod freq A
# 0x09 - pmod pw A
# 0x0A - pmod filt
# 0x0B - lfo ramp
# 0x0C - lfo tri
# 0x0D - lfo pulse
# 0x0E - filt kbd
# 0x0F - release
# 0x10 - wmod freq a
# 0x11 - wmod freq b
# 0x12 - wmod pw a
# 0x13 - wmod pw b
# 0x14 - wmod filter
# 0x15 - osc b lo


from dataclasses import dataclass


PATCH_SIZE = 0x18
F = False
T = True


def get_patches():
	return [
		# Bank 1
		patch(  # 1-1
			pmod(0, 0, F, F, F), lfo(6.5, F, T, F), wmod(0, T, T, F, F, F),
			osca(2.5, T, F, 2, F), oscb(4, 0, F, F, F, 2, F, T),
			mix(10, 10, 0), misc(6.5, F, T),
			filt(0, 0, 7, T, 4.5, 5.5, 5, 4.5), amp(4, 4, 6, 5),
		),
		patch(  # 1-2
			pmod(0, 0, F, F, F), lfo(6.5, F, T, F), wmod(0, F, F, T, T, F),
			osca(2.5, F, T, 3, F), oscb(2.5, 1.5, F, F, T, 3, F, T),
			mix(4, 4, 0), misc(0, F, T),
			filt(5.5, 0, 0, T, 0, 0, 0, 0), amp(6, 4, 10, 5.5),
		),
		patch(  # 1-3
			pmod(0, 0, F, F, F), lfo(7, F, T, F), wmod(0, F, F, F, F, T),
			osca(2.5, F, T, 1.5, F), oscb(2.5, 0, F, F, T, 1.5, F, T),
			mix(10, 10, 0), misc(0, F, F),
			# The diagram shows both the amp decay and sustain as 0. But that's
			# probably wrong. Going with a decay of 5.
			filt(5.5, 3, 4.5, F, 0, 6, 6, 6.5), amp(0, 5, 0, 6.5),
		),
		patch(  # 1-4
			pmod(5, 10, T, F, F), lfo(6, F, T, F), wmod(0, F, F, F, T, F),
			osca(4, F, T, 5, T), oscb(4, 0, F, T, T, 5, F, T),
			mix(10, 10, 0), misc(0, F, T),
			filt(2.5, 6, 2.5, T, 0, 7, 3, 7), amp(3, 7.5, 0, 6),
		),
		patch(  # 1-5
			pmod(0, 2, F, F, T), lfo(7, F, F, T), wmod(0, T, F, F, F, F),
			osca(6, T, F, 5, F), oscb(5.5, 0, F, T, F, 5, T, F),
			mix(10, 0, 0), misc(0, F, T),
			filt(2.5, 0, 3.5, T, 5, 7, 7, 5), amp(5, 6, 8, 5),
		),
		patch(  # 1-6
			pmod(0, 0, F, F, F), lfo(6.5, F, T, F), wmod(0, F, F, T, T, F),
			osca(4.5, F, T, 1.5, F), oscb(6, 0, F, F, T, 9, F, T),
			mix(6, 10, 0), misc(0, F, T),
			filt(10, 5, 0, T, 0, 0, 0, 0), amp(0, 7, 0, 4),
		),
		patch(  # 1-7
			pmod(6, 0, T, F, F), lfo(7, F, T, F), wmod(0, F, T, F, F, F),
			osca(3, T, F, 5, T), oscb(2.5, 0, F, F, F, 5, F, T),
			mix(5, 5, 0), misc(6, F, F),
			filt(5.5, 2, 0, T, 4, 6, 0, 7), amp(0, 0, 10, 7),
		),
		patch(  # 1-8
			pmod(0, 0, F, F, F), lfo(7, F, T, F), wmod(0, F, T, F, F, F),
			osca(7, F, T, 5, F), oscb(2.5, 0, F, T, F, 5, F, T),
			mix(4, 7, 0), misc(0, F, T),
			filt(3.5, 0, 4, T, 0, 6, 2.5, 4), amp(0, 0, 10, 4),
		),

		# Bank 2
		patch(  # 2-1
			pmod(0, 0, F, F, F), lfo(7, F, T, F), wmod(0, T, T, F, F, F),
			osca(4.5, T, F, 3, F), oscb(3, 0, T, F, F, 3, F, T),
			mix(5, 5, 0), misc(6, T, T),
			filt(2, 6.5, 10, T, 0, 10, 10, 7.5), amp(0, 5, 10, 8),
		),
		patch(  # 2-2
			pmod(0, 0, F, F, F), lfo(6.5, F, T, F), wmod(0, F, F, T, T, F),
			osca(4.5, F, T, 5, F), oscb(4, 2, F, F, T, 5, F, T),
			mix(3, 3, 0), misc(0, F, T),
			filt(6.5, 0, 0, T, 0, 0, 0, 0), amp(5.5, 6, 8, 5.5),
		),
		patch(  # 2-3
			pmod(0, 0, F, F, F), lfo(7, F, T, F), wmod(0, F, T, F, F, F),
			osca(4.5, F, T, 3, F), oscb(4.5, 0, F, F, T, 3, F, T),
			# Mix Osc B missing. Using the same value as A.
			mix(6, 6, 0), misc(6, F, T),
			filt(3.5, 7, 3.5, T, 0, 0, 5, 4), amp(0, 0, 7, 2),
		),
		patch(  # 2-4
			pmod(0, 0, F, F, F), lfo(5, F, T, F), wmod(0, F, F, T, F, F),
			osca(6, F, T, 5, F), oscb(6, 2.5, F, T, F, 5, F, T),
			mix(5, 10, 0), misc(0, F, T),
			# Amp sustain is not drawn clearly. It could be 0.5.
			filt(2, 5, 5, T, 0, 6, 7, 7.5), amp(2, 6, 0, 6.5),
		),
		patch(  # 2-5
			pmod(2.5, 2.5, F, T, F), lfo(7, F, T, F), wmod(0, T, F, F, F, F),
			osca(4.5, T, T, 5, F), oscb(5.5, 0, F, T, F, 5, T, F),
			mix(10, 0, 0), misc(6, F, T),
			filt(1.5, 0, 4.5, T, 5, 7, 6, 5), amp(5, 5, 10, 5),
		),
		patch(  # 2-6
			pmod(2, 5, F, F, T), lfo(7, F, T, F), wmod(0, T, T, F, F, T),
			osca(4.5, T, F, 5, F), oscb(4.5, 0, T, F, F, 5, F, T),
			mix(10, 10, 0), misc(6, F, F),
			filt(2.5, 5, 0, T, 4, 6, 0, 6), amp(3, 0, 10, 6),
		),
		patch(  # 2-7
			pmod(0, 0, F, F, F), lfo(7, F, T, F), wmod(0, F, T, F, F, F),
			osca(6.5, F, T, 5, T), oscb(4, 0, F, F, F, 5, F, T),
			mix(5, 5, 0), misc(6.5, F, T),
			filt(5, 0, 2, T, 2, 0, 10, 7), amp(5, 5, 6, 4),
		),
		patch(  # 2-8
			pmod(0, 0, F, F, F), lfo(6.5, F, T, F), wmod(0, T, T, F, F, F),
			osca(2.5, T, F, 5, F), oscb(3.5, 0, T, F, F, 5, F, T),
			mix(10, 10, 0), misc(0, F, F),
			filt(2, 0, 7, T, 5, 5.5, 6.5, 5), amp(3, 4, 6, 5),
		),

		# Bank 3
		patch(  # 3-1
			pmod(0, 0, F, F, F), lfo(7, F, T, F), wmod(0, T, T, F, F, F),
			osca(6, F, F, 5, F), oscb(6, 0, F, T, F, 5, F, T),
			mix(8, 8, 0), misc(0, F, T),
			filt(3, 5, 5, T, 3, 4, 5, 6), amp(5, 8, 6, 5),
		),
		patch(  # 3-2
			pmod(7, 0, T, F, F), lfo(7, F, T, F), wmod(0, F, T, F, F, F),
			osca(3, F, T, 5, T), oscb(2.5, 0, F, F, F, 5, F, T),
			mix(4, 4, 0), misc(6, F, T),
			filt(3.5, 0, 5, T, 4, 7, 3, 3.5), amp(0, 10, 9, 0),
		),
		patch(  # 3-3
			pmod(0, 10, T, F, F), lfo(7, F, T, F), wmod(0, T, F, F, F, F),
			osca(4.5, F, T, 5, T), oscb(4.5, 0, F, T, T, 5, F, T),
			mix(6, 5, 0), misc(0, F, T),
			filt(2.5, 2, 3, T, 0, 7, 3, 7), amp(0, 7.5, 0, 7),
		),
		patch(  # 3-4
			pmod(0, 0, F, F, F), lfo(7, F, T, F), wmod(0, F, F, T, T, F),
			osca(6, F, T, 3, F), oscb(6, 1.5, F, F, T, 3, F, T),
			mix(4, 4, 0), misc(0, F, T),
			filt(6, 0, 4, T, 7, 7, 8, 5.5), amp(6, 4, 10, 6),
		),
		patch(  # 3-5
			# Using LFO freq of 7 instead of 7.5.
			pmod(0, 0, F, F, F), lfo(7, F, T, F), wmod(0, T, T, F, F, F),
			osca(2.5, T, F, 5, F), oscb(4.5, 0, T, F, F, 5, F, T),
			mix(4, 4, 0), misc(6, F, F),
			filt(10, 0, 0, T, 0, 0, 0, 6), amp(0, 0, 10, 6),
		),
		patch(  # 3-6
			pmod(4.5, 0, F, T, F), lfo(7.5, F, T, F), wmod(0, T, F, F, F, F),
			osca(4.5, F, T, 8, F), oscb(4.5, 1.5, F, F, T, 8, F, T),
			mix(8, 8, 0), misc(0, F, T),
			filt(6, 3, 2.5, T, 3, 0, 10, 5), amp(3, 4.5, 8, 6),
		),
		patch(  # 3-7
			pmod(5, 0, F, T, F), lfo(7.5, F, T, F), wmod(0, T, F, F, F, F),
			osca(8, F, T, 5, F), oscb(2.5, 0, T, T, T, 5, F, T),
			mix(5, 5, 0), misc(6, F, T),
			filt(6, 3.5, 0, T, 0, 6, 0, 0), amp(0, 0, 10, 5),
		),
		patch(  # 3-8
			pmod(0, 6, F, F, T), lfo(6.5, F, T, F), wmod(0, T, T, F, F, F),
			osca(6, T, F, 5, F), oscb(6, 2, T, F, F, 5, F, T),
			mix(10, 0, 0), misc(0, F, T),
			filt(3, 0, 3.5, T, 0, 5, 5, 6), amp(0, 2, 6, 6.5),
		),

		# Bank 4
		patch(  # 4-1
			pmod(0, 10, F, T, F), lfo(6.5, F, T, F), wmod(0, F, F, T, F, F),
			osca(4.5, F, T, 5, F), oscb(3, 0, F, T, F, 5, T, F),
			mix(10, 0, 0), misc(0, F, T),
			filt(4.5, 7, 0, T, 0, 0, 0, 0), amp(3, 4.5, 7, 8),
		),
		patch(  # 4-2
			pmod(10, 0, T, F, F), lfo(6.5, F, F, T), wmod(0, T, F, F, F, F),
			osca(4.5, F, T, 2, T), oscb(4.5, 0, F, F, F, 5, F, T),
			mix(4.5, 4.5, 0), misc(0, F, T),
			filt(10, 0, 10, F, 7.5, 7.5, 0, 6), amp(0, 4, 7, 7),
		),
		patch(  # 4-3
			pmod(0, 0, F, F, F), lfo(4.5, F, T, F), wmod(0, F, F, T, T, F),
			osca(4.5, F, T, 2, F), oscb(4, 0, F, F, T, 7, F, T),
			mix(6, 6, 0), misc(0, F, T),
			filt(3, 7, 8, F, 8, 8, 0, 8), amp(4.5, 6, 8, 8),
		),
		patch(  # 4-4
			pmod(0, 4, F, T, F), lfo(2.5, F, T, F), wmod(0, F, F, F, F, T),
			osca(4, F, T, 5, F), oscb(5.5, 0, F, T, F, 5, T, F),
			mix(5, 0, 0), misc(0, F, T),
			filt(7, 7, 0, T, 0, 0, 0, 0), amp(3, 0, 10, 10),
		),
		patch(  # 4-5
			pmod(7, 0, T, F, F), lfo(7, F, T, F), wmod(0, F, F, T, F, T),
			osca(4.5, F, T, 4, T), oscb(0, 0, F, F, T, 4, F, T),
			mix(6, 4, 0), misc(0, F, F),
			filt(3, 0, 8, T, 8, 0, 10, 8), amp(3, 0, 10, 8),
		),
		patch(  # 4-6
			pmod(0, 10, F, F, T), lfo(4, T, F, F), wmod(0, F, T, F, F, F),
			osca(2.5, T, F, 3, F), oscb(4, 0, F, F, T, 2, T, F),
			mix(6, 0, 0), misc(0, F, T),
			filt(2, 0, 0, T, 0, 0, 0, 0), amp(0, 3.5, 10, 10),
		),
		patch(  # 4-7
			pmod(0, 10, F, T, T), lfo(5, F, T, F), wmod(0, F, F, T, F, T),
			osca(2.5, F, T, 5, F), oscb(0, 0, T, F, F, 5, T, F),
			mix(7, 0, 0), misc(0, F, T),
			filt(5, 5, 0, T, 0, 10, 5, 10), amp(2, 5.5, 10, 10),
		),
		patch(  # 4-8
			pmod(0, 10, T, F, F), lfo(4, F, T, F), wmod(0, F, F, T, F, F),
			osca(5, F, T, 5, F), oscb(4.5, 0, F, T, T, 5, F, T),
			mix(10, 5, 0), misc(0, F, T),
			filt(3, 5, 3, T, 0, 7, 3, 7), amp(0, 7.5, 0, 8),
		),

		# Bank 5
		patch(  # 5-1
			pmod(0, 5, F, F, T), lfo(1, F, T, F), wmod(0, F, T, F, F, F),
			osca(0, F, F, 5, F), oscb(10, 10, F, T, F, 5, F, F),
			mix(0, 0, 0), misc(0, T, T),
			filt(5, 10, 1, F, 10, 10, 0, 10), amp(7.5, 10, 10, 10),
		),
		patch(  # 5-2
			pmod(0, 7, F, F, T), lfo(2.5, F, T, F), wmod(2.5, F, F, F, F, T),
			osca(0, F, F, 5, F), oscb(0, 0, F, T, F, 5, T, F),
			mix(0, 0, 10), misc(0, T, T),
			filt(3, 6, 0, T, 0, 0, 0, 0), amp(0, 0, 6, 10),
		),
		patch(  # 5-3
			pmod(4, 10, T, F, F), lfo(5, F, T, F), wmod(0, F, F, T, F, F),
			osca(2, F, T, 5, F), oscb(2.5, 0, F, T, T, 3, F, T),
			mix(10, 0, 0), misc(0, F, T),
			filt(2, 6, 3, T, 0, 8, 10, 9), amp(0, 7, 10, 9),
		),
		patch(  # 5-4
			pmod(7.5, 6, T, F, F), lfo(7, T, F, F), wmod(0, T, F, F, F, F),
			osca(2, F, T, 4, F), oscb(4, 0, F, F, T, 4, T, T),
			mix(7, 0, 0), misc(0, F, T),
			filt(5, 6, 3, T, 0.5, 9, 5, 6.5), amp(2, 6, 10, 7),
		),
		patch(  # 5-5
			pmod(0, 0, F, F, F), lfo(7.5, F, T, T), wmod(0, F, F, F, F, T),
			osca(0, F, T, 3, T), oscb(3.5, 0, F, F, F, 5, F, F),
			mix(10, 0, 0), misc(10, T, T),
			filt(5.5, 0, 0, F, 0, 0, 0, 0), amp(8, 0, 10, 10),
		),
		patch(  # 5-6
			pmod(0, 5, F, F, T), lfo(4, F, T, F), wmod(0, F, F, F, F, T),
			osca(0, F, F, 5, F), oscb(4, 0, F, F, T, 6.5, F, T),
			mix(0, 0, 0), misc(0, F, T),
			filt(3.5, 10, 0, T, 0, 0, 0, 0), amp(0, 0, 6.5, 7),
		),
		patch(  # 5-7
			# The manual mentions that this is a duplicate of 1-1, but the
			# diagram doesn't match it exactly. Using the diagram for patch 5-7.
			pmod(0, 0, F, F, F), lfo(6.5, F, T, F), wmod(0, T, T, F, F, F),
			osca(2.5, T, F, 1.5, F), oscb(4, 0, F, F, F, 8.5, F, T),
			mix(10, 10, 0), misc(6.5, F, T),
			filt(0, 0, 7, T, 4.5, 5.5, 5, 4.5), amp(4, 4, 6, 5),
		),
		patch(  # 5-8
			# The manual mentions that this is a duplicate of 1-6, but the
			# diagram doesn't match it exactly. Using the diagram for patch 5-8.
			pmod(0, 0, F, F, F), lfo(6.5, F, T, F), wmod(0, F, F, T, T, F),
			# PW A is not shown on the diagram, so using the value from patch 1-6.
			osca(4, F, T, 1.5, F), oscb(6, 0, F, F, T, 1.5, F, T),
			mix(6, 10, 0), misc(0, F, T),
			filt(10, 5, 0, T, 0, 0, 0, 0), amp(0, 7, 0, 4),
		),
	]


def knob2byte(knob_value: float):
	# The max knob wiper voltage is 5V, which the ADC converts to 120.
	return round(120 * knob_value / 10)


@dataclass
class pmod:
	filt_env_amt: float
	osc_b_amt: float
	freq_a: bool
	pw_a: bool
	filt: bool

	def store(self, knobs, switches):
		knobs[0x13] = knob2byte(self.osc_b_amt)
		knobs[0x14] = knob2byte(self.filt_env_amt)
		switches[0x08] = self.freq_a
		switches[0x09] = self.pw_a
		switches[0x0A] = self.filt


@dataclass
class lfo:
	freq: float
	ramp: bool
	tri: bool
	pulse: bool

	def store(self, knobs, switches):
		knobs[0x11] = knob2byte(self.freq)
		switches[0x0B] = self.ramp
		switches[0x0C] = self.tri
		switches[0x0D] = self.pulse
		

@dataclass
class wmod:
	srcmix: float
	freqa: bool
	freqb: bool
	pwa: bool
	pwb: bool
	filt: bool

	def store(self, knobs, switches):
		knobs[0x12] = knob2byte(self.srcmix)
		switches[0x10] = self.freqa
		switches[0x11] = self.freqb
		switches[0x12] = self.pwa
		switches[0x13] = self.pwb
		switches[0x14] = self.filt


@dataclass
class osca:
	freq: float
	ramp: bool
	pulse: bool
	pw: float
	sync: bool

	def store(self, knobs, switches):
		knobs[0x0D] = knob2byte(self.pw)
		knobs[0x15] = knob2byte(self.freq)
		switches[0x00] = self.pulse
		switches[0x01] = self.ramp
		switches[0x02] = self.sync


@dataclass
class oscb:
	freq: float
	fine: float
	ramp: bool
	tri: bool
	pulse: bool
	pw: float
	lo: bool
	kbd: bool

	def store(self, knobs, switches):
		knobs[0x0B] = knob2byte(self.pw)
		knobs[0x16] = knob2byte(self.freq)
		knobs[0x17] = knob2byte(self.fine)
		switches[0x03] = self.ramp
		switches[0x04] = self.tri
		switches[0x05] = self.pulse
		switches[0x06] = self.kbd
		switches[0x15] = self.lo


@dataclass
class mix:
	osca: float
	oscb: float
	noise: float

	def store(self, knobs, switches):
		knobs[0x0C] = knob2byte(self.osca)
		knobs[0x0A] = knob2byte(self.oscb)
		knobs[0x0E] = knob2byte(self.noise)


@dataclass
class filt:
	cutoff: float
	res: float
	env_amt: float
	kbd: bool
	attack: float
	decay: float
	sustain: float
	release: float

	def store(self, knobs, switches):
		knobs[0x00] = knob2byte(self.attack)
		knobs[0x01] = knob2byte(self.decay)
		knobs[0x02] = knob2byte(self.sustain)
		knobs[0x03] = knob2byte(self.release)
		knobs[0x08] = knob2byte(self.cutoff)
		knobs[0x09] = knob2byte(self.env_amt)
		knobs[0x0F] = knob2byte(self.res)
		switches[0x0E] = self.kbd


@dataclass
class amp:
	attack: float
	decay: float
	sustain: float
	release: float

	def store(self, knobs, switches):
		knobs[0x04] = knob2byte(self.attack)
		knobs[0x05] = knob2byte(self.decay)
		knobs[0x06] = knob2byte(self.sustain)
		knobs[0x07] = knob2byte(self.release)


@dataclass
class misc:
	glide: float
	unison: bool
	release: bool

	def store(self, knobs, switches):
		knobs[0x10] = knob2byte(self.glide)
		switches[0x07] = self.unison
		switches[0x0F] = self.release			


class patch(object):

	def __init__(self, p: pmod, l: lfo, w: wmod, oa: osca, ob: oscb, mx: mix, m: misc, f: filt, a: amp):
		self.modules = [p, l, w, oa, ob, mx, m, f, a]

	def build(self):
		knobs = [0] * PATCH_SIZE
		switches = [False] * PATCH_SIZE
		for m in self.modules:
			m.store(knobs, switches)
		assert(not switches[0x16])
		assert(not switches[0x17])

		patch_bytes = list()
		for i in range(0, PATCH_SIZE):
			assert(knobs[i] >= 0 and knobs[i] < 128)
			switch_val = 0x80 if switches[i] else 0x00
			patch_bytes.append(switch_val | knobs[i])
		return patch_bytes

	def __eq__(self, other):
		assert(isinstance(other, patch))
		self_bytes = self.build()
		other_bytes = other.build()
		assert(len(self_bytes) == len(other_bytes))
		for i in range(0, len(self_bytes)):
			if self_bytes[i] != other_bytes[i]:
				return False
		return True


def make_nvram():
	nvram = list()
	for p in get_patches():
		nvram.extend(p.build())
	nvram.extend([0] * (2 * PATCH_SIZE + 16))  # Unused space.
	assert(len(nvram) == 1024)
	with open('nvram.bin', 'wb') as f:
		f.write(bytes(nvram))


if __name__ == '__main__':
	make_nvram()

