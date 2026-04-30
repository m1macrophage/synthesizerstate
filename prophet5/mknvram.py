# 0x00 - filt attack  pot_16-23 (0x10-0x17)
# 0x01 - filt decay
# 0x02 - filt sustain
# 0x03 - filt release
# 0x04 - amp attack
# 0x05 - amp decay
# 0x06 - amp sustain
# 0x07 - amp release
# 0x08 - filt cutoff  pot_8-15 (0x08-0x0f)
# 0x09 - filt env amt
# 0x0a - osc b mix
# 0x0b - osc b pw
# 0x0c - osc a mix
# 0x0d - osc a pw
# 0x0e - noise mix
# 0x0f - filt res
# 0x10 - glide       pot_0-7 (0x00-0x07)
# 0x11 - lfo freq
# 0x12 - wmod src mix
# 0x13 - oilymod osc b
# 0x14 - polymod filt env amt.
# 0x15 - osc a freq
# 0x16 - osc b freq
# 0x17 - osc b fine

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
# 0x0a - pmod filt
# 0x0b - lfo ramp
# 0x0c - lfo tri
# 0x0d - lfo pulse
# 0x0e - filt kbd
# 0x0f - release
# 0x10 - wmod freq a
# 0x11 - wmod freq b
# 0x12 - wmod pw a
# 0x13 - wmod pw b
# 0x14 - wmod filter
# 0x15 - osc b lo

from dataclasses import dataclass

PATCH_SIZE = 0x18


def get_patches():
	return [
		patch(
			pmod(2, 3, False, True, False),
			lfo(3, True, True, False),
			wmod(7, False, True, False, True, True),
			osca(2, True, False, 5, True),
			oscb(7, 3, False, True, False, 5, False, False),
			mix(2, 3, 4),
			filt(10, 3, 2, True, 3, 3, 2, 1),
			amp(1, 2, 3, 4),
			misc(5, True, False)
		),
		#patch(pmod(1, 5, True, False, True)),
	]


def knob2byte(knob_value: float):
	return round(127 * knob_value / 10)


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
		knobs[0x12] = self.srcmix
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
		knobs[0x0D] = self.pw
		knobs[0x15] = self.freq
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

	def __init__(self, p: pmod, l: lfo, w: wmod, oa: osca, ob: oscb, mx: mix, f: filt, a: amp, m: misc):
		self.modules = [p, l, w, oa, ob, mx, f, a, m]

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


def make_nvram():
	nvram = list()
	for i, p in enumerate(get_patches()):
		nvram.extend(p.build())
	empty_space = (5 * 8 - (i + 1)) * PATCH_SIZE + 2 * PATCH_SIZE + 16
	nvram.extend([0] * empty_space)
	print(i, len(nvram))
	assert(len(nvram) == 1024)

	with open('nvram', 'wb') as f:
		f.write(bytes(nvram))


if __name__ == '__main__':
	make_nvram()

