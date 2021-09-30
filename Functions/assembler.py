JMP_SIZE = 1
JMPIF_SIZE = 1
WRITE_ENABLE_SIZE = 1
WRITE_SOURCE_SIZE = 2
ALU_OP_SIZE = 4
REG_ADDR1_SIZE = 5
REG_ADDR2_SIZE = 5
WRITE_ADDR_SIZE = 5
CONST_SIZE = 8

ADDRESS_SIZE = 5
REGISTER_SIZE = 16
REGISTER_NUMBER = 16

NUMBER = 1
SWITCH = 2
REGISTER = 3

ADD = 0b011000
SUB = 0b011001
XOR = 0b101111
OR = 0b101110
AND = 0b010101
SRL = 0b100101
SLL = 0b100111
SRA = 0b100100
LTU = 0b000001
LTS = 0b000000
GEU = 0b001011
GES = 0b001010
EQ = 0b001100
NE = 0b001101

LABELS = dict()


class Instruction(object):

	def __init__(self):
		self.jmp = 'x'
		self.jmpif = 'x'
		self.write_enable = 'x'
		self.write_source = 'x'
		self.alu_operation = 'x'
		self.reg_address1 = 'x'
		self.reg_address2 = 'x'
		self.write_address = 'x'
		self.const = 'x'

	def set_write_addr(self, dest):
		self.write_address = dest.value

	def set_read_addr_1(self, dest):
		self.reg_address1 = dest.value

	def set_read_addr_2(self, dest):
		self.reg_address1 = dest.value

	def set_write_source(self, other):
		if other == NUMBER:
			self.write_source = 0
		elif other == SWITCH:
			self.write_source = 1
		elif other == REGISTER:
			self.write_source = 2
		else:
			raise InvalidInstructionSource(
				'Internal::(Instruction-class::(Write-Source))')

	def set_const(self, other):
		if other.value >= pow(2, CONST_SIZE):
			print('Warning: '
			      f'const value: {other.value} is too big for 8 bit, '
			      f'overflowing to {other.value % pow(2, CONST_SIZE)}'
			      )
		self.const = other.value % 255

	def __repr__(self):
		return ('Instruction class {'
		        f'jmp: {self.jmp}, jmpif: {self.jmpif}, we: {self.write_enable}, '
		        f'ws: {self.write_source}, alu: {self.alu_operation}, '
		        f'ra1: {self.reg_address1}, ra2: {self.reg_address2}, '
		        f'wa: {self.write_address}, const: {self.const}'
		        '}'
		        )

	def __str__(self):
		return self.__repr__()

	def compile(self):
		return '0x' + self.__tohex(self.jmp, JMP_SIZE) + \
		       self.__tohex(self.jmpif, JMPIF_SIZE) + \
		       self.__tohex(self.write_enable, WRITE_ENABLE_SIZE) + \
		       self.__tohex(self.write_source, WRITE_SOURCE_SIZE) + \
		       self.__tohex(self.alu_operation, ALU_OP_SIZE) + \
		       self.__tohex(self.reg_address1, REG_ADDR1_SIZE) + \
		       self.__tohex(self.reg_address2, REG_ADDR1_SIZE) + \
		       self.__tohex(self.write_address, WRITE_ADDR_SIZE) + \
		       self.__tohex(self.const, CONST_SIZE)

	@staticmethod
	def __tohex(num, size):
		if num == 'x':
			return 'x' * size
		st = hex(num)[2:]
		return '0' * (size - len(st)) + st


class Operand(object):

	def __init__(self, st):
		if st[0] == '0':
			self.type = NUMBER
			if st[1] == 'x':
				self.value = int(st, 16)
			elif st[1] == 'o':
				self.value = int(st, 8)
			elif st[1] == 'b':
				self.value = int(st, 2)
		elif st.isdigit():
			self.type = NUMBER
			self.value = int(st)
		elif st[0] == 'e' and st[2] == 'x':
			self.type = REGISTER
			if st == 'eax':
				self.value = 1
			elif st == 'ebx':
				self.value = 2
			elif st == 'ecx':
				self.value = 3
			elif st == 'edx':
				self.value = 4
		elif st[0] == 'r' and st[-1] == 'd':
			self.type = REGISTER
			try:
				regnum = int(st[1:-1])
			except ValueError:
				raise ValueError(f'invalid register number: {st[1:-1]}')
			if regnum < 4 or regnum >= REGISTER_NUMBER:
				raise ValueError(f'invalid register number: {st[1:-1]}')
		elif st == 'NULL':
			self.type = REGISTER
			self.value = 0
		elif st == 'SWITCH':
			self.type = SWITCH
		else:
			self.type = -1

	def __eq__(self, other):
		return self.type == other

	def __ne__(self, other):
		return self.type != other


class Label(object):

	def __init__(self, label, pc):
		if label[0] == '0':
			if label[1] == 'x':
				self.value = int(label, 16)
			elif label[1] == 'o':
				self.value = int(label, 8)
			elif label[1] == 'b':
				self.value = int(label, 2)
		elif label.isdigit():
			self.type = NUMBER
			self.value = int(label)
		elif label not in LABELS:
			raise LabelNameError(label)
		else:
			self.value = pow(2, ADDRESS_SIZE) + (LABELS[label] - pc)


class InvalidInstruction(SyntaxError):
	def __init__(self, message):
		super().__init__(f'invalid instruction: {message}\n'
		                 'it should be one of: inc, dec, mov, add, sub, xor, or, and, srl,\n'
		                 'sll, sra, sla, ltu, lts, geu, ges, eq, ne, jmp, jmpif'
		                 )


class InvalidInstructionSource(SyntaxError):
	def __init__(self, message):
		super().__init__(f'invalid instruction operand: {message}\n'
		                 'it should be hex (0x...), octal(0o...), binary(0b...),\n'
		                 'decimal (...), null (NULL), value on switches (SWITCH),\n'
		                 'or register (eax, ebx, ecx, edx, r5d, r6d, ..., r...d)'
		                 )


class InvalidInstructionDestination(SyntaxError):
	def __init__(self, message):
		super().__init__(f'invalid instruction operand: {message}\n'
		                 'it should be register (eax, ebx, ecx, edx, r5d, r6d, ..., r...d)'
		                 )


class InvalidLogicOperation(SyntaxError):
	def __init__(self, message):
		super().__init__(f'instruction {message} should be placed only after\n'
		                 'jmpif instruction'
		                 )


class InvalidJmpOpetarion(SyntaxError):
	def __init__(self, message):
		super().__init__(f'expected logic instruction, but got {message}\n'
		                 'after jmpif instruction should be logic instruction')


class LabelNameError(SyntaxError):
	def __init__(self, message):
		super().__init__(f'label {message} not defined')


class LabelRedefinition(SyntaxError):
	def __init__(self, message):
		super().__init__(f'label {message} has been defined before')


def parse(filename: str):
	file = open(filename)
	print('started', filename)
	program_counter = 0
	jump_wait = None
	while True:
		new_line = file.readline()
		if ';' in new_line:
			new_line = new_line[:new_line.index(';')]
		line = list(map(lambda x: x.strip(), new_line.split()))
		if len(line) == 0:
			continue
		elif line[0][-1] == ':':
			label = line[0][-1]
			if jump_wait is not None:
				raise InvalidJmpOpetarion(line[0])
			if label in LABELS:
				raise LabelRedefinition(label)
			LABELS[line[0][:-1]] = program_counter
			continue
		else:
			if jump_wait is not None:
				instruction = parce_line(new_line, program_counter, jump_wait)
				jump_wait = None
				program_counter -= 1
			else:
				instruction = parce_line(new_line, program_counter, None)
				if instruction.jmpif:
					jump_wait = instruction
		print(program_counter, instruction)
		program_counter += 1
	#
	file.close()


def parce_line(line_str: str, program_counter: int, jump_wait):
	instr = Instruction()
	if line_str == '':
		return None
	line = list(map(lambda x: x.strip().lower(), line_str.split()))
	if (line[0] not in ('ltu', 'lts', 'geu', 'ges', 'eq', 'ne') and
				jump_wait is not None):
		raise InvalidJmpOpetarion(line[0])
	#
	if line[0] in ('inc', 'dec'):
		if line[0] == 'inc':
			line[0:2] = ['add', line[1], '0x1']
		elif line[1] == 'dec':
			line[0:2] = ['sub', line[1], '0x1']
	#
	dest = Operand(line[1])

	source = Operand(line[2])
	if line[0] in ('mov', 'add', 'sub', 'xor', 'or', 'and', 'srl',
	               'sll', 'sra', 'sla'):
		instr.write_enable = 1
		if dest != REGISTER:
			raise InvalidInstructionSource(line[1])
		elif dest.value == 0:
			print('Warning: trying to change NULL register\n'
		            'NULL register is readonly, it will not make any changes')
		else:
			instr.set_write_addr(dest)
		#
		if source == REGISTER:
			instr.set_read_addr_2(source)
			instr.set_write_source(REGISTER)
		elif dest == NUMBER:
			instr.set_const(source)
			instr.set_write_source(NUMBER)
		elif dest == SWITCH:
			instr.set_write_source(SWITCH)
		else:
			raise InvalidInstructionDestination(line[2])
		#
		if line[0] == 'mov':
			instr.set_read_addr_1(Operand('NULL'))
		else:
			instr.set_read_addr_1(dest)
		#
		if line[0] == 'mov':
			instr.alu_operation = ADD
		elif line[0] == 'add':
			instr.alu_operation = ADD
		elif line[0] == 'sub':
			instr.alu_operation = SUB
		elif line[0] == 'xor':
			instr.alu_operation = XOR
		elif line[0] == 'or':
			instr.alu_operation = OR
		elif line[0] == 'and':
			instr.alu_operation = AND
		elif line[0] == 'srl':
			instr.alu_operation = SRL
		elif line[0] == 'sll':
			instr.alu_operation = SLL
		elif line[0] == 'sra':
			instr.alu_operation = SRA
		elif line[0] == 'sla':
			instr.alu_operation = SLL
		else:
			raise RuntimeError('Internal::(Operator-type)')
		return instr
	#
	#
	elif line[0] in ('ltu', 'lts', 'geu', 'ges', 'eq', 'ne'):
		if jump_wait is None:
			raise InvalidLogicOperation(line[0])
		if dest != REGISTER:
			raise InvalidInstructionDestination(line[1])
		if source != REGISTER:
			raise InvalidInstructionDestination(line[2])
		jump_wait.set_read_addr_1(dest)
		jump_wait.set_read_addr_2(source)
		jump_wait.set_write_source(REGISTER)
		if line[0] == 'ltu':
			jump_wait.alu_operation = LTU
		elif line[0] == 'lts':
			jump_wait.alu_operation = LTS
		elif line[0] == 'geu':
			jump_wait.alu_operation = GEU
		elif line[0] == 'ges':
			jump_wait.alu_operation = GES
		elif line[0] == 'eq':
			jump_wait.alu_operation = EQ
		elif line[0] == 'ne':
			jump_wait.alu_operation = NE
		else:
			raise RuntimeError('Internal::(Operator-type)')
		return jump_wait
	#
	#
	elif line[0] in ('jmp', 'jmpif'):
		label = Label(line[1], program_counter)
		instr.set_const(label)
		if line[0] == 'jmp':
			instr.jmp = 1
		else:
			instr.jmpif = 1
		return instr
	#
	#
	else:
		raise RuntimeError('Internal::(Operator-main-branch)')


parse("/home/kostya/Desktop/asm.s")
