from numpy import  array

POINT_OPERATORS = {

'IN' : array([
	[-1, 0, 0, ],
	[0, -1, 0, ],
	[0, 0, -1, ],
]),
'2Z' : array([
	[-1, 0, 0, ],
	[0, -1, 0, ],
	[0, 0, 1, ],
]),
'4Z' : array([
	[0, 1, 0, ],
	[-1, 0, 0, ],
	[0, 0, 1, ],
]),
'4Zi' : array([
	[0, 1, 0, ],
	[-1, 0, 0, ],
	[0, 0, -1, ],
]),
'6Z' : array([
	[1, 1, 0, ],
	[-1, 0, 0, ],
	[0, 0, 1, ],
]),
'6Zi' : array([
	[0, 1, 0, ],
	[-1, -1, 0, ],
	[0, 0, -1, ],
]),
'3Z' : array([
	[0, 1, 0, ],
	[-1, -1, 0, ],
	[0, 0, 1, ],
]),
'3Zi' : array([
	[1, 1, 0, ],
	[-1, 0, 0, ],
	[0, 0, -1, ],
]),
'TR' : array([
	[1, 0, 0, ],
	[0, 1, 0, ],
	[0, 0, 1, ],
]),
'MZ' : array([
	[1, 0, 0, ],
	[0, 1, 0, ],
	[0, 0, -1, ],
]),
'MX' : array([
	[-1, 0, 0, ],
	[0, 1, 0, ],
	[0, 0, 1, ],
]),
'MY' : array([
	[1, 0, 0, ],
	[0, -1, 0, ],
	[0, 0, 1, ],
]),
'MXY' : array([
	[0, 1, 0, ],
	[1, 0, 0, ],
	[0, 0, 1, ],
]),
'M-X-Y' : array([
	[0, -1, 0, ],
	[-1, 0, 0, ],
	[0, 0, 1, ],
]),
'4Z3' : array([
	[0, -1, 0, ],
	[1, 0, 0, ],
	[0, 0, 1, ],
]),
'3Z2' : array([
	[-1, -1, 0, ],
	[1, 0, 0, ],
	[0, 0, 1, ],
]),
'6Z5' : array([
	[0, -1, 0, ],
	[1, 1, 0, ],
	[0, 0, 1, ],
]),
'MX Hex' : array([
	[1, 0, 0, ],
	[-1, -1, 0, ],
	[0, 0, 1, ],
]),
'MY Hex' : array([
	[-1, -1, 0, ],
	[0, 1, 0, ],
	[0, 0, 1, ],
]),
'MU' : array([
	[1, 1, 0, ],
	[0, -1, 0, ],
	[0, 0, 1, ],
]),
'M-U' : array([
	[-1, 0, 0, ],
	[1, 1, 0, ],
	[0, 0, 1, ],
]),
'2X' : array([
	[1, 0, 0, ],
	[0, -1, 0, ],
	[0, 0, -1, ],
]),
'2Y' : array([
	[-1, 0, 0, ],
	[0, 1, 0, ],
	[0, 0, -1, ],
]),
'2XY' : array([
	[0, -1, 0, ],
	[-1, 0, 0, ],
	[0, 0, -1, ],
]),
'2-X-Y' : array([
	[0, 1, 0, ],
	[1, 0, 0, ],
	[0, 0, -1, ],
]),
'2X Hex' : array([
	[1, 0, 0, ],
	[-1, -1, 0, ],
	[0, 0, -1, ],
]),
'2U' : array([
	[-1, -1, 0, ],
	[0, 1, 0, ],
	[0, 0, -1, ],
]),
'2X-Y' : array([
	[1, 1, 0, ],
	[0, -1, 0, ],
	[0, 0, -1, ],
]),
'2-XY' : array([
	[-1, 0, 0, ],
	[1, 1, 0, ],
	[0, 0, -1, ],
]),
'3XYZ' : array([
	[0, 1, 0, ],
	[0, 0, 1, ],
	[1, 0, 0, ],
]),
'6S1' : array([
	[0, 1, 0, ],
	[-1, -1, 0, ],
	[0, 0, -1, ],
]),
'6S2' : array([
	[1, 1, 0, ],
	[-1, 0, 0, ],
	[0, 0, -1, ],
]),
'6S3' : array([
	[0, -1, 0, ],
	[1, 1, 0, ],
	[0, 0, -1, ],
]),
'6S4' : array([
	[-1, -1, 0, ],
	[1, 0, 0, ],
	[0, 0, -1, ],
]),
'3XYZ1' : array([
	[0, -1, 0, ],
	[0, 0, -1, ],
	[1, 0, 0, ],
]),
'3XYZ2' : array([
	[0, -1, 0, ],
	[0, 0, 1, ],
	[-1, 0, 0, ],
]),
'3XYZ3' : array([
	[0, 0, 1, ],
	[1, 0, 0, ],
	[0, 1, 0, ],
]),
'3XYZ4' : array([
	[0, 0, -1, ],
	[1, 0, 0, ],
	[0, -1, 0, ],
]),
'M Cub1a' : array([
	[0, -1, 0, ],
	[0, 0, 1, ],
	[1, 0, 0, ],
]),
'M Cub2a' : array([
	[0, 1, 0, ],
	[0, 0, -1, ],
	[1, 0, 0, ],
]),
'M Cub3a' : array([
	[0, 0, -1, ],
	[1, 0, 0, ],
	[0, 1, 0, ],
]),
'M Cub4a' : array([
	[0, 0, 1, ],
	[1, 0, 0, ],
	[0, -1, 0, ],
]),
'4X' : array([
	[1, 0, 0, ],
	[0, 0, 1, ],
	[0, -1, 0, ],
]),
'4Xi' : array([
	[-1, 0, 0, ],
	[0, 0, 1, ],
	[0, -1, 0, ],
]),
'4Y' : array([
	[0, 0, -1, ],
	[0, 1, 0, ],
	[1, 0, 0, ],
]),
'4Yi' : array([
	[0, 0, -1, ],
	[0, -1, 0, ],
	[1, 0, 0, ],
]),
'4Y3' : array([
	[0, 0, 1, ],
	[0, 1, 0, ],
	[-1, 0, 0, ],
]),
'4X3' : array([
	[1, 0, 0, ],
	[0, 0, -1, ],
	[0, 1, 0, ],
]),
'4S1' : array([
	[0, 1, 0, ],
	[-1, 0, 0, ],
	[0, 0, -1, ],
]),
'4S3' : array([
	[0, -1, 0, ],
	[1, 0, 0, ],
	[0, 0, -1, ],
]),
'2 Cub2' : array([
	[-1, 0, 0, ],
	[0, 0, 1, ],
	[0, 1, 0, ],
]),
'2 Cub3' : array([
	[-1, 0, 0, ],
	[0, 0, -1, ],
	[0, -1, 0, ],
]),
'2 Cub1' : array([
	[0, 0, -1, ],
	[0, -1, 0, ],
	[-1, 0, 0, ],
]),
'3XYZ12' : array([
	[0, 0, 1, ],
	[-1, 0, 0, ],
	[0, -1, 0, ],
]),
'2 Cub4' : array([
	[0, 0, 1, ],
	[0, -1, 0, ],
	[1, 0, 0, ],
]),
'3XYZ22' : array([
	[0, 0, -1, ],
	[-1, 0, 0, ],
	[0, 1, 0, ],
]),
'3XYZ32' : array([
	[0, 1, 0, ],
	[0, 0, -1, ],
	[-1, 0, 0, ],
]),
'M Cub1' : array([
	[0, 0, 1, ],
	[0, 1, 0, ],
	[1, 0, 0, ],
]),
'M Cub2' : array([
	[1, 0, 0, ],
	[0, 0, 1, ],
	[0, 1, 0, ],
]),
'M Cub3' : array([
	[1, 0, 0, ],
	[0, 0, -1, ],
	[0, -1, 0, ],
]),
'M Cub4' : array([
	[0, 0, -1, ],
	[0, 1, 0, ],
	[-1, 0, 0, ],
]),
'3XYZ1i' : array([
	[0, -1, 0, ],
	[0, 0, -1, ],
	[-1, 0, 0, ],
]),
'3XYZ2i' : array([
	[0, 1, 0, ],
	[0, 0, 1, ],
	[-1, 0, 0, ],
]),
'3XYZ3i' : array([
	[0, 0, -1, ],
	[-1, 0, 0, ],
	[0, -1, 0, ],
]),
'3XYZ4i' : array([
	[0, 0, 1, ],
	[-1, 0, 0, ],
	[0, 1, 0, ],
]),
'ZERO' : array([
	[0, 0, 0, ],
	[0, 0, 0, ],
	[0, 0, 0, ],
]),
}

# -----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	import numpy as np

	def _parse(name, inf, out):
		fl = True
		mat = []
		for i in range(4):
			row = inf.readline()
			dat = np.array([float(v) for v in row.split()])
			if dat[-1] != 0: fl = False
			mat.append(dat)

		mat = np.array(mat)[:3,:3]

		if fl:
			out.write("'%s' : array([\n" % name)
			for row in mat:
				out.write('\t[')
				for v in row:
					out.write("%.0f, " % v)
				out.write('],\n')
			out.write(']),\n')

	path = r"d:\YandexDisk\Python\PyPointGroup\delphi\Data\Operators.dat"
	outpath = '_data.py'

	with open(path,'rt',encoding='utf8') as inf:
		with open(outpath,'wt') as out:
			out.write("from numpy import array\n")
			out.write("POINT_OPERATORS = {\n")
			while True:
				name = inf.readline().strip()
				if not name:break
				_parse(name, inf, out)

			out.write("}\n")