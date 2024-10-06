OPCODES = {
	"0x00": "ADD r/m8, r8",
	"0x01": "ADD r/m16/32, r16/32",
	"0x02": "ADD r8, r/m8",
	"0x03": "ADD r16/32, r/m16/32",
	"0x04": "ADD AL, imm8",
	"0x05": "ADD eAX, imm16/32",
	"0x06": "PUSH ES",
	"0x07": "POP ES",
	"0x08": "OR r/m8, r8",
	"0x09": "OR r/m16/32, r16/32",
	"0x0A": "OR r8, r/m8",
	"0x0B": "OR r16/32, r/m16/32",
	"0x0C": "OR AL, imm8",
	"0x0D": "OR eAX, imm16/32",
	"0x0E": "PUSH CS",
}


def decode_hex(hex):
	if len(hex) >= 2:
		op_code_hex = hex[0:2]
		instruction, operand_size = OPCODES.get("0x" + op_code_hex, (None, None))
		if instruction:
			if len(hex) > 2:
				operand_hex = hex[2:2 + operand_size * 2]
				operand = int(operand_hex, 16)
				return instruction, operand
			else:
				return instruction, None
	return None, None


def get_instruction(hex_instructions_list):
	assembly_instructions = []
	for hex in hex_instructions_list:
		if not isinstance(hex, str) or not all(c in '0123456789abcdefABCDEF' for c in hex):
			assembly_instructions.append("Invalid instruction format")
		instruction_decoded, operand_decoded = decode_hex(hex)
		if instruction_decoded:
			assembly_instructions.append(f"{instruction_decoded} {operand_decoded if operand_decoded is not None else 'N/A'}")
		else:
			assembly_instructions.apppend("Unknown instruction")
	return assembly_instructions
